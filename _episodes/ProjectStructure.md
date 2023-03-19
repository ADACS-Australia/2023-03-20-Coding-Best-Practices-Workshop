---
title: "Project Structure"
teaching: 15
exercises: 15
questions:
- "How do I start a new project?"
- "What can I do early in a project to make my life easier later on?"
objectives:
- "Understand the utility of a planned project structure"
- "Create a new project plan"
keypoints:
- "Planning is important"
- "Project structure will help you organize your work"
---

## Beginning a new software project

Before we do anything to our project we should talk about organization.

### Organization
Organization is key to a good project.
Every time you start a new project or explore a new idea it is a good idea to create a new space for that project.
This means creating a new directory for you to collect all the relevant data, software, and documentation.
You will be involved in many projects through your career and often will have to manage multiple projects simultaneously.
It is therefore not just a good idea to organize each project, but to have a consistent organization structure between projects.
In this section we will make some recommendations for organizing a software project.

### Put each project in its own directory, which is named after the project.

The location of this directory will depend on a higher level organization scheme.
For example you may separate your projects based on funding, based on collaboration, or based on research area.

Within you software project directory we recommend the following structure:
~~~
.
├── README.md          <- Description of this project
├── bin                <- Your compiled code can be stored here (not tracked by git)
├── config             <- Configuration files, e.g., for sphinx or for your model if needed
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for analysis.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Documentation, e.g., sphinx or reference papers (not tracked by git)
├── env                <- Python environment specific to this project
├── notebooks          <- Jupyter or R notebooks
├── reports            <- For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
│   └── figures        <- Figures for the manuscript or reports
└── src                <- Source code for this project
    ├── external       <- Any external source code, e.g., pull other git projects libraries
    └── tools          <- Any helper scripts go here
~~~
{: .output}

Setting up an empty structure such as the above can be done either by making an template and then copying that every time you start a new project.
Additionally there are python packages such as `cookiecutter` ([pypi](https://pypi.org/project/cookiecutter/), [rtfd](https://cookiecutter.readthedocs.io/en/1.7.2/), [github](https://github.com/audreyfeldroy/cookiecutter-pypackage)) that can automate this process for you, and offer a range of templates to work with.

### Name all files to reflect their content or function.
(Recall: Naming is important)

It is also convenient to use a consistent and descriptive naming format for all your files and sub-folders. For example, use names such as `galaxy_count_table.csv`, `manuscript.md`, or `light_curve_analysis.py`.
Do not using sequential numbers (e.g., `result1.csv`, `result2.csv`) or a location in a final manuscript (e.g., `fig_3_a.png`), since those numbers will almost certainly change as the project evolves (and are meaningless on their own).


> ## Structure our project
> - Create a new directory for your project with a name that makes sense to you
> - Create a directory to store our scripts called `mymodule`
> - Save your initial python script as `sky_sim.py` and put it in the module directory
> - Create a `README.md` file and make a short note about what this project is about
{: .challenge}