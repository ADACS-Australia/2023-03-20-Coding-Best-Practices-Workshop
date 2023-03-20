---
title: "Working on an HPC"
teaching: 15
exercises: 15
questions:
- "How do I access an HPC facility?"
- "How do I run tasks on an HPC?"
- "How do I request resources for my jobs?"
- "How do I access already installed software?"
- "How can I install other software?"
objectives:
- "Understand how to login and submit jobs"
- "Know how to create a workflow with job dependencies and array jobs"
- "Know how to access/install/use software"
keypoints:
- "Plan your work and map it onto a workflow for SLURM to execute"
- "Find software with LMOD or Singularity / Docker hub"
---

![NCI]({{page.root}}{%link fig/NCILogo.png %}) HPC resources for this workshop are provided by The National Computational Infrastructure [NCI](https://nci.org.au/).
In this lesson we'll be taking an accelerated path through the [Gadi User Guide](https://opus.nci.org.au/display/Help/Gadi+User+Guide) which is very thorough and recommended when you use NCI for your own work.

## Logging in 
We will be working with the NCI HPC cluster called Gadi, you should have an account, and be a member of the group `vp91`.
See the [setup]({{page.root}}{% link _episodes/Setup.md %}#an-account-on-nci) page if you need more information.

To connect to a login node you should use ssh:
~~~
ssh <user>@gadi.nci.org.au
~~~
{: .language-bash}

You will be asked for a password each time you connect.
If you would prefer to work with ssh keys for password-less login, [this tutorial](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/) is quite helpful.

Upon login you'll be greeted with a message of the day:

~~~
###############################################################################
#                  Welcome to the NCI National Facility!                      #
#      This service is for authorised clients only. It is a criminal          #
#      offence to:                                                            #
#                - Obtain access to data without permission                   #
#                - Damage, delete, alter or insert data without permission    #
#      Use of this system requires acceptance of the Conditions of Use        #
#      published at http://nci.org.au/users/nci-terms-and-conditions-access   #
###############################################################################
|         gadi.nci.org.au - 185,032 processor InfiniBand x86_64 cluster       | 
===============================================================================

Jul 5 2022 /scratch File Expiry
   The file expiry system is now active on /scratch: files that have not been
   accessed in more than 100 days will be automatically quarantined for 14 days
   and then permanently deleted. For more details, please see
   https://opus.nci.org.au/x/BABTCQ.

Oct 4 2022 Account Status Information on Login
   Whenever logging in from outside of Gadi, all users will now be presented
   with a brief summary about file expiry and projects near compute and/or
   storage quotas. This can be configured using the "login-info-conf" utility.
   For more information, please see https://opus.nci.org.au/x/HoABCw.

===============================================================================
~~~
{: output}

and you'll either be working on the `gadi-login-01` or `gadi-login-02` log-in node.
It doesn't matter which node you join.

You can check the groups that you are a member of using the `groups` command:
~~~
[pjh562@gadi-login-01 ~]$ groups
vp91 S.U
~~~
{: .language-bash}

You ou should be a member of the `vp91` group, as that is the one that we'll be using for this course.

You have access to two file systems: **home** and **scratch**.
The **home** file system holds your home or `~/` directory and files, and is limited to 10GB.
It is backed up but should not be used for frequent file access (don't do work here).
The **scratch** file system is a large scratch storage for general use.
It is *not* backed up, files older than 10days are marked for deletion.

> ## Create a personal work folder
> Navigate to `/scratch/vp91`.
> Create a directory in here with your username (if it doesn't already exist)
> 
> > ## Solution
> > ~~~
> > cd /scratch/vp91
> > ls
> > mkdir ${USER}
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

Please use your username and not some other personal nickname.

## How do I run tasks on an HPC
Currently you will have only a very minimal set of software loaded.
To see what software modules you have loaded:
~~~
module list
~~~
{: .language-bash}

~~~
Currently Loaded Modulefiles:
 1) pbs  
~~~
{: .output}

Effectively we start of with just enough tools to submit and monitor jobs.

Remember from last lesson, we need to use a scheduler in order for our jobs to be run on the compute nodes:
![JobQueuing]({{page.root}}{% link fig/queueing_infog.png %})


### Querying the queue system
Before we run any jobs we need to see what resources are available.
One way to do this is using the `qstat -Q` command which will report information similar to:

~~~
[pjh562@gadi-login-01 ~]$ qstat -Q
Queue              Max   Tot Ena Str   Que   Run   Hld   Wat   Trn   Ext Type
---------------- ----- ----- --- --- ----- ----- ----- ----- ----- ----- ----
normal               0   812 yes yes   779     0    20    13     0     0 Rou*
normal-exec          0  4265 yes yes  2322  1593   339     0     0    11 Exe*
express              0     0 yes yes     0     0     0     0     0     0 Rou*
express-exec         0   138 yes yes    28    92    18     0     0     0 Exe*
copyq                0    20 yes yes     0     0     0    20     0     0 Rou*
copyq-exec           0    61 yes yes     3    52     6     0     0     0 Exe*
gpuvolta             0     0 yes yes     0     0     0     0     0     0 Rou*
gpuvolta-exec        0   480 yes yes   152   258    63     0     0     0 Exe*
hugemem-exec         0    79 yes yes     7    66     6     0     0     0 Exe*
hugemem              0     0 yes yes     0     0     0     0     0     0 Rou*
biodev               0     0 yes yes     0     0     0     0     0     0 Rou*
biodev-exec          0    21 yes yes     0    21     0     0     0     0 Exe*
megamembw-exec       0     6 yes yes     4     2     0     0     0     0 Exe*
megamembw            0     0 yes yes     0     0     0     0     0     0 Rou*
normalbw-exec        0  2301 yes yes   301  1902    95     0     0     3 Exe*
normalbw             0     1 yes yes     0     0     0     1     0     0 Rou*
expressbw-exec       0     7 yes yes     0     7     0     0     0     0 Exe*
expressbw            0     0 yes yes     0     0     0     0     0     0 Rou*
normalsl-exec        0    10 yes yes     0    10     0     0     0     0 Exe*
normalsl             0     0 yes yes     0     0     0     0     0     0 Rou*
hugemembw-exec       0    12 yes yes     0     9     3     0     0     0 Exe*
hugemembw            0     0 yes yes     0     0     0     0     0     0 Rou*
megamem              0     0 yes yes     0     0     0     0     0     0 Rou*
megamem-exec         0     1 yes yes     0     1     0     0     0     0 Exe*
gpursaa              0     0 yes yes     0     0     0     0     0     0 Rou*
gpursaa-exec         0     1 yes yes     0     1     0     0     0     0 Exe*
analysis             0     0 yes yes     0     0     0     0     0     0 Rou*
analysis-exec        0     2 yes yes     0     2     0     0     0     0 Exe*
dgxa100              0     0 yes yes     0     0     0     0     0     0 Rou*
dgxa100-exec         0    75 yes yes    68     6     1     0     0     0 Exe*
normalsr             0     0 yes yes     0     0     0     0     0     0 Rou*
normalsr-exec        0     0 yes yes     0     0     0     0     0     0 Exe*
expresssr            0     0 yes yes     0     0     0     0     0     0 Rou*
expresssr-exec       0     0 yes yes     0     0     0     0     0     0 Exe*
~~~
{: .output}

A description of the columns is:
~~~
       Description of columns:

       Queue          Queue name

       Max            Maximum number of jobs allowed to run concurrently in this queue

       Tot            Total number of jobs in the queue

       Ena            Whether the queue is enabled or disabled

       Str            Whether the queue is started or stopped

       Que            Number of queued jobs

       Run            Number of running jobs

       Hld            Number of held jobs

       Wat            Number of waiting jobs

       Trn            Number of jobs being moved (transiting)

       Ext            Number of exiting jobs

       Type           Type of queue: execution or routing
~~~
{: .output}

The **queue** column lists the name of the job queue.
See [Queue Structure](https://opus.nci.org.au/display/Help/Queue+Structure) for a list of what all the queues are for and the hardware available for each, and [Queue Limits](https://opus.nci.org.au/display/Help/Queue+Limits) for a break down of the limits for each of the available queues.

The **run** column shows how many jobs are currently running in that queue and the **que** column shows how many jobs are queued (waiting to run) for that queue.
Together we can use these get a feel for which queues are busy/free.



## Running Jobs
There are two types of jobs that can be run: either a batch job where PBSPro executes a script on your behalf, or an interactive job whereby you are given direct access to a compute node and you can do things interactively.


### Interactive jobs
We will start with a simple **interactive** job.
Use `qsub -I` to start an interactive job.
You should see a sequence of output as follows:
~~~
[pjh562@gadi-login-01 ~]$ qsub -I -qnormal -lwalltime=00:05:00,storage=scratch/vp91
qsub: waiting for job 76970825.gadi-pbs to start
qsub: job 76970825.gadi-pbs ready

[pjh562@gadi-cpu-clx-1891 ~]$
~~~
{: .output}

Note that the prompt has changed to be `gadi-cpu-clx-1891` which tell us the name of the node we are working. 
You will most likely get a different node name.

When you finish with an interactive session you can exit it using `exit` or `<ctrl>+d` to end the ssh session, and then again to exit the job allocation.

Before we exit the interactive session, let's have a look at what the job queue looks like.

~~~
[pjh562@gadi-cpu-clx-1891 ~]$ qstat -u ${USER} 

gadi-pbs: 
                                                                 Req'd  Req'd   Elap
Job ID               Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
-------------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
76970825.gadi-pbs    pjh562   normal-* STDIN      20925*   1   1  500mb 10:00 R 00:02
[pjh562@gadi-cpu-clx-1891 ~]$ exit
logout

qsub: job 76970825.gadi-pbs completed
[pjh562@gadi-login-01 ~]$ 
~~~
{: .output}

You can see that each job has an ID (above it is 76970825), and we can see which queue the job is in, how many nodes (NDS) and tasks (TSK) have been assigned, and what the requested memory/time is, as well as how long the job has been running (Elap Time).
We didn't request a specific amount of nodes/tasks/memory so we get the default.

If we have no jobs in the queue then `qstat` will just return nothing.

Interactive jobs are good for debugging your code, but usually leave the compute node idle whilst you read/think/code.
Interactive jobs should be used sparingly, in preference of batch jobs.

### Batch jobs
The most common type of job that you will run on an HPC is a batch job.
A batch job requires that you have a script that describes all the processing that you will need to do, as well as an estimate of the resources that you'll need.
With these bits of information the SLURM scheduler can then appropriately assign you resources and execute the work.

Lets run a basic hello world script, watch it run, and then pick apart what happened.

> ## The python script
> `/scratch/vp91/pjh562/scripts/hello.py`
> ~~~
> #! /usr/bin/env python
> 
> import os
> 
> host = os.environ["HOSTNAME"]
> print(f"Hello from the world of {host}")
> ~~~
> {: .language-python}
{: .callout}

> ## The bash script
> `/scratch/vp91/pjh562/scripts/first_script.sh`
> ~~~
> #! /usr/bin/env bash
> #
> #PBS -N hello
> #PBS -o output.txt
> #PBS -e error.txt
> #
> #PBS -l walltime=00:05:00
> #PBS -l mem=200MB
> 
> # load the python module
> module load python/3.8.5
> 
> # move to the work directory
> cd /scratch/vp91/${USER}
> # do the work
> python3 ../pjh562/scripts/hello.py | tee hello.txt
> sleep 120
> ~~~
> {: .language-bash}
{: .callout}

We then submit the batch script to SLURM using the `qsub` command from our own directory, and view our job list:
~~~
[pjh562@gadi-login-04 pjh562]$ qsub scripts/first_script.sh 
77477612.gadi-pbs
[pjh562@gadi-login-04 pjh562]$ qstat -u ${USER}

gadi-pbs: 
                                                                 Req'd  Req'd   Elap
Job ID               Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
-------------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
77477612.gadi-pbs    pjh562   normal-* hello         --    1   1  200mb 00:05 Q   -- 
~~~
{: .output}

Initially our jobs is not running (S column shows Q), but after a minute or so we see:

~~~
[pjh562@gadi-login-04 pjh562]$ qstat  -u ${USER}

gadi-pbs: 
                                                                 Req'd  Req'd   Elap
Job ID               Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
-------------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
77477612.gadi-pbs    pjh562   normal-* hello      34700*   1   1  200mb 00:05 R 00:00
~~~
{: .output}

The script will take a few seconds to run the python script, and then sleep for 2 minutes so that we have a chance to catch it in the queue.

We'll get the out put ina file called `res.txt`, which sits in the directory from which we submitted the `qsub` job.

~~~
[pjh562@gadi-login-04 pjh562]$ more hello.txt
Hello from the world of gadi-cpu-clx-1891.gadi.nci.org.au

[pjh562@gadi-login-04 pjh562]$ more output.txt 
Hello from the world of gadi-cpu-clx-1891.gadi.nci.org.au

======================================================================================
                  Resource Usage on 2023-03-20 22:53:37:
   Job Id:             77478053.gadi-pbs
   Project:            vp91
   Exit Status:        0
   Service Units:      0.07
   NCPUs Requested:    1                      NCPUs Used: 1               
                                           CPU Time Used: 00:00:00        
   Memory Requested:   200.0MB               Memory Used: 6.42MB          
   Walltime requested: 00:05:00            Walltime Used: 00:02:01        
   JobFS requested:    100.0MB                JobFS used: 0B              
======================================================================================

[pjh562@gadi-login-04 pjh562]$ more error.txt
~~~
{: .output}

Now let's review what we did:
1. Created a python script which did all the "hard" work.
2. Created a bash script which told PBSPro about the resources that we needed, and how to invoke our program.
   1. The `#PBS` comments at the top of the bash script are ignored by bash, but are picked up by PBSPro.
      1. `-N` is what shows up in the `qsub` listing. It defaults to your script name, but can be renamed here.
      2. `-o` is the location of the file that will contain all of the `STDOUT` from the running of your program, plus a summary of resource usage at the end.
      3. `-e`  is the location of the file that will have the `STDERR` from your program
      4. `-l walltime=[H:M:S]` is the (wall) time that this job requires. If your job does not complete in this time it will be killed.
      5. `-l mem=` will tell PBSpro how much ram is required per node default is in B, but you can use MB/GB
   2. Load the software that we'll need using the `module` system
   3. Move to the directory which contains the code we are running
   4. Run the python code and copy the stdout to a file
   5. Sleep for 120 to simulate a job that takes more than a few seconds to run
3. Submitted the job to the scheduler using `qsub`
4. Watched the progress of the job by running `qstat -u ${USER}` (a few times)
5. Inspected the outputs once the job completed by viewing `hello.txt`, `output.txt`, and `error.txt` (empty).

## Building a workflow
Once we know how to submit jobs we start thinking about all the jobs that we could run, and quickly we get into a state where we spend all our time writing jobs, submitting them to the queue, monitoring them, and then deciding which jobs need to be done next and submitting them.
This is time consuming and it's something we should get the computers to do for us.
If we think about the work that we need to do as discrete jobs, and then join multiple jobs together to form a workflow, then we can implement this workflow on an HPC using the scheduler system.

Below is a generic workflow with just three parts.

![WorkFlow]({{page.root}}{% link fig/SimpleFlow.png%})

The purple boxes represent work that needs to be done, and the arrows represent dependency of tasks.
You cannot process the data until you have retrieved the data, and you have to process the data *before* you do the cleanup.

In the above diagram we would say that there is a **dependency** between the tasks, as indicated by the arrows.
Slurm allows us to create these dependency links when we schedule jobs so that we don't have to sit around waiting for something to complete before submitting the next job.
When we schedule a job with `qsub` we can use the `-W depend` flag to indicate these links between our jobs.

> ## Dependency example
> Try the following in your directory.
> Remember to replace the `123456` with the actual job id that is returned to you
> ~~~
> [pjh562@gadi-login-04 pjh562]$ qsub scripts/first_script.sh 
> 77479068.gadi-pbs
> [pjh562@gadi-login-04 pjh562]$ qsub -W depend=afterok:77479068 scripts/second_script.sh 
> 77479087.gadi-pbs
> [pjh562@gadi-login-04 pjh562]$ qstat -u ${USER}
> ~~~
> {: .output}
> > ## Example output
> > ~~~
> > [pjh562@gadi-login-04 pjh562]$ qsub scripts/first_script.sh 
> > 77479068.gadi-pbs
> > [pjh562@gadi-login-04 pjh562]$ qsub -W depend=afterok:77479068 scripts/second_script.sh 
> > 77479087.gadi-pbs
> > [pjh562@gadi-login-04 pjh562]$ qstat -u ${USER}
> > Job ID               Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
> > -------------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
> > 77479068.gadi-pbs    pjh562   normal-* hello         --    1   1  200mb 00:05 Q   --
> > 77479087.gadi-pbs    pjh562   normal-* no_hello      --    1   1  200mb 00:05 H   --
> > 
> > ~~~
> >{: .output}
> {: .solution}
{: .challenge}

In the above example you'll see that the first job submitted was not running due to `Q`.
This means that the job in in the queue but that it is waiting for other jobs to complete before it can be run.
The second job, however, is not running due to `H`, and this is because it's on hold waiting for the first job to complete.

Again in the above example, we used the dependency criteria of `afterok`, but many more options are available:

- `after`: This job starts after the other job has begun or been canceled.
- `afterany`: This jobs starts after the other job has finished, regulardless of status.
- `afterok`: This job statrts after the other job has finished successfully.
- `afternotok`: This job starts after the other job has finished un-successfully (returned error, or was killed by the scheduler).

It is possible to list multiple dependencies by appending multiple job ids.
For example `afterok:123:124:125:153`

In the case of `afterok` if the named job fails, then this job will not be run - it will be deleted from the schedule.
Similarly with the `afternotok` - if the named job succeeded then this job will not be run.

By using the `afterok` and `afternotok` dependencies it is possible to set up a fork in your workflow, such that when a job fails, a cleanup job will run, but when the job succeeds the next part of your workflow will run.

> ## Plan a job
> Use the dependencies listed above to create the following workflow in SLURM:
> 1. Hold a meeting of criminals to plan a heist (3 criminals)
> 2. After the meeting and before the heist, all criminals go home and plan ways to back stab their colleagues 
> 3. Heist is enacted
> 4. If the heist is successful book flights to the cayman islands and retire
> 5. If the heist fails enact back-stabbing plans
> 
> > ## Possible solution
> > ~~~
> > > qsub meeting.sh
> > 100.gadi-pbs
> > > qsub -W depend=afterany:100 plan1.sh 
> > 101.gadi-pbs
> > > qsub -W depend=afterany:100 plan2.sh 
> > 102.gadi-pbs
> > > qsub -W depend=afterany:100 plan3.sh
> > 103.gadi-pbs
> > > qsub -W depend=afterany:101,102,103 heist.sh
> > 104.gadi-pbs
> > > qsub -W depend=afterok:104 retire.sh
> > 105.gadi-pbs
> > > qsub -W depend=afternotok:104 back-stab.sh
> > 106.gadi-pbs
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

### Parallel workflows
We will be discussing parallel computing in [another lesson]({{page.root}}{% link _episodes/ParallelComputing.md %}) in more depth.
As a prelude to that lesson lets consider a workflow which has a structure more like the following:

![DiamondWorkflow]({{page.root}}{% link fig/DiamondWorkflow.png %})

In this workflow we have a single job which fetches all the data that we need to process, and then multiple processing jobs which are independent of each other, followed by a cleanup job.
The dependency indicated by the arrows shows that the different processing jobs need to happen after the data retrieval and before the cleanup, but have no reliance on each other.
In this case we can set up the dependencies as follows:

1.  queue start job
2.  queue processing job1, depends on start job
3.  queue processing job2, depends on start job
4.  queue processing job3, depends on start job
5.  ...
6.  queue processing jobN, depends on start job
7.  queue cleanup job, depends on all of the processing jobs

In the above case it is highly likely that the processing jobs (1..N) will be copies of each other, with only a small change in the way that the processing is done.
For example: the start job can download a lot of data, and the individual processing jobs are processing the same data, but testing different models each time.
In this case the parameters of the models are all that is changing in the job files.
We could either set up a template system to make a copy of the template job, and then alter the parameters within, and submit them according to the above scheme, or we could get SLURM to do this work for us.

This brings us to the concept of **array jobs**.
In an array job we write a single script that is submitted to SLURM, but we tell it that we want multiple copies of this job to run.
Within the job we then identify the ID or job number, and use that to set up the parameters for the job.

TODO: link / advert the NextFlow workshop!

<!-- 
TODO FROM HERE
Let's explore this idea with a simple example.

We have a process that does some simulation based on initial parameters and we want to run this on various different inputs and collect the results in a summary file.
Our workflow is:
1. set up the parameters for each of the simulations
2. run the simulation on each set of parameters
3. collate all the results together in one file

The simulation that we want to run is computing the area and perimeter of a regular polygon (an N-gon) which is inscribed within the unit circle.
Our simulation is contained within the following python script:

> ## area_of_ngon.py 
> ~~~
> #! /usr/bin/env python
> 
> import argparse
> import math
> import sys
> 
> 
> def area_perimeter_ngon(n=3):
>   """
>   Compute the area and perimeter of a regular N-gon
>   inscribed within a cirlce of radius 1.
>   """
>   # Complain if n<3 because those shapes don't exist
>   if n<3:
>     raise AssertionError(f"Cannot compute area for ngon when n={n}")
>   r = 1 # Radius of our circle
>   perimeter = 2*n*r * math.sin(math.pi/n)
>   area = 0.5 * n * r**2 * math.sin(2*math.pi/n)
>   return area, perimeter
> 
> 
> if __name__ == "__main__":
>   parser = argparse.ArgumentParser()
>   parser.add_argument('n', default=None, type=int, help='Number of angles in our n-gon')
>   parser.add_argument('--out', dest='out', default='output.txt', type=str, help='output file')
>   options = parser.parse_args()
>   area, perimeter = area_perimeter_ngon(options.n)
>  
>   with open(options.out,'w') as f:
>     f.write(f'A {options.n}-gon inscribed within a unit circle has an area of {area:5.3f} and a perimeter of {perimeter:5.3f}\n')
> ~~~
> {: .language-python}
{: .callout}

Our script has been built in such a way that we can control it's behaviour using command line arguments:
`area_of_ngon.py --out 3-gon.txt 3`

Our setup script is:
> ## start.sh
> ~~~
> #! /usr/bin/env bash
> #
> #PBS --job-name=start
> #PBS --output=/fred/oz983/%u/start_%A_out.txt
> #PBS --error=/fred/oz983/%u/start_%A_err.txt
> #
> #PBS --ntasks=1
> #PBS --time=00:05:00
> #PBS --mem-per-cpu=1G
> 
> # move to the directory where the script/data are
> cd /fred/oz983/${USER}
> 
> #make a file
> touch input_data.txt
> 
> echo "doing some pre-processing work"
> 
> # put some data in
> for i in 3 4 5 6 7 8;
> do
>   echo ${i} >> input_data.txt
> done
> ~~~
> {: .language-bash}
{: .callout}

As you can see this start up script creates a file called `intput_data.txt` which contains the numbers 3..8.
Also note that we have use `%u` in the path for the output and error logs.
When we submit the job SLURM will replace `%u` with the username of the person submitting the job.
Similarly, we have use `%A` as part of the file name, and SLURM will replace this with the jobid.
The end result is that our error and ouput logs will look like:
`/fred/oz983/phancock/start_123456_out.txt`
and if we run our script multiple times, the log files wont get over written.

We then create a script that will read one of the lines from this file, and use it to run our python script.
This script is part of an array job.
We use `--array=start-end` to indicate that this is an array job and what job indicies we would like to use.

> ## branch.sh
> ~~~
> #! /usr/bin/env bash
> #
> #PBS --job-name=ngon
> #PBS --output=/fred/oz983/%u/ngon_%A-%a_out.txt
> #PBS --error=/fred/oz983/%u/ngon_%A-%a_err.txt
> #
> #PBS --ntasks=1
> #PBS --time=00:05:00
> #PBS --mem-per-cpu=1G
> #PBS --array=1-6
> 
> # load modules
> module load python/3.8.5
> 
> # move to the directory where the script/data are
> cd /fred/oz983/${USER}
> 
> data_file='input_data.txt'
> 
> # read the i-th line of the data file (where i is the array number)
> # and stor it as "n"
> n=$(sed -n ${SLURM_ARRAY_TASK_ID}p ${data_file})
> 
> echo "I'm array job number ${SLURM_ARRAY_TASK_ID}"
> echo "My n-gon number is ${n}"
> 
> python3 ../KLuken_HPC_workshop/area_of_ngon.py --out ${n}-gon.txt ${n}
> ~~~
> {: .language-bash}
{: .callout}

The script `branch.sh` is doing a few new things we should note:
- we use `%a` to use the array task id in the filename of the output (eg `ngon_123456-1_out.txt`). 
- we set `--array=1-6` to indicate that we want six jobs to run with task ids of 1,2,3,4,5 and 6.
- we read the environment variable `${SLURM_ARRA_TASK_ID}` to determine the task id
- we use sed to print the line from the data file corresponding to our task id and save it as `n`
- run our simulation script with parameter `${n}`

Finally our collect and clean up script looks like:

> ## collect.sh
> ~~~
> #! /usr/bin/env bash
> #
> #PBS --job-name=collect
> #PBS --output=/fred/oz983/%u/collect_%A_out.txt
> #PBS --error=/fred/oz983/%u/collect_%A_err.txt
> #
> #PBS --ntasks=1
> #PBS --time=00:05
> #PBS --mem-per-cpu=200
> 
> 
> # move to the directory where the script/data are
> cd /fred/oz983/${USER}
> 
> # list all the files that we will 'process'
> files=$(ls *gon.txt)
> 
> # this is where the 'proccessed' data will end up
> outfile=collected.txt
> 
> echo "collecting outputs from : ${files}"
> echo "results will be in: ${outfile}"
> 
> # delete the outfile before we write to it
> if [[ -e ${outfile} ]]; then rm ${outfile};fi
> 
> # do the 'processing' and write to the outfile
> for f in ${files}; do
>   cat ${f} >> ${outfile}
>   # delete the intermediate files to save space
>   rm ${f}
> done
> 
> 
> echo "Phew! Hard work complete..."
> ~~~
> {: .language-bash}
{: .callout}

There isn't much new in the collect script, except to note that we also delete the intermediate data files.

With all of the above in place we can then make our workflow run using the following three commands.

~~~
[phancock@farnarkle1 phancock]$ sbatch --begin=now+120 ../KLuken_HPC_workshop/start.sh
Submitted batch job 29442061
[phancock@farnarkle1 phancock]$ sbatch -d afterok:29442061 ../KLuken_HPC_workshop/branch.sh
Submitted batch job 29442065
[phancock@farnarkle1 phancock]$ sbatch -d afterok:29442065 ../KLuken_HPC_workshop/collect.sh
Submitted batch job 29442066
~~~
{: .output}

The `--begin=now+120` tells SLURM that we don't want the first job to start for another 2 minutes.
This is just gives us time to set up the dependencies before the job runs.

Note: when we set up the dependency for the collect script we just need to refer to the array job id and not all the individual tasks.
Slurm will automatically wait until all parts of a job have completed before resolving dependencies.

We can watch the jobs move through different stages of the queue as follows.
~~~
[phancock@farnarkle1 phancock]$ watch squeue -u ${USER}
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          29442061   skylake    start phancock PD       0:00      1 (BeginTime)
          29442066   skylake  collect phancock PD       0:00      1 (Dependency)
    29442065_[1-6]   skylake     ngon phancock PD       0:00      1 (Dependency)
# Start job is waiting to begin, others are waiting for dependency to be resolved

             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          29442061   skylake    start phancock CG       0:04      1 john31
          29442066   skylake  collect phancock PD       0:00      1 (Dependency)
    29442065_[1-6]   skylake     ngon phancock PD       0:00      1 (Dependency)
# start job is running, others are waiting on dependency

             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
        29442065_6   skylake     ngon phancock PD       0:00      1 (Priority)
        29442065_5   skylake     ngon phancock PD       0:00      1 (Priority)
        29442065_4   skylake     ngon phancock PD       0:00      1 (Priority)
        29442065_3   skylake     ngon phancock PD       0:00      1 (Priority)
        29442065_2   skylake     ngon phancock PD       0:00      1 (Priority)
          29442066   skylake  collect phancock PD       0:00      1 (Dependency)
        29442065_1   skylake     ngon phancock PD       0:00      1 (Priority)
# start job has completed, the ngon jobs are waiting in the queue ready to start
# the collect job is still waiting on dependencies to be resolved

             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          29442066   skylake  collect phancock PD       0:00      1 (Priority)
# all the ngon jobs are finished and now the collect job is waiting to start

             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
# all jobs now complete
~~~
{: .output}

We now have an understanding of how to run job on and HPC with SLURM, how to create a workflow, and monitor the status of our jobs.
The we will now focus on doing jobs that are a more than just printing things, and for this we'll need some of our own software. -->

## How do I install software on an HPC
As noted in a [previous lesson]({{page.root}}{% link _episodes/WhatIsHPC.md %}#software), the HPC facility administrators manage a lot of software.
For software that is provided by the HPC facility we can use the module system to load the required software/version.
In the previous exercises you saw this happen when we called `module load python3/3.8.5`.
We will explore the module system in more detail and then learn how to build and install our own software.

### The LMOD module system
The [LMOD](https://lmod.readthedocs.io/en/latest/) software is designed to allow users of an HPC facility to manage which software they are using at a given time.
When a user loads a module, the lmod system will set a bunch of different environment variables that are needed to run the particular software.
Additionally, additional modules (dependencies) will be loaded (or unloaded) to minimise version conflicts.

When we first log into OzSTAR we have a farily limited set of modules already loaded:
~~~
[phancock@farnarkle1 ~]$ module list

Currently Loaded Modules:
  1) nvidia/.latest (H,S)   2) slurm/.latest (H,S)
~~~
{: .output}

If we want to have access to a python interpreter we can try the following:
~~~
[phancock@farnarkle1 ~]$ module load python
Lmod has detected the following error:  Couldn't find module with name python, did you mean to load one of the following?
        * python/.3.6.4-numpy-1.14.1
        * python/3.6.4
        * python/.2.7.14-numpy-1.14.1
        * python/3.8.5
        * python/3.7.4
        * python/3.6.9
        * python/2.7.14
        * python/3.10.4 
~~~
{: .output}

As can be seen from the error message, there are multiple versions of python installed on this system, and none of them are set as the default version.
We need to specify the version that we want to load using `module load python/3.8.5`
Once we've done this we can see that python is now loaded along with a set of dependent libraries:
~~~
[phancock@farnarkle1 ~]$ module list

Currently Loaded Modules:
  1) nvidia/.latest (H,S)   3) gcccore/9.2.0     5) gcc/9.2.0     7) openmpi/4.0.2     9) sqlite/3.21.0  11) openssl/1.1.1g
  2) slurm/.latest  (H,S)   4) binutils/2.33.1   6) hwloc/2.0.3   8) imkl/2019.5.281  10) zlib/1.2.11    12) python/3.8.5
