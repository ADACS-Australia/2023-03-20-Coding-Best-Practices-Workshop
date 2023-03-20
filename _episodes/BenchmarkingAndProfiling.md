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

TODO just read the pbs output file!


## Profiling

We'll be using the [scalene](https://pypi.org/project/scalene/) package to profile our python code.
Unlike other profiling systems, scalene doesn't require you to edit the source code as part of the profiling process.
Instead you simply run `scalene your_prog.py` and it will run your code and deliver a report.