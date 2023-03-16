---
title: "Optimization"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

Optimize your total workflow:

Amdahl's Law: 
- System speed-up limited by the slowest component.

Paul’s rule of thumb: 
- You are the slowest component.

Therefore: 
1. Focus on reducing **your** active interaction time,
2. *then* on your total wait time, 
2. *then* on cpu time.

Avoid premature optimisation:
![ObligatoryXKCD](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

Verify that you **have** a problem before you spend resources **fixing** a problem.


> Premature optimization is the root of all evil
> 
> -- Donanld Knuth (in the context of software development)
{: .quote}

Good coding practices can lead to more performant code from the outset.
This is **not** wasted time.

You can't optimize to zero.
Working fast is good, but avoiding work is better.
Repeated computing is wasted computing.
[Check-pointing](https://hpc-unibe-ch.github.io/slurm/checkpointing.html) and [memoization](https://en.wikipedia.org/wiki/Memoization) are good for this.

Embrace sticky tape solutions:
- Build on existing solutions
- Use your code to move between solutions (eg BASH / Python)
- Only write new code where none exists
- Choose a language/framework that suits the problem
- Optimize only when there is a problem 