---
title: "Introduction and setup"
teaching: 15
exercises: 15
questions:
- "How can I prepare?"
- "How will we be learning?"
objectives:
- "Set expectations for engagement and behavior"
keypoints:
- "Ask questions, experiment, and help others"
- "Everyone is here to learn and that means making mistakes"
---
## Acknowledgement of country
We wish to acknowledge the custodians of the land we reside on. These lessons were developed on the lands of the Wadjuk (Perth region) people of the Nyoongar nation. This workshop will be delivered on the lands of the Bedegal people (UNSW campus), and we will be using computing resources that are on the lands of the Ngunnawal and Ngambri people (Canberra region).
We pay our respect to their Elders and acknowledge their continuing culture and the contribution they make to the life of our cities and regions. 


## Overview
This training was developed by [ADACS](https://adacs.org.au) at the request of Caroline Foster as part of their 2023A training project.

This workshop is intended for researchers who have little or no formal computing training, but who have learned to get by via self or peer learning, and who are interested to being exposed to some best practices in computing and software development.

This workshop has been developed in the style of Carpentries (hence the site layout) but is not an official Carpentries lesson.
Some of the content is intended for learners to read, think, and ask questions, some of it will require learners to write code or use the HPC facility for themselves, and other parts will be treated as a discussion session where no or little computing interaction will be needed.

## Required software / services
You will need:
- Access to Zoom video conferencing system (for remote participants, depending on which works on the day!)
  - [Join from PC, Mac, Linux, iOS or Android](https://unsw.zoom.us/j/86138935425?pwd=dXBpVC9nWnh5RnBSWmpGUlpRSUc0QT09) 
  - Password: see [etherpad]({{site.ether_pad}})
- A bash terminal
- An account on NCI  (see below)
- A zest for life

See instructions on the [home page]({{page.root}}#Setup)

### An account on NCI
You will need to have an account on the National Compute Infrastructure (NCI) in order to complete some of the exercises for this course.
See [these instructions](https://my.nci.org.au/mancini/signup/0) for how you can obtain an account.

Once you have an account you'll need to join the group `vp91`.

## Assumed knowledge
This course assumes that you have basic proficiency in python.

One of the main lessons for this workshop is to use version control for all your text based projects (papers / code).
For this we will be using the git version control system, and in particular we will be using GitHub as the remote repository.

Software requirements

- Python 3.6 +
- A integrated development environment ([IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)) or text editor of choice
  - We recommend [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/)
- An operating system which gives you a proper command line
  - For windows this means using something like [gitbash](https://gitforwindows.org/), [WSL](https://docs.microsoft.com/en-us/windows/wsl/install), or the [Anaconda](https://www.anaconda.com/) prompt
  - For OSX or Linux the regular terminal will be fine
- git, either from the command line, using a git desktop app, or as an add on to PyCharm or VSCode.

An account on [GitHub](https://github.com/) is required for some of the activities.


- (linux) command line / bash [SWC Lesson](https://swcarpentry.github.io/shell-novice/), [ADACS Lesson](https://adacs.org.au/courses/introduction-to-bash/)
- ssh login
- command line text editor ([emacs](https://www.linuxfordevices.com/tutorials/linux/emacs-editor-tutorial)/[vim](https://www.tutorialspoint.com/vim/index.htm#)/[nano](https://www.linuxfordevices.com/tutorials/linux/nano-editor-in-linux))
- Python scripting [SWC Lesson](http://swcarpentry.github.io/python-novice-gapminder/), [ADACS Lesson](https://adacs.org.au/courses/introduction-to-python/)

## Engagement

This workshop is developed for three main delivery methods:
1. Facilitated, in person, at UNSW
2. Facilitated, online, in parallel with (1)
3. Self-paced, online, via this website.

This workshop is all about learning by doing.
We will be engaging in live coding type exercises for most of the workshop, and we will set challenges and exercises for you to complete in groups.
The more you engage with your fellow learners and the more questions that you ask, the more that you will get out of this workshop.

We will be using sticky notes for in-person participants to indicate their readiness to move on: please stick them on your laptop screen to indicate if you need help or are done and ready to move ahead.
For those joining online we'll be using emotes to indicate the same.

We will use a shared document ([etherpad](https://pad.carpentries.org/2023-03-20CodingSydney)) to manage and record many of our interactions.


## Conduct

This workshop will be an inclusive and equitable space, which respects:
- the lived experience of it's attendees,
- the right for all to learn, and 
- the fact that learning means making mistakes.

We ask that you follow these guidelines:

- Behave professionally. Harassment and sexist, racist, or exclusionary comments or jokes are not appropriate.
- All communication should be appropriate for a professional audience including people of many different backgrounds. 
- Sexual or sexist language and imagery is not appropriate.
- Be considerate and respectful to others.
- Do not insult or put down other attendees.
- Critique ideas rather than individuals.
- Do not engage in tech-shaming.

See the [ASA2022 code of conduct](https://www.asa2022.org/code-of-conduct) and the [Software Carpentries code of conduct](https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html) for more information.



> ## Introduce yourselves
> ![IceBreaker](https://ichef.bbci.co.uk/news/976/cpsprodpb/D6B5/production/_123956945_225107a3-318d-4c2e-b040-2dcd03c4698a.jpg){: width="400"}
> 
> Introduce yourself to your peers by telling us your name, a band you are listening to at the moment, and your favorite kind of pet.
> 
> Do this in person and via the [etherpad]({{site.ether_pad}}).
{: .challenge}