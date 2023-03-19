---
title: "Coding Style"
teaching: 40
exercises: 20
questions:
- "Is my personal coding style ok?"
- "Should I try to change my style?"
- "Do I even have a style?"
objectives:
- "Understand the importance of consistency"
- "Be able to write code that you can understand in 6mo"
- "Use some tools and guides that help with coding style"
keypoints:
- "Python is *very* forgiving"
- "Make your code as easy to understand as possible for humans"
---

## Best Practice - Coding Style
>
> Programs must be written for people to read, and only incidentally for machines to execute.
>
> ― Harold Abelson, Structure and Interpretation of Computer Program
{: .quote}

A style guide is about consistency.
- Consistency with [a] style guide is important.
- Consistency within a project is more important.
- Consistency within one module or function is the most important.

Having code with inconsistent coding style makes it hard for humans to focus on how and what the code is doing.
In particular, when (not if) you come back to debug or further develop your code, you'll have forgotten the details of what was done.
For this reason you should write code in as easy to understand way as possible.


Why care about style?
- provides consistency
- makes code easier to read
- makes code easier to write
- makes it easier to collaborate


Have you tried to read Shakespeare?
How much of a mental load was it to try and understand the characters and stories simply because the language was so different from our every day?
Now imagine that you 'get in the groove' with his style, and now have to start reading works by another author who as a different (but still strange) language choice.
You have to spend a significant amount of effort learning the new style before you can even analyze the themes of their work!

