---
title: "Testing"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
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
It would live in the file `test_module.py, and simply tries to import our code:
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
>         if f.startswith('test'):
>             print(f)
>             globals()[f]()
> ~~~
> {: .language-python}
> with the above you can run all the tests within a file just by running that file.
{: .callout}

TODO - From here on

> ## Challenge write a test
> - Create a file `tests/test_default` and within it a function `test_hard_compute`.
> - Use the desired behavior listed [above](#testing-code) as the three test cases
> - `test_hard_compute` should return `None` if all cases passed
> - `test_hard_compute` should raise an `AssertionError` with a sensible note if a test fails
> 
> If you include the code from the bonus not [above](#bonus-note) you can quickly run just this test.
> 
> When you have a test that you are happy with run it using `pytest`
> >## Solution
> > ~~~
> > def test_hard_compute():
> >     from mymodule.default import hard_compute
> > 
> >     answer = hard_compute(1, 'help')
> >     expected = 1
> >     if answer != expected:
> >         raise AssertionError(f"hard_compute(1,'help') should return {expected} but 
> >                                returned {answer}")
> > 
> >     answer = hard_compute(1, 'test', 7)
> >     expected = "test.7"
> >     if answer != expected:
> >         raise AssertionError(f"hard_compute(1,'test', 7) should return {expected} but 
> >                                returned {answer}")
> > 
> >     answer = hard_compute(None,'hello')
> >     expected = -1
> >     if answer != expected: # "is" instead of "==" since expected is None
> >         raise AssertionError(f"hard_compute(None,'hello') should return {expected} 
> >                                but returned {answer}")
> > 
> >     return
> > 
> > if __name__ == "__main__":
> >     # introspect and run all the functions starting with 'test'
> >     for f in dir():
> >         if f.startswith('test'):
> >             print(f)
> >             globals()[f]()
> > ~~~
> > {: .language-python}
> {: .solution}
> If your test code works as intended you should get the following output from `pytest`
> ~~~
> ============================================================= short test summary info > =============================================================
> FAILED tests/test_default.py::test_hard_compute - AssertionError: hard_compute(None,> 'hello') should return -1 but returned None
> =========================================================== 1 failed, 1 passed in 0.> 11s ===========================================================
> ~~~
> {: .output}
{: .challenge}

The fact that the failed tests are reported individually, and the assertion errors are reported for each failure, should be an encouragement to write useful things as your error messages.

Note that in the above we ran all three tests in the same function.
If the first test failed, then the second two are not run.
If the subsequent tests are dependent on the success of the first then this is a good design technique.
However, if the tests are independent then it might be a good idea to split the tests into individual functions.

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
Performance testing is an extension of benchmarking and profiling.
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
The *desired* operation of the software should also be recorded for reference and the best place to do this is in the user/developer documenation (see [below](#Documentation)).

One strategy for developing test code is to write tests for each bug or failure mode that is identified.
In this strategy, when a bug is identified, the first course of action is to develop a test case that will expose the bug.
Once the test is in place, the code is altered until the test passes.
This strategy can be very useful for preventing bugs from reoccurring, or at least identifying them when they do reoccur so that they don't make their way into production.

## Test metrics
As well has having all your tests pass when run, another consideration is the fraction of code which is actually tested.
A basic measure of this is called the *testing coverage*, which is the fraction of lines of code being executed during the test run.
Code that isn't tested can't be validated, so the coverage metric helps you to find parts of your code that are not being run during the test.

> ## Example coverage
> Run `python -m pytest --cov=mymodule  --cov-report=term tests/test_module.py`
> to see the coverage report for this test/module.
> > ## result
> > ~~~
> > python -m pytest --cov=mymodule --cov-report=term tests/test_module.py 
> > ================================================================ test session starts =================================================================
> > platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
> > rootdir: /data/alpha/hancock/ADACS/MAP21A-JCarlin-ExampleCodes
> > plugins: cov-2.12.1, anyio-3.3.0
> > collected 1 item                                                                                                                                     
> > 
> > tests/test_module.py .                                                                                                                         [100%]
> > 
> > ---------- coverage: platform linux, python 3.8.10-final-0 -----------
> > Name                   Stmts   Miss  Cover
> > ------------------------------------------
> > mymodule/__init__.py       6      2    67%
> > mymodule/default.py       17     17     0%
> > mymodule/other.py          0      0   100%
> > ------------------------------------------
> > TOTAL                     23     19    17%
> > 
> > 
> > ================================================================= 1 passed in 0.05s ==================================================================
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

Note that `default.py` has 0% coverage because we didn't use it in the `test_module.py` test. 
We could have run the `test_default.py` test, but that would have failed and not generated a coverage report.
Also note that `other.py` has 100% coverage because there are no lines of code to be tested.
Finally, the `__init__.py` code has only 2/6 of the statements being executed.
We can have a better look at the coverage report by writing an html formatted report:
~~~
python -m pytest --cov=mymodule --cov-report html:coverage tests/test_module.py
~~~
{: .language-bash}
This will give use a report for each file in the directory `coverage`.
Let's open up the file `mymodule___init___py.html` (note the 3x underscores in the name), and see what statements were hit/missed during the testing.

> ## An exercise for the keen student
> Adjust the code/testing for mymodule such that all the functions are tested, all the tests pass, and you achieve 100% coverage on the coverage report.
{: .challenge}

## Automated testing
We have already learned about the `pytest` package that will run all our tests and summarize the results.
This is one form of automation, but it relies on the user/developer remembering to run the tests after altering the code.
Another form of automation is to have a dedicated workflow that will detect code changes, run the tests, and then report the results.
GitHub (and GitLab) have continuous integration (CI) tools that you can make use of to run a suite of tests every time you push a new commit, or make a pull request.