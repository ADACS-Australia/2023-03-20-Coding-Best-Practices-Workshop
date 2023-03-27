---
title: "Testing"
teaching: 20
exercises: 20
questions:
- "Why should I write tests?"
- "How do I write tests?"
objectives:
- "Be able to write tests"
- "Be able to run tests with pytest"
keypoints:
- "Testing reduces the number of bugs"
- "If you don't test it, it might be broken"
- "Testing is about having your code live up to it's *intended* use"
---

## Test your code
> Finding your bug is a process of confirming the many things that you believe are true — until you find one which is not true.
> 
> — Norm Matloff

The only thing that people write less than documentation is test code.

> ## Pro-tip
> Both documentation and test code is easier to write if you do it as part of the development process.
{: .callout}

Ideally:
1. Write function definition and basic docstring
2. Write function contents
3. Write test to ensure that function does what the docstring claims.
4. Update code and/or docstring until (3) is true.

Exhaustive testing is rarely required or useful.
Two main philosophies are recommended:
1. Tests for correctness (eg, compare to known solutions)
2. Tests to avoid re-introducing a bug (regression tests)



In our `sky_sim` project we have a function called `get_radec` which accepts no arguments.
Let's try writing a test for this function.
The *desired* behavior of the function can be summarized as:
~~~
get_radec() = (14.215420962967535, 41.26916666666666)
~~~
{: .language-python}


## How to write and run tests

Depending on how you will run your test harness you will write tests in different ways.
For this workshop we'll focus on `pytest` ([docs](https://docs.pytest.org/en/6.2.x/)) as it is both a great starting point for beginners, and also a very capable testing tool for advanced users.

`pytest` can be installed via pip:
~~~
pip install pytest
~~~
{: .language-bash}

In order to use `pytest` we need to structure our test code in a particular way.
Firstly we need a directory called `tests` which contain test modules named as `test_<item>.py` which in turn have functions called `test_<thing>`.
The functions themselves need to do one of two things:
- return `None` if the test was successful
- raise an exception if the test failed

Here is an example test.
It would live in the file `test_module.py`, and simply tries to import our code:
~~~
def test_module_import():
    try:
        import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return
~~~
{: .language-python}

With pytest installed we simply navigate to our package directory and run `pytest`:
~~~
============================ test session starts ============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /data/alpha/hancock/ADACS/2023-03-20-Coding-Best-Practices-Workshop/code/examples
plugins: cov-2.12.1, anyio-3.3.0
collected 1 tem                       

test_module.py .                                                       [100%]

============================= 1 passed in 0.01s =============================
~~~
{: .output}

`pytest` will automatically look for directories/files/functions of the required format and run them.

If you decide that a test is no longer needed (or not valid, or still in development), you can turn it off by changing the name so that it doesn't start with test.
I like to change `test_thing` so that it becomes `dont_test_thing`.
This way you can keep the test code, but it just wont run.

> ## Bonus note
> Eventually the number of tests that you create will be large and take a while to run.
> In order that you can test individual sections of your code base the following python-fu may be useful:
> ~~~
> if __name__ == "__main__":
>     # introspect and run all the functions starting with 'test'
>     for f in dir():
>         if f.startswith('test_'):
>             print(f)
>             globals()[f]()
> ~~~
> {: .language-python}
> with the above you can run all the tests within a file just by running that file.
{: .callout}

### More detailed testing
Let's now work with some more meaningful tests for the `sky_sim.py` that we have been working with.
In particular let's test the `get_radec()` and `make_stars()` functions.

To do this we nee to know how to work with exceptions.
In python we can use the keyword `raise` to send an exception up the call stack where it will eventually be caught in a `try/except` clause (or by the python interpreter itself).
For our testing purposes we need to raise a particular type of exception called an `AssertionError`.
The syntax is:

~~~
def test_that_a_thing_works():
    # do things
    if not thing_works:
        raise AssertionError("Description of what failed")
    return
~~~
{: .language-python}

We can have multiple exit points in our function, corresponding to the various ways that a test might fail (each with a useful message).


