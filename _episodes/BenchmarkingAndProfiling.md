---
title: "Benchmarking and profiling"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

We are working toward [optimization]({{page.root}}{% link _episodes/Optimization.md %}) and [parallel computing]({{page.root}}{% link _episodes/ParallelComputing.md %}).
We need to understand the current state of our code before we should even think about optimization or parallel computing.


## Benchmarking vs Profiling
These two processes are quite similar in that they involve running a program and then measuring the resources that were used.
You can think of benchmarking is the high-level view of a process, where as profiling is zooming in to each of the lines of code to understand where all the resources are being used.

The primary resources that people track are:
- Time to execute,
- CPU usage,
- RAM usage,
- GPU usage, and
- Disk usage (I/O)

When benchmarking, it is common to look at the average, peak, or total value for each of these resources.
When you have benchmarked your software you will then have an understanding of how it performs in it's current state, and what resources are required on an HPC, or when purchasing new equipment.

When you are profiling a piece of code, you are typically trying to understand *why* it is using the given resource (usually because you'd like to use less of them).
When profiling the same resources are tracked, however they are usually tracked at a much higher cadence, and often at the level of each line of code.

## Benchmarking
Benchmarking is the process of running code on a target system to determine the typical behavior or resource usage.
Benchmarking is different from profiling, in that with profiling we want a detailed report of what our software is doing at various times with an eye to improving the program, where as benchmarking is only interested in estimating how much resources are required to run a program in it's current state.
In the context of this workshop we are mostly interested in determining the resource usage in terms of:

1. run time
2. peak RAM use
3. CPU utilization

The peak RAM use and CPU usage will determine how many copies of our task we can run on a node at once, which we can then multiply by the total run time to estimate our kSU requirement.

Whilst it's possible to estimate the cpu/time/ram requirements by running tasks on a desktop and then "scaling up" the results, this is an unreliable method, and usually requires a buffer of uncertainty.
The best method is to run some test jobs on the target machine and then ask SLURM how much resources were used for those jobs.
The key to this method is the `sacct` (SLURM accounting) task.

In the example below I run `sacct` on a job that has completed:
~~~
sacct -j 29780362
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- -------- 
29780362           test    skylake      oz983          4    TIMEOUT      0:0 
29780362.ba+      batch                 oz983          4  CANCELLED     0:15 
29780362.ex+     extern                 oz983          4  COMPLETED      0:0
~~~
{: .output}

There area few things to unpack here so lets go in order of columns:
- JobID - This shows all the jobs you asked to see. Note that there are three job steps shown here.
  - 29780362 - This is the parent job, this row will show summary attributes that include all other steps.
  - 29780362.ba+ - this is the "batch" job, what was executed within your bash script.
  - 29780362.ex+ - this is the "external" tasks that were run, typically this will be small/none in terms of resource usage
  - 29780362.0 - [Not shown above] steps that end in a `.<number>` are created each time you use `srun` to launch a task. Unless you are using mpi jobs this is not required so you may not see this.
- JobName - The name of the job/step
- Partition - The cluster name or partition that the job ran on
- Account - The account that will be charged for the resources used
- AllocCPUS - The number of CPUs that were allocated to the job
- State - The final state of the job
  - CANCELLED Job was cancelled by the user or a sysadmin
  - COMPLETED Job finished normally, with exit code 0
  - FAILED Job finished abnormally, with a non-zero exit code
  - OUT_OF_MEMORY Job was killed for using too much memory
  - TIMEOUT	Job was killed for exceeding its time limit
- ExitCode - The (highest) exit code for the job along with the signal that caused it to exit in the format exitcode:signal

In the above example, I submitted a task that requested minute wall time.
The job ran over time and was therefore cancelled by SLURM.
The SLURM controller sent [signal](https://www.computerhope.com/unix/signals.htm) 15 (SIGTERM) to the script which caused it to exit with code 0.

> ## What else can `sacct` do?
> Read the `man` pages for `sacct` and see what other reporting options are available.
> For a short hand view try `sacct -e`.
> > ## `sacct -e`
> > ~~~
> > Account             AdminComment        AllocCPUS           AllocNodes         
> > AllocTRES           AssocID             AveCPU              AveCPUFreq         
> > AveDiskRead         AveDiskWrite        AvePages            AveRSS             
> > AveVMSize           BlockID             Cluster             Comment            
> > Constraints         Container           ConsumedEnergy      ConsumedEnergyRaw  
> > CPUTime             CPUTimeRAW          DBIndex             DerivedExitCode    
> > Elapsed             ElapsedRaw          Eligible            End                
> > ExitCode            Flags               GID                 Group              
> > JobID               JobIDRaw            JobName             Layout             
> > MaxDiskRead         MaxDiskReadNode     MaxDiskReadTask     MaxDiskWrite       
> > MaxDiskWriteNode    MaxDiskWriteTask    MaxPages            MaxPagesNode       
> > MaxPagesTask        MaxRSS              MaxRSSNode          MaxRSSTask         
> > MaxVMSize           MaxVMSizeNode       MaxVMSizeTask       McsLabel           
> > MinCPU              MinCPUNode          MinCPUTask          NCPUS              
> > NNodes              NodeList            NTasks              Priority           
> > Partition           QOS                 QOSRAW              Reason             
> > ReqCPUFreq          ReqCPUFreqMin       ReqCPUFreqMax       ReqCPUFreqGov      
> > ReqCPUS             ReqMem              ReqNodes            ReqTRES            
> > Reservation         ReservationId       Reserved            ResvCPU            
> > ResvCPURAW          Start               State               Submit             
> > SubmitLine          Suspended           SystemCPU           SystemComment      
> > Timelimit           TimelimitRaw        TotalCPU            TRESUsageInAve     
> > TRESUsageInMax      TRESUsageInMaxNode  TRESUsageInMaxTask  TRESUsageInMin     
> > TRESUsageInMinNode  TRESUsageInMinTask  TRESUsageInTot      TRESUsageOutAve    
> > TRESUsageOutMax     TRESUsageOutMaxNode TRESUsageOutMaxTask TRESUsageOutMin    
> > TRESUsageOutMinNode TRESUsageOutMinTask TRESUsageOutTot     UID                
> > User                UserCPU             WCKey               WCKeyID            
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

For our current needs the relevant fields are as follows:

| Field     | Description                                                  |
| --------- | ------------------------------------------------------------ |
| TimeLimit | How much time was *allocated* to the job                     |
| Elapsed   | How much time was *used* by the job                          |
| NCPUS     | *allocated* number of CPUS                                   |
| UserCPU   | Time spent on user time (the program you ran)                |
| SystemCPU | Time spent on system time (libraries called by your program) |
| TotalCPU  | Total time spent (User + System)                             |
| CPUTime   | NCPUS * Elapsed                                              |
| ReqMem    | Requested memory                                             |
| MaxRSS    | Maximum RSS (used memory)                                    |
| MaxVMSize | Maximum VMSize (addressable memory )                         |

We can use these fields to get the following information:
~~~
sacct -j  29780362 -o JobID,TimeLimit,Elapsed,NCPUS,UserCPU,SystemCPU,TotalCPU,CPUTime,ReqMem,MaxRSS,MaxVMSize
JobID         Timelimit    Elapsed      NCPUS    UserCPU  SystemCPU   TotalCPU    CPUTime     ReqMem     MaxRSS  MaxVMSize 
------------ ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- 
29780362       00:01:00   00:01:16          4  00:03.649  00:02.291  00:05.941   00:05:04         4G                       
29780362.ba+              00:01:19          4  00:03.649  00:02.290  00:05.939   00:05:16                  572K    211236K 
29780362.ex+              00:01:16          4   00:00:00  00:00.001  00:00.001   00:05:04                   88K      4380K 
~~~
{: .output}

For this particular job we requested 4 CPUs and used 3.649 seconds of user time, 2.291 seconds of system time, for a total of 5.941 seconds, and ran for 1minute 16seconds.
The amount of time that could have been used if we had used all 4 CPU cores at 100% is 5:04 minutes, meaning that we used less than 1% of the allocated resources.
We requested 4GB of RAM but had a peak VMSize of just 212MB, meaning that we could have requested less RAM.
For my example task I would have been charged 1minute x 4 cores worth of resources, but have made use of less than 1% of those resources.

When benchmarking your jobs, it is clearly important to have the jobs run successfully.
Once a job runs successfully you can then use `sacct` to figure out the time, CPU, and RAM usage.
Note that the `sacct` system only polls the jobs at some interval (30seconds?) and therefore it is possible that the MaxVMSize will not capture short duration peaks in RAM usage.
This polling interval also means that your jobs that run overtime will not always be cancelled exactly at the wall time requested (see the example above).

For longer running jobs you can monitor their resource usage in near-real time thanks to [this nifty website](https://supercomputing.swin.edu.au/monitor/).
Take a minute to explore the site and see what kinds of efficiency people are getting in their jobs.


## Profiling

We'll be using the [scalene](https://pypi.org/project/scalene/) package to profile our python code.
Unlike other profiling systems, scalene doesn't require you to edit the source code as part of the profiling process.
Instead you simply run `scalene your_prog.py` and it will run your code and deliver a report.