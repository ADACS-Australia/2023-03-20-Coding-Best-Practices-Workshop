---
title: "Managing software dependencies"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---
## Virtual environments
From the python [documentation](https://docs.python.org/3/tutorial/venv.html):

> Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.
>
> This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.
>
> The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.
>
> Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.
> 
{: .quote}

There are two ways to setup virtual environments and manage dependencies: using `pip` or using `anaconda`

## venv, pip, and requirements.txt

A virtual environment can be set up in the following way.
~~~
python -m venv [--prompt PROMPT] ENV_DIR
~~~
{: .language-bash}
By default the `PROMPT` is equal to the `ENV_DIR`.

Once set up you can activate the environment via:
~~~
source ENV_DIR/bin/activate
~~~
{: .language-bash}

Once you have activated the environment your command line will be prepended with (PROMPT) to remind you that you are using the given environment.
To exit the environment you can either activate a different one (they don't "stack"), or type *deactivate*.

Here is how I set up an environment for generic use:
~~~
python -m venv --prompt py3 ~/.py3-generic
echo 'alias py3="source ~/.py3-generic/bin/activate"' >> ~/.bash_aliases
py3
pip install scipy numpy astropy matplotlib jupyterlab
~~~
{: .language-bash}

`pip` is the default, OG, package manager for python, and it will search the python package index ([pypi.org](https://pypi.org/)) for the modules that you specify, and then install them.
As part of this process `pip` will compare the dependencies listed by each module and install/upgrade them if needed.
This means that installing one package can result in lots of other packages also being installed.

In order to port your virtual environment to another machine, the best practice is to set up a file such as `requirements.txt` that contains all the modules and module versions that you want to have in the environment.
This file can then be used to tell `pip` which modules are required to get your code working.

For example, this workshop could have the following dependencies listed in `requirements.txt`:
~~~
numpy
pdoc
pylint
pytest
pytest-cov
scalene
~~~
{: .language-python}

When a user runs `pip install -r requirements.txt` they will install the latest version of each of these modules (depending on their version of python), as well as all the modules that these will in turn depend on.

If I were to install the above:
~~~
pip install -r requirements.txt
~~~
{: .language-bash}

I would get a long output that ends with:
~~~
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 astroid-2.15.0 astunparse-1.6.3 attrs-22.2.0 cloudpickle-2.2.1 coverage-7.2.1 dill-0.3.6 exceptiongroup-1.1.1 iniconfig-2.0.0 isort-5.12.0 lazy-object-proxy-1.9.0 markdown-it-py-2.2.0 mccabe-0.7.0 mdurl-0.1.2 numpy-1.24.2 packaging-23.0 pdoc-13.0.0 platformdirs-3.1.1 pluggy-1.0.0 pygments-2.14.0 pylint-2.17.0 pynvml-11.5.0 pytest-7.2.2 pytest-cov-4.0.0 rich-13.3.2 scalene-1.5.20 six-1.16.0 tomli-2.0.1 tomlkit-0.11.6 typing-extensions-4.5.0 wheel-0.38.4 wrapt-1.15.0
~~~
{: .output}

So you can see which modules where installed and their versions.
As I install more and more modules in my environment I can see a complete listing by typing `pip freeze`:
~~~
$ pip freeze
astroid==2.15.0
astunparse==1.6.3
attrs==22.2.0
cloudpickle==2.2.1
coverage==7.2.1
dill==0.3.6
exceptiongroup==1.1.1
iniconfig==2.0.0
isort==5.12.0
Jinja2==3.1.2
lazy-object-proxy==1.9.0
markdown-it-py==2.2.0
MarkupSafe==2.1.2
mccabe==0.7.0
mdurl==0.1.2
numpy==1.24.2
packaging==23.0
pdoc==13.0.0
platformdirs==3.1.1
pluggy==1.0.0
Pygments==2.14.0
pylint==2.17.0
pynvml==11.5.0
pytest==7.2.2
pytest-cov==4.0.0
rich==13.3.2
scalene==1.5.20
six==1.16.0
tomli==2.0.1
tomlkit==0.11.6
typing-extensions==4.5.0
wrapt==1.15.0
~~~
{: .output}

If I were being pedantic I could list the above as my dependencies by saving this all into a requirements file.
If I were being not lazy I would go through the above and pick out the versions of numpy et. al and remove the others, and keep that in my requirements file.

The process for new people using your software then becomes:
- download the software (`git clone <repo>`)
- install dependencies (`pip install -r requirements.txt`)
- run the code (`sky_sim.py --help`)

Which is much easier to describe.

## *conda and environment.yaml

Anaconda (and miniconda, and conda) offers an alternative package management system.
Anaconda can also create different environments for you to work within, and these can be specified using a configuration file typically called `environment.yaml`.
By default Anaconda will pull python modules from it's own package index, but it can be told to pull packages from pypi.org as well.
Unlike `pip`, Anaconda can also manage environments that contain different python versions, different c/fortran compilers and a range of other software as well.
Anaconda has a graphic interface that most windows/mac users will be familiar with.
See [here](https://docs.anaconda.com/navigator/tutorials/manage-packages/) for instructions on how to work with the GUI.
From the command line you can work in a way that is similar to `pip`.

If you are using conda or Anaconda from the command line then the relevant instructions are:
- Create a new environment with `conda create --name myenv --prefix ./envs`.
  - In contrast to pip, the `--prefix` specifies the location that the files will be stored, and `--name` specifies the name of the environment which will be prepended to your command line when activated.
  - You can optionally also include `python=3.9` to specify the version of python that you want to use in this environement (something that pip/venv doesn't easily support).
- Activating a conda environment is done via `conda activate ./env` where `./env` is the directory that stores your environment.
- Once activated you can install modules using `conda install <module name>`.
- You can list the modules installed in the current environment using `conda env list`.
- To build an `environment.yaml` file you can use `conda env export > environment.yaml`, which can then be loaded via `conda create -f environment.yaml`


## which to use?
If you are publishing your code on pypi.org (see [PythonPackages]({{page.root}}{% link _episodes/PythonPackages.md %})), then it is best to use a `requirements.txt` file, however you can be agnostic and provide both files.
To avoid duplication (recall DRY?) you can list all your python requirements in a requirements file, and then use the following `environment.yaml` file:
~~~
name: my-env
dependencies:
  - python>=3.6
  - anaconda
  - pip
  - pip:
    - -r requirements.txt
~~~
{: .output}