> ## get_radec() testing
> Recall that the function should obey the following:
> ~~~
> get_radec() = (14.215420962967535, 41.26916666666667)
> ~~~
> {: .language-python}
>
> Create a test for the above function that will raise an exception when the returned ra/dec are not correct.
> 
> > ## initial function
> > ~~~
> > def get_radec():
> >     """
> >     Generate the ra/dec coordinates of Andromeda
> >     in decimal degrees.
> > 
> >     Returns
> >     -------
> >     ra : float
> >         The RA, in degrees, for Andromeda
> >     dec : float
> >         The DEC, in degrees for Andromeda
> >     """
> >     # from wikipedia
> >     andromeda_ra = '00:42:44.3'
> >     andromeda_dec = '41:16:09'
> > 
> >     d, m, s = andromeda_dec.split(':')
> >     dec = int(d)+int(m)/60+float(s)/3600
> > 
> >     h, m, s = andromeda_ra.split(':')
> >     ra = 15*(int(h)+int(m)/60+float(s)/3600)
> >     ra = ra/math.cos(dec*math.pi/180)
> >     return ra,dec
> > ~~~
> > {: .language-python}
> {: .solution}
> 
{: .challenge}

> ## testing make_stars()
> Read the docstring for the make_stars function below and come up with at least 2 tests that you can run.
> 
> > ## initial function
> > ~~~
> > def make_stars(ra, dec, nsrc=NSRC):
> >     """
> >     Generate NSRC stars within 1 degree of the given ra/dec
> > 
> >     Parameters
> >     ----------
> >     ra,dec : float
> >         The ra and dec in degrees for the central location.
> >     nsrc : int
> >         The number of star locations to generate
> >     
> >     Returns
> >     -------
> >     ras, decs : list
> >         A list of ra and dec coordinates.
> >     """
> >     ras = []
> >     decs = []
> >     for _ in range(nsrc):
> >         ras.append(ra + random.uniform(-1,1))
> >         decs.append(dec + random.uniform(-1,1))
> >     return ras, decs
> > ~~~
> > {: .language-python}
> {: .solution}
> How do you deal with the fact that the positions that are generated are random and thus different each time you run them?
>
{: .challenge}

When you are writing tests, you can test multiple things in a single function (pytest will consider this just one test).
The drawback is that if the first test fails, the function will exit and the other tests don't run.
However, some tests will require that you do a fair bit of setup to create objects with a particular internal state, and that doing this multiple times can be time consuming.
In this case you are probably better off doing the set up once and have multiple small tests bundled up into one function.

