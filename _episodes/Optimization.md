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


## leveraging the work of others
There are a lot of python packages that are designed, directly or indirectly, to provide optimized python code.
For example:
- [Numpy](https://numpy.org/)
  - The fundamental package for scientific computing with Python
- [Scipy](https://scipy.org/)
  - Fundamental algorithms for scientific computing in Python
  - extends upon Numpy to provide additional data structures and algorithms
- [Numba](https://numba.pydata.org/)
  - an open source JIT compiler that translates a *subset* of Python and NumPy code into fast machine code.
- [Dask](https://www.dask.org/)
  - library for parallel computing in Python, with a focus on workflows and big data processing
- [Taichi](https://www.taichi-lang.org/)
  - a domain-specific language embedded in Python that helps you easily write portable, high-performance parallel programs
- [Cython](https://cython.org/)
  - an optimising static compiler for both the Python programming language and the extended Cython programming language
  - write python code, convert it to c, compile, and run
- [PyPy](https://www.pypy.org/)
  - A fast, compliant alternative implementation of Python
  - Not python modules will work in pypy, but many of the main one will
- [pandas](https://pandas.pydata.org/)
  - a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

These packages can provide significant performance increases, often by implementing parallel processing under the hood, without you having to write or manage any of the parallel computing components.