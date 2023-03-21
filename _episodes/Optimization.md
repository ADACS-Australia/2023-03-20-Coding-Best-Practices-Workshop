---
title: "Optimization"
teaching: 15
exercises: 15
questions:
- "How can I optimize my code?"
- "What am I even optimizing for?"
objectives:
- "Review the different resources we can optimize for"
- "Understand the optimization loop"
- "Make our example code run at least a little faster"
keypoints:
- "After a while you'll remember some of these optimization things and do them by default (esp, NumPy things)"
- "Without profiling you are just guessing at what the problems is"
- "Know when to stop"
---


## Scope your optimization work
When we are engaged in optimization there are a few things we should do first:
- Understand what the problem is
- Measure the current state of things (benchmark + first profile)
- Have a target in mind for what is "good enough"

When thinking about the problem, remember that your code doesn't run in isolation.
It runs as part of a larger workflow, that includes other pieces of code as well as non-automated things like researcher thinking time.
Consider your entire workflow, and how much time is spent on waiting for code to run vs you analyzing results.
If you have other useful work that can be done while your code runs, then do that, it'll be time well spent.

**Amdahl's Law**: 
- System speed-up limited by the slowest component.

**Paul’s rule of thumb**: 
- You are the slowest component.

**Therefore**: 
1. Focus on reducing **your** active interaction time,
2. *then* on your total wait time, 
3. *then* on cpu time.

In [parallel computing]({{page.root}}{% link _episodes/ParallelComputing.md %}) we'll explore ways of making your work complete sooner, without making it run faster!
Another way of making your code run faster can be to just buy a faster computer, though this isn't always an option for everyone).

A reason to confirm that we *need* to optimize our code is that we want to avoid premature optimization:
![ObligatoryXKCD](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)


Good coding practices can lead to more performant code from the outset.
This is **not** wasted time.

Remember also that you cannot can't optimize to zero.
There will always be a minimum amount of time that your work will take to do, and you will only ever approach this minimum asymptotically.
At first you'll get 2-3 or even 10x speed increases for moderate effort, but as you keep going, you'll end up spending a day writing unreadable code just for that 0.1% gain.
Don't be a speed addict, know when to quit!


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

optimization -> profile, idea, implement, profile, better?

show openAI integration magics

options:
- scalene (entire codebase)
- jupyter magics for snippets. %timit (also in ipython)

~~~
In [2]: import numpy as np

In [3]: %timeit np.ones(100)
1.76 µs ± 43.3 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [4]: %timeit np.empty(100)
222 ns ± 9.64 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
~~~
{: .language-python}

note: beware of scaling, do bigger tests