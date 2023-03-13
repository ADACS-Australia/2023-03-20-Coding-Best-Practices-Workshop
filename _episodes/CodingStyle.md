---
title: "Coding Style"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

## Best Practice - Coding Style

## Style Guides
```
Programs must be written for people to read, and only incidentally for machines to execute.
```
 ― Harold Abelson, Structure and Interpretation of Computer Program

A style guide is about consistency.
- Consistency with [a] style guide is important.
- Consistency within a project is more important.
- Consistency within one module or function is the most important.

[PEP8 style guide](https://peps.python.org/pep-0008/)

Why care?
- provides consistency
- makes code easier to read
- makes code easier to write
- makes it easier to collaborate	


TODO - linters

`pylint` will give you a summary of where your code doesn't conform to the PEP8 standard.

```
$ pylint poc.py
************* Module poc
poc.py:1:0: C0114: Missing module docstring (missing-module-docstring)
poc.py:8:0: W0622: Redefining built-in 'pow' (redefined-builtin)
poc.py:4:0: C0103: Constant name "ra" doesn't conform to UPPER_CASE naming style (invalid-name)
poc.py:5:0: C0103: Constant name "dec" doesn't conform to UPPER_CASE naming style (invalid-name)
poc.py:8:0: W0401: Wildcard import math (wildcard-import)
poc.py:8:0: C0413: Import "from math import *" should be placed at the top of the module (wrong-import-position)
poc.py:17:0: C0103: Constant name "nsrc" doesn't conform to UPPER_CASE naming style (invalid-name)
poc.py:20:0: W0401: Wildcard import random (wildcard-import)
poc.py:20:0: C0413: Import "from random import *" should be placed at the top of the module (wrong-import-position)
poc.py:29:4: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
poc.py:32:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
poc.py:29:4: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
poc.py:8:0: W0614: Unused import(s) acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cosh, degrees, dist, e, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, frexp, fsum, gamma, gcd, hypot, inf, isclose, isfinite, isinf, isnan, isqrt, ldexp, lgamma, log, log10, log1p, log2, modf, nan, perm, pow, prod, radians, remainder, sin, sinh, sqrt, tan, tanh, tau and trunc from wildcard import of math (unused-wildcard-import)
poc.py:20:0: W0614: Unused import(s) NV_MAGICCONST, TWOPI, LOG4, SG_MAGICCONST, BPF, RECIP_BPF, Random, SystemRandom, seed, random, triangular, randint, choice, randrange, sample, shuffle, choices, normalvariate, lognormvariate, expovariate, vonmisesvariate, gammavariate, gauss, betavariate, paretovariate, weibullvariate, getstate, setstate and getrandbits from wildcard import of random (unused-wildcard-import)

------------------------------------------------------------------
Your code has been rated at 2.63/10
```
{: .output}

Thats a fairly poor rating, but then again, the code isn't very well structured.
Each of the lines that have been identified come with an error code which you can get more information from pytlint:

```
pylint --list-msgs | less
```
{: .bash}
And then press `/` for search, and type the error code such as W0401.

## Structuring our code

Let's take a look at our proof of concept code and point out some of the things we are doing that make it hard for us to read, and might be causing problems in the future.
I've interspersed the code with comments that come from pylint:
```
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

```
{: .language-python}

Notice that `pylint` really doesn't like lines like `from math import *`.


TODO - more explainers for each line, and then how to fix it.



## Documentation and comments
Python allows / encourages documentation via docstrings.

Documentation is for people using the code (regular folks).
Documentation describes the ingredients and what kind of sausages are made.

Comments are for people reading the code (ie developers and future you).
Comments are about the sausage making process (ew!).


| Information           | Audience                                |
| --------------------- | --------------------------------------- |
| Comments              | Developers, people who read source code |
| Docstrings            | Developers, users                       |
| Wiki                  | Users, developers                       |
| mycode.readthedocs.io | Users                                   |


Consider creating a command line interface (CLI) for your code and providing an option of `--help` that gives users a quick into to the use of your code.

```
# TODO CLI example
```
{: .language-python}

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
Have a look on [pypi.org](https://pypi.org/) for packages of interest, or ask you colleagues, or [stack overflow](https://stackoverflow.com/).


> ## Use functions
> - Update POC to use two functions: one to generate the positions, and one to save them to a file
> - Have a very short "main" clause to run the code.
{: .challenge}
