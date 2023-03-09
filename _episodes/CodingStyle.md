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
<!-- See https://docs.google.com/presentation/d/11fOcEBwyAwUchFocbTopph9k3IPeTirCe04HJC8lXkM/edit#slide=id.g5ad883c8fc_0_0 -->

## Naming conventions
Consistent and meaningful naming of files and folders can make everyone’s life easier. 
For example to represent Date Location Sensor a general naming convention could be:
`YYYYMMDD_SiteA_SensorB.CSV`

Some characters may have special meaning to the operating system so avoid using these characters when you are naming files.
These characters include the following: `/ \ " ' * ; - ? [ ] ( ) ~ ! $ { } &lt > # @ & |` space tab newline

Using a date format of `YYYYMMDD` will have the added bonus that files sorted alphabetically will be also sorted by date.
Similarly, you should consider zero-padding your integers in file names so that `File.v12.txt`, comes after `File.v02.txt`, rather than before `File.v2.txt`.


Within your code:
Use words! Be verbose but not needlessly so.
- nouns for classes and variables 
  - CamelCaseForClasses
- verbs for functions 
  - Underscores_for_functions
- ALL_CAPS_FOR_STATIC_VARIABLES
- _private_function_or_variable (not part of a public API)

Loop iterators are commonly just `i, j, k` which is not very descriptive, but in many cases this can be appropriate.
[For example, when you are using `i,j,k` as array indexes.]


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


## Python idioms

Avoid `import *` like the plague.
Use `from math import sqrt` or, even better, `import math` and then `math.sqrt` as required.

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


## Test your code
```
Finding your bug is a process of confirming the many things that you believe are true — until you find one which is not true.
```
— Norm Matloff

The only thing that people write less than documentation is test code.

Pro-tip: Both documentation and test code is easier to write if you do it as part of the development process.

Ideally:
1. Write function definition and basic docstring
2. Write function contents
3. Write test to ensure that function does what the docstring claims.
4. Update code and/or docstring until (3) is true.

Exhaustive testing is rarely required or useful.
Two main philosophies are recommended:
1. Tests for correctness (eg, compare to known solutions)
2. Tests to avoid re-introducing a bug (regression tests)
