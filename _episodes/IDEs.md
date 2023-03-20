---
title: "Interactive Development Environments"
teaching: 15
exercises: 15
questions:
- "What is and IDE?"
- "What is **The best** IDE?"
- "What have IDEs ever done for us?"
objectives:
- "Review how we edit our code"
- "Preview some of the nice features of VSCode"
keypoints:
- "VSCode is amazing"
- "Many IDEs learn from each other so at some level they are mostly the same"
- "Use what you like best and what is supported locally"
---

## Your personal work environment
Having the right number and right type of screens can really boost your productivity.
So can a comfortable keyboard and mouse, a good chair, and even some great "in the zone" music over a good set of headphones.
You'll also find a great productivity boost by using a text editor that does more than just read/write files for you.
Vim and emacs are great, and do have some great plugins and features that help you with your coding experience, but a purpose build interactive development environment is hard to beat.

In this episode will be demonstrating some of the great features of [VSCode](https://code.visualstudio.com/).
Not because we are shills for microsoft, but because VSCode is genuinely excellent and is the tool of choice in our office.

Other notable products which provide many/all the features of VSCode include:
- [Pycharm](https://www.jetbrains.com/pycharm/) (and the rest of the JetBrains suite TBH)
- [kate](https://kate-editor.org/)
- [eclipse](https://www.eclipse.org/downloads/) (mostly Java focused)
- [atom](https://github.com/atom) (precursor to VSCode, now sunset)
- [sublime text](https://www.sublimetext.com/)
- [code::blocks](http://www.codeblocks.org/)
- [JupyterLab](https://jupyter.org/) (not just for notebooks!)

No matter which of the IDEs you use, you should have a look at the plugins/extensions that are available as they can add a huge amount of functionality.

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

![VSCode python testing]({{page.root}}{% link fig/VSCodeTesting.png%})

### Git things
![VSCode GitHub integration]({{page.root}}{%link fig/VSCodeGitIntegration.png%})

![VSCode Git diff]({{page.root}}{%link fig/VSCodeGitDiff.png%})

![VSCode Git merge classic]({{page.root}}{% link fig/VSCodeMergeClassic.png%})

![VSCode Git merge 3 way view]({{page.root}}{% link fig/VSCodeMergeAdvanced.png %})

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

Or using [remote tunnels](https://code.visualstudio.com/docs/remote/tunnels) instead of ssh (with a GitHub account):
![Remote dev without ssh](https://code.visualstudio.com/assets/docs/remote/vscode-server/server-arch-latest.png)


> ## What features do you wish existed?
> Use the [etherpad]({{site.ether_pad}}) to describe a feature that you'd love to see in your IDE.
>
> Browse the list and see if you can help people out!
{: .challenge}

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