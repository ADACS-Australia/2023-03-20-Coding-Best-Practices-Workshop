---
title: "Packaging and publishing code"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---


## Include a README.md
Upon downloading new software, the first point of call for many people is to look for some help on how to install and use the software.
This is where a file such as `INSTRUCTIONS`, `INSTALL`, or `README` can come in handy.
The name of the file says what it is and will attract the attention of the user.
While these files can be in any format, and have any name, a common choice is `README.md`.
If you have navigated to a GitHub software repository, and seen the nice documentation available on the front page, then this has been generated from the `README.md` file.

The markdown format ([guide here](https://www.markdownguide.org/)) is a simple to use, future proof, platform independent, document format that can be rendered into a range of other formats.
As a bonus, the raw files are easily read and written by humans.

### Things to consider for your README.md file

- The name of the project
- A description of the purpose of the software
  - Maybe a one liner for each script
- Install instructions
  - List some high level dependencies
- Usage instructions
  - If you have a CLI then the output of mycode --help is appropriate to include verbatim
- A link to documentation
- Author information and contact details (email, or just a link to github issues)
- A note on how people should credit this work

> ## Create a README.md for your project
> Based on the above recommendations, write a short readme for this example project
> 
> commit/push this to Github and see how it renders the information
>
> Repeat until you are happy with the result.
{: .challenge}

## Useful project metadata
Previously we used an empty `__init__.py` file in a directory to cause python to interpret that directory as a module.
There is meta data that we wish to store about our project, and the `__init__.py` file is an excellent place to do this.

### Versioning
One of the most common items to store is the version of your software. For most modules the module.
`__version__` is used to store this information.
There are many conventions for software versioning and no one single correct answer.
Versioning is the practice of using unique numbers of names to refer to the different states of a software project or code.
A common choice is to use major/minor/patch versions for the code such as `4.2.1`, which is used by most python modules.
See [semver.org](https://semver.org/spec/v2.0.0.html) for a description on the how and why of semantic versioning.

A major version change will usually mean that the code has changed in some fundamental way, and that people should not expect compatibility between the two versions.
For example: there were many changes between the last version of python 2 (2.7) and python 3 that meant not all code would work on both versions.
If you have been using python for a while, or have seen python code from ~10 years ago (or ~2 years ago if it’s astronomers’ code!), then you’ll have seen some of these changes.
Most notable is the change from `print "hello"` to `print("hello")`.

A minor version change will usually indicate changes have been made that do not break compatibility within the major version.
This would usually include the addition of new functionality that is compatible with (but not available in) previous versions of the software.

A patch version is used to distinguish states of development that do not change the intended functionality of the code base.
These include bug fixes, security patches, or documentation updates.

Typically version 1.0 is used to represent the first stable/complete version of the software, and so versions such as 0.9 are used to indicate development versions.

### Modification date

In addition to a semantic versioning noted above, some developers find it useful to record the date of last change for each version of their software (and indeed each file/module within).
For this purpose we would make use of the `module.__date__` attribute.
Date formats are a perpetual problem for people and computers alike so it is recommended that a single format be chosen and used consistently throughout a project.
The format YYYY-MM-DD is recommended as it has the advantage of being time sorted when sorted alphanumerically.

### Authors / developers

One method tracking attribution (or blame) in a project is to use the `module.__author__` attribute to store the author name as either a string or list.
For a project with few developers this can be handled easily.
For larger groups or projects git blame would be a better method for tracking contributions on a line by line basis.

### Citation

For any researcher writing software there is an eternal battle between writing good code and "doing science".
Acknowledging the use of software is common but not yet standard or required when publishing papers.
To make it easier for people to cite your work you can use an attribute such as `module.__citation__` to employer people to cite your work, link to papers or code repositories that should be cited or referenced.
When combined with a `--cite` command line option, this is a great way for people to properly credit your work.
If your target audience are researchers then it can be very useful to store a bibtex entry in the citation string so that people can just copy/paste into their LaTeX document.

### Meta data for an example project
The `__init__` file in our example project can be updated to include the above recommendations.
Note the format of the `__citation__` string being multi line, and including LaTeX formatting.

~~~
# /usr/bin/env python

__author__ = ['Dev One', 'Contrib Two']
__version__ = '0.9'
__date__ = '2021-12-02'
__citation__ = """
% If this work is used to support a publication please
% cite the following publication:
% Description of This code
@ARTICLE{ExcellentCode_2022,
   author = { {One}, D. and {Two}, C. and {People}, O},
    title = "{Awesome sauce code for astronomy projects}",
  journal = {Nature},
 keywords = {techniques: image processing, catalogues, surveys},
     year = 2021,
    month = may,
   volume = 1337,
    pages = {11-15},
      doi = {some.doi/link.in.here}
}

% It is also appropriate to link to the following repository: https://github.com/devone/AwesomeSauce
"""
~~~
{: .output}

## Licensing your work
By default any creative work is under an exclusive copyright which means that the author(s) of that work have a say in what others can do with it.
In general this means that no one can build upon, use, reuse, or distribute your work without your permission.
To use or build upon software that has no license requires the new developer/user to contact the original author(s) and get permission.
This is time consuming, annoying, and often not done.
If you want your work to be used by others your best bet is to provide an explicit software license as part of your project so that people know up front what is allowed and not allowed.
A common way of licensing software is to provide a LICENSE (or LICENCE) file in the root of the project.
(Alternatively you can provide the license as part of the header for each file, but that’s a lot of repetition, and goes against our good practice of don’t repeat yourself).

### Choosing a software license for your project

Your home institute may have opinions/guidelines for appropriate licencsng software.
Ask around and follow the advice of you local experts.

If you don’t have any local constraints on licensing your software you can use one of the many license templates available on Github. 
To use a template you need to log into your Github account, navigate to your repository and then click the “add file”->”create new file” button.
You will be presented with a blank text editor and be asked for a file name.
If you use `LICENSE.md` (or any similar spelling/extension) then you’ll see a new button appear on the right of the screen saying “Choose a license template”.
Click that.

![Github Choose a License]({{page.root}}{% link fig/GitHubCreateLicence.png %})

You’ll then see a list of common software licenses that you can choose from.
If you are brave you can read each of them in full.
Alternatively you can simply read the Github provided summary at the top of what the permissions/limitations are.
Choose one that feels right to you and then press “Review and submit”.
This will create a new license file.

![Github choose a licence part 2]({{page.root}}{% link fig/GitHubCreateLicence2.png %})

Once you have a license file GitHub will add a badge to the “About” section of your project like this:

![Github choose a licence part 2]({{page.root}}{% link fig/GitHubAboutWithLicence.png %})

> ## License your work
> Use the GitHub tools described above to apply a new license to your project.
>
> `git pull` to your local repository when you are done so that your repo's are in sync.
{: .challenge}
