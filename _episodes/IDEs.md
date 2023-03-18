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

## VSCode examples

### Python things

Can easily swap between environments, will automatically use `env` in the project directory.
Can easily create environments.

![VSCode Nice Python things]({{page.root}}{% link fig/VSCodePythonNice.png%})

Also will show:
- unused imports, 
- variables that are never referenced, 
- variables with confusing names,
- variables that mirror global variables
- missing doc strings
- inline help for all modules/functions in current environment including **your** functions/classes/modules
- prompt you to pip/conda install modules that you import but are in the current env

Additionally you can fold blocks of code, which is great for long code bases.

TODO: screenshot for testing, debugging

### Git things
![VSCode GitHub integration]({{page.root}}{%link fig/VSCodeGitIntegration.png%})

![VSCode Git diff]({{page.root}}{%link fig/VSCodeGitDiff.png%})

![VSCode GitGraph plugin]({{page.root}}{%link fig/VSCodeGitGraph.png%})

### Docker

![VSCode Docker plugin]({{page.root}}{%link fig/VSCodeDockerPlugin.png%})

From this panel you can easily prune containers that have stopped but are not shut down.
This is especially good when you have been building containers.

### Other things
Support for multiple languages in a single project, including multiple environments and linting etc.

[Develop remotely using ssh](https://code.visualstudio.com/docs/remote/ssh):
![VSCode remote](https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png)
This is **much** faster than running VSCode remotely and forwarding an X11 session.




> ## Want more magic?
> Go to [my project](https://github.com/PaulHancock/Aegean/blob/main/AegeanTools/MIMAS.py) and press '.'
> 
> > ## Yes
> > ![mega brain](http://www.reactiongifs.com/r/yjbmm.gif)
> {: .solution}
{: .challenge}



## Summary
There is no one best IDE.
Use one that you like, one that has features that will help you work better, and one that you can find help for when you don't know how do to something.
I moved from using pycharm to VSCode primarily because no-one else that I worked with used pycharm and I couldn't get help when I was stuck!

Also, don't forget about good old vim/emacs, because sometimes you will be ssh-ed into a machine that has no X forwarding and you just have to make that one change at 2am!