~~~
{: .output}

In loading python we've actually loaded **10** modules.
Thankfully we didn't have to track these dependencies down and load them ourselves!

If we want to see a list of all the modules that are available we can run `module avail`, but it is a very long and exhaustive list that is hard to browse.
Instead, if we want to search for a library or module we can use `module spider <name>`.

> ## Find some modules
> Use `module spider` to figure out what versions of the scipy python module are available.
> > ## answer
> > ~~~
> > [phancock@farnarkle1 ~]$ module spider scipy
> > 
> > ------------------------------------------------------------------------------------------------------------------------
> >   scipy:
> > ------------------------------------------------------------------------------------------------------------------------
> >     Description:
> >       SciPy is a collection of mathematical algorithms and convenience functions built on the Numpy extension for
> >       Python.
> > 
> >      Versions:
> >         scipy/1.0.0-python-2.7.14
> >         scipy/1.0.0-python-3.6.4
> >         scipy/1.0.1-python-3.6.4
> >         scipy/1.3.0-python-3.6.4
> >         scipy/1.4.1-python-3.7.4
> >         scipy/1.4.1-python-3.8.5
> >         scipy/1.6.0-python-3.7.4
> >         scipy/1.6.0-python-3.8.5
> >         scipy/1.8.0-python-3.10.4
> >      Other possible modules matches:
> >         scipy-bundle
> > 
> > ------------------------------------------------------------------------------------------------------------------------
> >   To find other possible module matches execute:
> > 
> >       $ module -r spider '.*scipy.*'
> > 
> > ------------------------------------------------------------------------------------------------------------------------
> >   For detailed information about a specific "scipy" module (including how to load the modules) use the module's full name.
> >   For example:
> > 
> >      $ module spider scipy/1.8.0-python-3.10.4
> > ------------------------------------------------------------------------------------------------------------------------
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

The `module spider` command will also match partial strings so if you use `module spider zip` it will show you all the modules with zip in the name.
Once you locate the module you want to use you'll need to include `module load program/version` in all of your job scripts before that program can be used.
If you end up in the not so nice situation where you need to run different versions of a program at different parts of your job you can use `module unload pogram/version` or `module swap old_program/version new_program/version` to change versions.
This is occasionally needed when the software you rely on was not written/built/installed by you.

TODO backlink to containers.