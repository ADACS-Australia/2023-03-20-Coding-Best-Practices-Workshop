---
title: "Interactive Development Environments"
teaching: 15
exercises: 15
questions:
- "TODO"
objectives:
- "TODO"
keypoints:
- "TODO"
---

## Your personal work environment
Having the right number and right type of screens can really boost your productivity.
So can a comfortable keyboard and mouse, a good chair, and even some great "in the zone" music over a good set of headphones.
You'll also find a great productivity boost by using a text editor that does more than just read/write files for you.
Vim and emacs are great, and do have some great plugins and features that help you with your coding experience, but a a purpose build interactive development environment is hard to beat.

In this episode will be demonstrating some of the great features of [VSCode](https://code.visualstudio.com/).
Not because we are shills for microsoft, but because VSCode is genuinely excellent and is the tool of choice in our office.

Other notable products which provide many/all the features of VSCode include:
- [Pycharm](https://www.jetbrains.com/pycharm/) (and the rest of the JetBrains suite TBH)
- TODO that thing that Leigh uses a lot - [kate](https://kate-editor.org/)?
- TODO one more thing to demonstrate this isn't just a VSCode love fest


> ## What do you use?
> Please list the IDEs that you use (favorite or not), on the [etherpad]({{site.ether_pad}})
>
> If you have an "in the zone" playlist, link that too!
{: .challenge}

## IDE examples

TODO: Demo screen shots and discussion for the below

Screenshots with some highlights of:
- git panel, including in-document indications of what changes
- live syntax highlighting and PEP recommendations
  - missing modules
  - unused imports, arguments, language aware spelling
- code folding
- in-document help for functions/classes
- testing panel
- multiple environment support
- docker panel
- support for multiple languages in a single project
- remote coding (vis ssh)

> ## Want more magic?
> Go to [my project](https://github.com/PaulHancock/Aegean/blob/main/AegeanTools/MIMAS.py) and press '.'
> > 
> > ![mega brain](http://www.reactiongifs.com/r/yjbmm.gif)
> {: .solution}
{: .challenge}



## Summary
There is no one best IDE.
Use one that you like, one that has features that will help you work better, and one that you can find help for when you don't know how do to something.
I moved from using pycharm to VSCode primarily because no-one else that I worked with used pycharm and I couldn't get help when I was stuck!

Also, don't forget about good old vim/emacs, because sometimes you will be ssh-ed into a machine that has no X forwarding and you just have to make that one change at 2am!