Do yourself a favour and be clear, consistent, and concise, whenever possible.
Even better, have a look at how other people code, and learn from their best practices.
[PEP8 style guide](https://peps.python.org/pep-0008/) is essentially a summary of these practices as relating to coding style.
	
Because programmers will automate anything they can, there are a programs written to analyse the style of your code, and point out where you deviate from a given style guide.
For example, `pylint` will give you a summary of where your code doesn't conform to the PEP8 standard.

If we apply `pylint` to our proof of concept code we'll get a bunch of notices:
~~~
$ pylint sky_sim.py
************* Module poc
sky_sim.py:1:0: C0114: Missing module docstring (missing-module-docstring)
sky_sim.py:8:0: W0622: Redefining built-in 'pow' (redefined-builtin)
sky_sim.py:4:0: C0103: Constant name "ra" doesn't conform to UPPER_CASE naming style (invalid-name)
sky_sim.py:5:0: C0103: Constant name "dec" doesn't conform to UPPER_CASE naming style (invalid-name)
sky_sim.py:8:0: W0401: Wildcard import math (wildcard-import)
sky_sim.py:8:0: C0413: Import "from math import *" should be placed at the top of the module (wrong-import-position)
sky_sim.py:17:0: C0103: Constant name "nsrc" doesn't conform to UPPER_CASE naming style (invalid-name)
sky_sim.py:20:0: W0401: Wildcard import random (wildcard-import)
sky_sim.py:20:0: C0413: Import "from random import *" should be placed at the top of the module (wrong-import-position)
sky_sim.py:29:4: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
sky_sim.py:32:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
sky_sim.py:29:4: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
sky_sim.py:8:0: W0614: Unused import(s) acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cosh, degrees, dist, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp, fsum, gamma, gcd, hypot, inf, isclose, isfinite, isinf, isnan, isqrt, ldexp, lgamma, log, log10, log1p, log2, modf, nan, perm, pow, prod, radians, remainder, sin, sinh, sqrt, tan, tanh, tau and trunc from wildcard import of math (unused-wildcard-import)
sky_sim.py:20:0: W0614: Unused import(s) NV_MAGICCONST, TWOPI, LOG4, SG_MAGICCONST, BPF, RECIP_BPF, Random, SystemRandom, seed, random, triangular, randint, choice, randrange, sample, shuffle, choices, normalvariate, lognormvariate, expovariate, vonmisesvariate, gammavariate, gauss, betavariate, paretovariate, weibullvariate, getstate, setstate and getrandbits from wildcard import of random (unused-wildcard-import)

------------------------------------------------------------------
Your code has been rated at 2.63/10
~~~
{: .output}

Thats a fairly poor rating, but then again, the code isn't very well structured, mostly because our main goal was making things work.
Each of the lines that have been identified come with an error code which you can get more information from `pytlint`:

> ## Look up an message number
> Run the following from your command line
> ~~~
> pylint --list-msgs | less
> ~~~
> {: .bash}
> and then press `/` for search, and type the error code such as W0401.
>
{: .challenge}


## Structuring and styling our code

Let's take a look at our proof of concept code and point out some of the things we are doing that make it hard for us to read, and might be causing problems in the future.
I've interspersed the code with comments that come from pylint:
~~~
# Determine Andromeda location in ra/dec degrees 
# ^- Missing module docstring (missing-module-docstring)

# from wikipedia
ra = '00:42:44.3' 
# ^- Constant name "ra" doesn't conform to UPPER_CASE naming style (invalid-name)
dec = '41:16:09'  
# ^- Constant name "dec" doesn't conform to UPPER_CASE naming style (invalid-name)

# convert to decimal degrees
from math import *  
# ^- Redefining built-in 'pow' (redefined-builtin)
# ^- Wildcard import math (wildcard-import)
# ^- Import "from math import *" should be placed at the top of the module (wrong-import-position)
# ^- W0614: Unused import(s) acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cosh, degrees, dist, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp, fsum, gamma, gcd, hypot, inf, isclose, isfinite, isinf, isnan, isqrt, ldexp, lgamma, log, log10, log1p, log2, modf, nan, perm, pow, prod, radians, remainder, sin, sinh, sqrt, tan, tanh, tau and trunc from wildcard import of math (unused-wildcard-import)

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

nsrc = 1_000_000
# ^- Constant name "nsrc" doesn't conform to UPPER_CASE naming style (invalid-name)

# make 1000 stars within 1 degree of Andromeda
from random import *
# ^- Wildcard import math (wildcard-import)
# ^- Import "from math import *" should be placed at the top of the module (wrong-import-position)
# ^- Unused import(s) NV_MAGICCONST, TWOPI, LOG4, SG_MAGICCONST, BPF, RECIP_BPF, Random, SystemRandom, seed, random, triangular, randint, choice, randrange, sample, shuffle, choices, normalvariate, lognormvariate, expovariate, vonmisesvariate, gammavariate, gauss, betavariate, paretovariate, weibullvariate, getstate, setstate and getrandbits from wildcard import of random (unused-wildcard-import)

ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
# ^- Using open without explicitly specifying an encoding (unspecified-encoding)
# ^- Consider using 'with' for resource-allocating operations (consider-using-with)

print("id,ra,dec", file=f)
for i in range(nsrc):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
    # ^- Formatting a regular string which could be a f-string (consider-using-f-string)

~~~
{: .language-python}

Notice that `pylint` *really* doesn't like lines like `from math import *`.

> ## "fixing" our code
> Pick a line of code which has been shamed and suggest an alternative.
>
> Make your suggestion in the [etherpad]({{site.ether_pad}})
> 
> Note that sometimes you have to break the style guide in order to achieve our ultimate goal of **being clear**.
> 
> `git commit` with a useful message each time you make a meaningful change
{: .discussion}

> ## auto-formatters
> There are also auto formatting tools that will do most of the style rewriting for you.
>
> In our discussion of [IDEs]({{page.root}}{% link _episodes/IDEs.md %}) we'll touch on this again.
> 
{: .callout}

## DRY coding principle

Don't Repeat Yourself (DRY), means not having (near) identical blocks of code throughout your program.
Repeated code means repeated bugs, multiple places for the one bug to occur.
If you need to do the same thing more than once, then write a function and call it.
If there is a bug in the code then at least it's only in one place!

Next level, is to not repeat yourself across multiple projects.
This means writing your code as class/functions and then `import`ing that code when you need it.
Next level is to provide a package/module with all these helpful bits of code.

Related to DRY is the DRO principle of Don't Repeat Others, or simply don't re-invent the wheel.
There is a lot of already existing code available that will probably do most of what you need.
Instead of remaking a solution from scratch (and having to test/debug/maintain it) you should just `pip install` the package that does what you need.
Have a look on [pypi.org](https://pypi.org/) for packages of interest, or ask your colleagues, or [stack overflow](https://stackoverflow.com/).

### Structuring code

At a high level python files should have the following content / order:
- a `#!` line like `#! /usr/bin/env python` on the first line
- a docstring for this module (if it's a module, see [later]({{page.root}}{% link _episodes/Documentation.md %}))
- `import` all the modules/clasess/functions that you need (and no more)
- global (static) variables
- define classes
- define functions
- a `main()` function if you use one
- an `if __name__` clause if you want one

Notice that the above leaves almost no code in the global scope.
This is a good thing, it helps us keep our different parts of code from interfering with each other.
If we reuse variable names and forget to set/reset the value of that variable then we get bugs, by keeping our code within functions and classes then we can avoid this common source of bugs.

Let's revisit our proof of concept code and apply the above structure.

> ## Use functions
> - Update POC to use two functions: one to generate the positions, and one to save them to a file
> - Have a very short "main" clause to run the code.
> - `git commit` with a useful message when you are done
{: .challenge}
