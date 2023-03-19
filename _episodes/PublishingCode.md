---
title: "Publishing code"
teaching: 15
exercises: 20
questions:
- "Why publish code?"
- "What does 'publish' even mean?"
- "Ok, so how and where can I publish my code?"
objectives:
- "Review the FAIR principles for software publishing"
- "Be able to publish code to Zenodo and recieve a DOI"
- "Be able to register your code on ASCL.net"
keypoints:
- "You deserve credit for all the work you do"
- "Publishing code can help you increase your publication/citation rate"
- "Publishing your code 'pays forward' the efforts of people who developed your dependencies"
---

# Publishing code
Publishing your software will allow you to share your work with a larger audience.
Having your software shared online will increase the visibility of your work, which can lead to greater recognition of your work through software citation.

Developing or contributing to a software package that is widely used is another way that your effort can be recognized and can be used to strengthen a grant, scholarship, or job application.

Any code that you use as part of your research should be considered for publication.
Depending on the size of the codebase, the intended audience, and intended use of the code, you will want to put a different amount of effort into publishing and publicizing your work.

At the very least, you should keep all your work under version control, and have these repositories "backed up" or "mirrored" online to guard against data loss.
GitHub, GitLab, and Bitbucket are great places to do this, and so long as you don't set your repository to be private, then you have published your work.

Once you have code that you are happy to share among collaborators you should consider publishing this code.

What do we mean by publishing? From least to greatest effort, any of the following could be considered as a definition for publishing code:

