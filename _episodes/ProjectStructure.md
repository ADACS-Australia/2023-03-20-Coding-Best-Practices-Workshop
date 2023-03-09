---
title: "Project Structure"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

## Project structure
Before you start a new project consider using the following template:

Research project:
```
.
├── README.md          <- Description of this project
├── bin                <- Your compiled code can be stored here (not tracked by git)
├── config             <- Configuration files, e.g., for doxygen or for your model if needed
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for analysis.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Documentation, e.g., doxygen or reference papers (not tracked by git)
├── notebooks          <- Jupyter or R notebooks
├── reports            <- For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── external       <- Any external source code, e.g., pull other git projects libraries
    └── tools          <- Any helper scripts go here
```
{: .language-bash}


Python project:
This is for a module called `sample`.
```
README.md
LICENSE.md
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```
{: .language-bash}

Pick and choose from the above to create your own project structure.

## Beginning a new software project

Before we do anything to our project we should talk about:

### Organisation
Organisation is key to a good project. Every time you start a new project or explore a new idea it is a good idea to create a new space for that project. This means creating a new directory for you to collect all the relevant data, software, and documentation. You will be involved in many projects through your career and often will have to manage multiple projects simultaneously. It is therefore not just a good idea to organise each project, but to have a consistent organisation structure between projects. In this section we will make some recommendations for organising a software project.

### Put each project in its own directory, which is named after the project.

The location of this directory will depend on a higher level organisation scheme. For example you may separate your projects based on funding, based on collaboration, or based on research area.

Within you software project directory we recommend the following structure:
```
.
├── README.md          <- Description of this project
├── bin                <- Your compiled code can be stored here (not tracked by git)
├── config             <- Configuration files, e.g., for doxygen or for your model if needed
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for analysis.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Documentation, e.g., doxygen or reference papers (not tracked by git)
├── notebooks          <- Jupyter or R notebooks
├── reports            <- For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── external       <- Any external source code, e.g., pull other git projects libraries
    └── tools          <- Any helper scripts go here
```
{: .output}

Setting up an empty structure such as the above can be done either by making an template and then copying that every time you start a new project. Additionally there are python packages such as `cookiecutter` ([pypi](https://pypi.org/project/cookiecutter/), [rtfd](https://cookiecutter.readthedocs.io/en/1.7.2/), [github](https://github.com/audreyfeldroy/cookiecutter-pypackage)) that can automate this process for you, and offer a range of templates to work with.

### Name all files to reflect their content or function.

It is also convenient to use a consistent and descriptive naming format for all your files and sub-folders. For example, use names such as `galaxy_count_table.csv`, `manuscript.md`, or `light_curve_analysis.py`.
Do not using sequential numbers (e.g., `result1.csv`, `result2.csv`) or a location in a final manuscript (e.g., `fig_3_a.png`), since those numbers will almost certainly change as the project evolves (and are meaningless on their own).

## Project evolution

In the typical project cycle for an astronomer or research software engineer (or [RSE](https://rse-aunz.github.io/), a formal name for people who combine professional software expertise with an understanding of research), you will not sit down and have a detailed discussion about what the project is, where it needs to go, what the user stories and milestones are, and who will be involved. Usually research evolves organically through informal discussions with colleagues, or a sudden thought in the shower. Similarly our software projects evolve in an organic manner, often beginning with a small script of function to do just this one thing, which then over time gets used, reused, augmented, shared, and thus evolves into a software project. This evolution of ideas and code does not fit will with much of the more formal structures that professional software developers adhere to, and so we will not try to fit our projects to such a scheme. Instead we will create a path for our software that will be suited to our work style, but which draws on the knowledge and experience of professional software developers. Thus we will begin with a proof of concept code – a short bit of work that proves that something works using the minimal amount of effort.