---
title: "Functions, Classes, and OO (Oh My!)"
teaching: 15
exercises: 0
questions:
- "What is this 'object oriented' thing people talk about?"
- "When should I write or use classes?"
- "Should I feel bad about not writing classes?"
objectives:
- "Understand object oriented programming"
- "Be able to *use* classes"
- "Not feel bad for not writing classes"
keypoints:
- "You don't have to create your own classes if you don't want to"
- "Classes can be useful but they are not essential"
---

## Object Oriented (OO) programming
You may have heard that python is an object oriented programming language.
In python, everything that you work with is an object, though it's not always obviously so.

In programming languages, objects are a collection of data (attributes) with an associated set of functions (methods) that operate on these data.
In effect, an object is something that can store some kind of internal state.

When you work with python, any time you call function such as `message.upper()` you are calling the method `upper()` which is part of the `message` object.
Different types of objects can have methods with the same name, and they can behave in the the same or different ways.

If we want to create new object types then we create a `Class`, which is a description of how the object works, and then create new objects of this type using `variable = MyClass()`.
We can have multiple instances of the same class, each of which are individual objects.

## Functions in python
Python also allows us to create and use functions that are not attached to objects.
These would be functions like `int()` which would parse a string into an integer or `math.sqrt()` which would return the square root of a numeric value.

We have already created some of our own functions earlier in this workshop.

## Classes in python
The how/when/why of using classes in python is a long discussion.
Any program that you can write that uses classes can be written without using classes (and vice-versa).

This means that you can get by without ever creating your own classes in python, however there are a few instances where a small class can be a quick and easy fix:
- A data class that holds information about an entity, but doesn't define any functions.
  - e.g. a `Galaxy` class that attributes like 'redshift', 'ra', 'dec', 'name'
  - These are super easy to make with the [dataclass](https://docs.python.org/3/library/dataclasses.html) module / decorator
- A config class that holds a bunch of configuration settings for your code.
  - Passing a "config" object to a function is easier than setting 10+ arguments.
- A position class that is created with ra/dec coordinates but has functions that return the coords in different formats (though see [astropy.SkyCoord](https://docs.astropy.org/en/stable/api/astropy.coordinates.SkyCoord.html))


## Functional or OO programming?
Python allows us to work in an OO paradigm, but also in a functional or programmatic paradigm.
(In fact we are able to use a hybrid as well).
Note that PEP8 doesn't make any recommendation about which of these paradigms should be used!
(None of the PEP documents do to my knowledge).

Some people may feel that they are not "real programmers" because they don't use objects.
This is false for two reasons:
1. Everything in python is an object, so you are already 'using' objects,
2. Creating your own custom classes is not a requirement for writing good / effective code.

At the end of the day, the first and most important metric for your code is that "it works".
The way that you achieve this "work-y-ness" is up to you.

![Worst Code]({{page.root}}{% link fig/WorstCode.png %})

Ideally you will follow many of the best practices that we are covering in this workshop, but there will always be exceptions to the rule, reasons why you will deviate.
The choice of programming paradigm, language, or operating system are all for you to choose.
Some languages are more suited to particular tasks.
Not choosing a language because you don't have experience with it is a valid reason!



<!-- ## Data classes
One of the features of (and common complaints about) python is that it is not a strongly typed language.
This means that you are free to modify both the value and the type of a variable any time you like.
Moreover, it means that the python interpreter doesn't check the types of variables that are being passed to functions (or returned from them).
So in order for things to not fall apart we have to have some agreement between the code calling the function and the code within the function that is working with the passed parameters.
This is managed in part by having doc strings so that developers can indicate the expected types and intent for each of the parameters that are being passed.
You might think that there would be some internal checking of data types that come into a function before these data are being used, but this is uncommon, and against the ethos of python programming ([Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) and [Leap before you look](https://realpython.com/python-lbyl-vs-eafp/)).

One way to ensure that the data being passed to your function obeys some regular type/format constraints is to define a data class that has the required attributes and then use this type in your docstring.

For example, we could have a function that  -->