1. Copying a version of your code to a public website for others to find and use,
2. Making your version control repository (github, gitlab, bitbucket) public so that others can use and reuse your code,
3. Uploading your code to a repository such a [pypi.org](http://pypi.org/) so that others can easily download/install your software,
4. Archiving a version of your code to a doi minting / storage service such as [zenodo.org](http://zenodo.org/), or [figshare](https://figshare.com/),
5. Registering your code on a site such as [ascl.net](http://ascl.net/) so that others can find your code,
6. Writing a paper describing an application of your code and submitting for peer review in a science focused journal such as [PASA](https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia) or [MNRAS](https://academic.oup.com/mnras),
7. Writing a companion paper that describes your code and submitting the paper and code for peer review in a software focused journal such as [A&C](https://www.journals.elsevier.com/astronomy-and-computing), [JOSS](https://joss.theoj.org/), [RNAAS](https://iopscience.iop.org/journal/2515-5172), or [SoftwareX](https://www.sciencedirect.com/journal/softwarex).

From the descriptions above you can see that the different options have slightly different intentions and audiences. We can take an lead from [FAIR principles for data](https://ardc.edu.au/resources/working-with-data/fair-data/), and apply these principles to code.

### Findable
Make code findable by creating a persistent identifier (eg doi) and including metadata.
On pypi/zenodo/github you can use tags or topics to identify the software language but also the area of research or methodology that is being used.
This makes it easier for people to find code that will suit their needs.

### Accessible
Make code accessible by providing source code, install instructions, and documentation.
Testing code on a range of platforms will also increase the accessibility of the code.

### Interoperable
Use standard project templates, coding styles and idioms, and a modular design to allow your code to be used as part of a larger workflow or as a component of another product.
This interoperability is useful for others, but will also make it easier for you to build on your own existing solutions.

### Reusable
Make code reusable by providing a license, and indicating how people should acknowledge use of your work.

## Reasons not to publish
The following are often given as reasons not to publish code:

| Reason                                                       | Counter argument                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I don’t want to have to “support” my code.                   | Publishing code does not commit you to providing endless support. If you do not intend to reply to emails, fix bugs, or make updates to the code, simply say so in the README.md file. If this is the case you could invite keen users to fork the repo and provide their own fixes.                                                                                                                                        |
| I don’t want people to steal my good work.                   | With an appropriate license and attribution request, you can let others use your work while you benefit from their reuse. If there is a paper that describes or uses the code, you can ask for it to be cited by others, and this will increase the impact of that paper (and your h-index!).                                                                                                                               |
| My code is a bit hacky and I don’t want others to see it.    | Being embarrassed about less-than-perfect code is normal. However, a quick scan of GitHub will show you that hacked-together code is very common even among professional developers. If your code serves it’s intended purpose then it’s good enough to share. Consider writing a short blurb in the README.md file that clearly state the intended aim of the code, so that you can manage the expectations of your users. |
| I don’t know how to share my code.                           | It’s not difficult to share code, and it’s easy to learn. This course is one of many (MANY) that take you through the steps of sharing or publishing code. The small investment to learn how to share code will pay off quickly when you start to discover and use code written by others, get feedback and recognition for your code, or when your computer dies and you need to recover your work.                        |
| My code contains sensitive IP that I’m not allowed to share. | **Good argument!** Keep it secure some place. Many of the steps that you would take to prepare your data for publication are still worth doing to make your code usable within your trusted network.                                                                                                                                                                                                                        |

## Obtaining a doi from Zenodo.org
You have a piece of code on github, but it is changing over time, and you would like to provide a link to a particular version of the code.
This is important for reproducibility of your research work, both for yourself and others.

The [Zenodo](https://zenodo.org/) repository provides a safe, trusted, and citable place to host your code.
Zenodo is primarily focused on the storage of data, but this includes: documentation, papers, posters, raw or processed data, source code, and compiled binaries.
Zenodo will allow you to version your data but does not provide a version control system such as git.
However, Zenodo and Github are friends so you can link them together to get the best of both worlds.

### Sign up to Zenodo

You can create a new Zenodo account using an email address and password, or you can use your Github or [ORCID](https://orcid.org/) accounts to login.
Whatever you choose, you can still link your github/ORCID later and use them to sign in.

### Create a new repository

Once signed in click on the upload button at the top of the page, and then on the next page click “New Upload”:

![Zenodo Header]({{page.root}}{% link fig/ZenodoHeader.png %})

The following page will have a lot of details, some of which are mandatory, but most of which are either recommended or optional.
Begin by downloading a .zip of your files from Github:

![GitHub download a zip file]({{page.root}}{% link fig/GitHubDownloadZip.png %})

Once you have your zip file from GitHub, upload it to Zenodo, and then press the green “start upload” button and then start filling out the rest of the form.
As the upload is progressing you can fill in the upload type (Software) and basic information.

Leave the DOI blank, but click the “reserve DOI” button so that you can know what the final DOI will be.

Fill in the remainder of the form and then press “save” at the top of the page, this will make a draft of your repository that you can come back to later and update.
When you are finally happy with all the details you can press ‘publish’.

Once your upload has been published you should navigate to the published repository in your uploads list, and select it.

![Zenodo about section]({{page.root}}{% link fig/ZenodoAbout.png%})

The above example is for the Aegean source finding software.
You can see the DOI badge with the full DOI, a link to supplementary material, and the license.
If you click the DOI badge you’ll get a new pane that shows you how to embed this information into a markdown file such as your `README.md` that you have on your github page!

Below this panel you can also see a box that allows people to cite your code. There is even a box that allows people to get the citation in any format that they need it.

![Zenodo cite as]({{page.root}}{% link fig/ZenodoCite.png %})

You now have a version of your code which is archived on Zenodo and will not change.
If you want to update the archive with new versions of the code, Zenodo has the capacity to do this, and will mint a new doi for each version.
It is recommended that you don’t make a new doi for every small change you make to your code.
A new version for each major or minor version change would be appropriate, or when you have published work that used a particular major/minor/patch version of the code.

Sadly Zenodo is not indexed by [ADS](https://ui.adsabs.harvard.edu/) so you can’t track citations very well from here.
However, ASCL.net *is* indexed by ADS so we can register our code on there.

## Registering your code on ascl.net
In this section we’ll make an entry in the Astrophysics Source Code Library ([ASCL.net](https://ascl.net/)), which is indexed by ADS, and can help you gain an audience, and track citations.

### Submit a code to ASCL

Go to the “submit a code” page [here](https://ascl.net/code/submit).

The page asks for a title, credit (authors/contributors), abstract, and a site list for the code.

The site list should be a list of links to places where people can obtain the code.
I highly recommend that you put a link to both your Github and Zenodo repositories.
If the code was described in a paper you can put that in the “Preferred Citation Method” section.

![ASCL.net submit a code]({{page.root}}{% link fig/ASCLSubmitCode.png %})

ASCL.net does not store your code.
No one will vet the quality of your code.
ASCL.net is simply a place to register that some code exists and that you’d like to be acknowledged for creating/contributing.
ASCL.net is indexed by ADS so it will get a bibcode in ADS, which can then be used to generate a bibtex entry for people to use when citing your code.
Another goal of ASCL.net is to make it easier for people to find your code in the first place.
If you haven’t explored the code available here I recommend that you do so now – there are some gems.


## Where else?
Of course we have skipped the most logical place for us to publish our python code - `pypi.org`!
In the next episode we'll cover just that.