There are many modules available which can help you with different kinds of testing.
Of particular note for scientific computing is [numpy.testing](https://numpy.org/doc/stable/reference/routines.testing.html).
`numpy.testing` has lots of convenience functions for testing related to numpy data types.
Especially useful when you want things to be "close" or "equal to with a given precision".

## Testing modes

Broadly speaking there are two classes of testing: functional and non-functional.

| Testing type            | Goal                                                                                               | Automated? |
| ----------------------- | -------------------------------------------------------------------------------------------------- | ---------- |
| Functional testing      |                                                                                                    |            |
| - Unit testing          | Ensure individual function/class works as intended                                                 | yes        |
| - Integration testing   | Ensure that functions/classes can work together                                                    | yes        |
| - System testing        | End-to-end test of a software package                                                              | partly     |
| - Acceptance testing    | Ensure that software meets business goals                                                          | no         |
| Non-functional testing  |                                                                                                    |            |
| - Performance testing   | Test of speed/capacity/throughput of the software in a range of use cases                          | yes        |
| - Security testing      | Identify loopholes or security risks in the software                                               | partly     |
| - Usability testing     | Ensure the user experience is to standard                                                          | no         |
| - Compatibility testing | Ensure the software works on a range of platforms or with different version of dependent libraries | yes        |

The different testing methods are conducted by different people and have different aims.
Not all of the testing can be automated, and not all of it is relevant to all software packages.
As someone who is developing code for personal use, use within a research group, or use within the astronomical community the following test modalities are relevant.

### Unit testing
In this mode each function/class is tested independently with a set of known input/output/behavior.
The goal here is to explore the desired behavior, capture edge cases, and ideally test every line of code within a function.
Unit testing can be easily automated, and because the desired behaviors of a function are often known ahead of time, unit tests can be written *before* the code even exists.

### Integration testing
Integration testing is a level above unit testing.
Integration testing is where you test that functions/classes interact with each other as documented/desired. 
It is possible for code to pass unit testing but to fail integration testing.
For example the individual functions may work properly, but the format or order in which data are passed/returned may be different.
Integration tests can be automated.
If the software development plan is detailed enough then integration tests can be written before the code exists.

### System testing
System testing is Integration testing, but with integration over the full software stack.
If software has a command line interface then system testing can be run as a sequence of bash commands.

### Performance testing
Performance testing is an extension of benchmarking and profiling which we'll talk about [later]({{page.root}}{% link _episodes/BenchmarkingAndProfiling.md %}).
During a performance test, the software is run and profiled and passing the test means meeting some predefined criteria.
These criteria can be set in terms of:
- peak or average RAM use
- (temporary) I/O usage
- execution time
- cpu/gpu utilization

Performance testing can be automated, but the target architecture needs to be well specified in order to make useful comparisons.
Whilst unit/integration/system testing typically aims to cover all aspects of a software package, performance testing may only be required for some subset of the software.
For software that will have a long execution time on production/typical data, testing can be time-consuming and therefore it is often best to have a smaller data set which can be run in a shorter amount of time as a pre-amble to the longer running test case.

### Compatibility testing
Compatibility testing is all about ensuring that the software will run in a number of target environments or on a set of target infrastructure.
Examples could be that the software should run on:
- Python 3.6,3.7,3.8
- OSX, Windows, and Linux
- Pawsey, NCI, and OzStar
- Azure, AWS, and Google Cloud
- iPhone and Android 

Compatibility testing requires testing environments that provide the given combination of software/hardware.
Compatibility testing typically makes a lot of use of containers to test different environments or operating systems.
Supporting a diverse range of systems can add a large overhead to the development/test cycle of a software project.

## Developing tests
Ultimately tests are put in place to ensure that the actual and desired operation of your software are in agreement.
The actual operation of the software is encoded in the software itself.
The *desired* operation of the software should also be recorded for reference and the best place to do this is in the user/developer documentation (see [below](#Documentation)).

One strategy for developing test code is to write tests for each bug or failure mode that is identified.
In this strategy, when a bug is identified, the first course of action is to develop a test case that will expose the bug.
Once the test is in place, the code is altered until the test passes.
This strategy can be very useful for preventing bugs from reoccurring, or at least identifying them when they do reoccur so that they don't make their way into production.

## Test metrics
As well has having all your tests pass when run, another consideration is the fraction of code which is actually tested.
A basic measure of this is called the *testing coverage*, which is the fraction of lines of code being executed during the test run.
Code that isn't tested can't be validated, so the coverage metric helps you to find parts of your code that are not being run during the test.

> ## Example coverage
> Run `pytest --cov=sky_sim --cov-report=term ./test_module.py` to see the coverage report for this test/module.
> > ## result
> > ~~~
> > pytest --cov=sky_sim --cov-report=term ./test_module.py 
> > ================================================================ test session starts ================================================================
> > platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
> > rootdir: /data/alpha/hancock/ADACS/2023-03-20-Coding-Best-Practices-Workshop/code/examples
> > plugins: cov-2.12.1, anyio-3.3.0
> > collected 2 items                                                                                                                                   
> > 
> > test_module.py ..                                                                                                                             [100%]
> > 
> > ---------- coverage: platform linux, python 3.8.10-final-0 -----------
> > Name         Stmts   Miss  Cover
> > --------------------------------
> > sky_sim.py      37     21    43%
> > --------------------------------
> > TOTAL           37     21    43%
> > 
> > 
> > ================================================================= 2 passed in 0.04s =================================================================
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

In the above example I have only 43% coverage, which means that only 43% of the lines in the `sky_sim.py` file were executed during my testing.
Achieving 100% coverage is a fun goal, but usually only achievable for the simplest codes.
Even with 100% code coverage, there is no guarantee that you have zero bugs in your code.

We can have a better look at the coverage report by writing an html formatted report:
~~~
python -m pytest --cov=mymodule --cov-report html:coverage tests/test_module.py
~~~
{: .language-bash}
This will give use a report for each file in the directory `coverage`.
Let's open up the file `sky_sim_py.html`, and see what statements were hit/missed during the testing.

Note in particular that anything in the `if __name__ == "__main__"` clause will not be tested because it is only run when the file is called directly, not when it is imported as a module.
How could we write tests that would test our CLI?

## Automated testing
We have already learned about the `pytest` package that will run all our tests and summarize the results.
This is one form of automation, but it relies on the user/developer remembering to run the tests after altering the code.
Another form of automation is to have a dedicated workflow that will detect code changes, run the tests, and then report the results.
GitHub (and GitLab) have continuous integration (CI) tools that you can make use of to run a suite of tests every time you push a new commit, or make a pull request.