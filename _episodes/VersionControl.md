---
title: "Version Control"
teaching: 20
exercises: 15
questions:
- "What is version control?"
- "How is version control useful?"
objectives:
- "Put our sample project under version control"
- "Understand what should and should not be version controlled"
keypoints:
- "Git it great!"
- "Knowing that you can 'go back' should give you confidence to experiment"
---
## [Intro to Version Control](https://swcarpentry.github.io/git-novice/index.html)
We'll start by exploring how version control can be used to keep track of what one person did and when.
Even if you aren't collaborating with other people, automated version control is much better than this situation:

!["Piled Higher and Deeper" by Jorge Cham, http://www.phdcomics.com](http://www.phdcomics.com/comics/archive/phd101212s.gif)


We've all been in this situation before: it seems unnecessary to have multiple nearly-identical versions of the same document.
Some word processors let us deal with this a little better, such as Microsoft Word's [Track Changes](https://support.office.com/en-us/article/Track-changes-in-Word-197ba630-0f5f-4a8e-9a77-3712475e806a), Google Docs' [version history](https://support.google.com/docs/answer/190843?hl=en), or LibreOffice's [Recording and Displaying Changes](https://help.libreoffice.org/Common/Recording_and_Displaying_Changes).

Version control systems start with a base version of the document and then record changes you make each step of the way.
You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your more recent version.

![Changes Are Saved Sequentially](https://github.com/swcarpentry/git-novice/raw/gh-pages/fig/play-changes.svg){: width="600"}

Once you think of changes as separate from the document itself, you can then think about "playing back" different sets of changes on the base document, ultimately resulting in different versions of that document.
For example, two users can make independent sets of changes on the same document. 

![Different Versions Can be Saved](https://github.com/swcarpentry/git-novice/raw/gh-pages/fig/versions.svg){: width="600"}

Unless multiple users make changes to the same section of the document - a conflict - you can incorporate two sets of changes into the same base document.

![Multiple Versions Can be Merged](https://github.com/swcarpentry/git-novice/raw/gh-pages/fig/merge.svg){: width="600"}

A version control system is a tool that keeps track of these changes for us, effectively creating different versions of our files.
It allows us to decide which changes will be made to the next version (each record of these changes is called a `commit`), and keeps useful metadata about them.
The complete history of commits for a particular project and their metadata make up a `repository`.
Repositories can be kept in sync across different computers, facilitating collaboration among different people.

> ## Paper Writing
>
> *   Imagine you drafted an excellent paragraph for a paper you are writing, but later ruin 
>     it. How would you retrieve the *excellent* version of your conclusion? Is it even possible?
>
> *   Imagine you have 5 co-authors. How would you manage the changes and comments 
>     they make to your paper?  If you use LibreOffice Writer or Microsoft Word, what happens if 
>     you accept changes made using the `Track Changes` option? Do you have a 
>     history of those changes?
>
> Share your thoughts and experience on the [etherpad]({{site.ether_pad}})
>
> > ## Solution
> >
> > *   Recovering the excellent version is only possible if you created a copy
> >     of the old version of the paper. The danger of losing good versions
> >     often leads to the problematic workflow illustrated in the PhD Comics
> >     cartoon at the top of this page.
> >     
> > *   Collaborative writing with traditional word processors is cumbersome.
> >     Either every collaborator has to work on a document sequentially
> >     (slowing down the process of writing), or you have to send out a
> >     version to all collaborators and manually merge their comments into
> >     your document. The 'track changes' or 'record changes' option can
> >     highlight changes for you and simplifies merging, but as soon as you
> >     accept changes you will lose their history. You will then no longer
> >     know who suggested that change, why it was suggested, or when it was
> >     merged into the rest of the document. Even online word processors like
> >     Google Docs or Microsoft Office Online do not fully resolve these
> >     problems.
> {: .solution}
{: .challenge}


## Version Control for software projects
The above lesson focuses on text documents such as you might use for writing a paper (e.g. LaTeX).
However, software is written as text based documents so the above applies equally to all the code that we write.
Lets make a start on our project by keeping that first proof of concept script under version control.

> ## Start a new project
> - Move into the root directory for our project
> - Initialize a git repository in this directory by typing `git init`
> - Tell git that you want to track your `README.md` and `sky_sim.py` files using `git add <filename>`
> - Save your initial progress by creating a new commit to your repository via `git commit -m <message>`
>   - The first commit message can be something simple like "initial version" or "proof of concept"
> - Check that you have committed your progress by running `git log`
>
> If git gets your goat, have a yarn in the [etherpad]({{site.ether_pad}})
{: .challenge}

If at any point we are editing our work and we break something, or change our mind about what we are doing, so long as we have the files under version control we can go back to our previous save point using:
~~~
git checkout -- <filename>
~~~
{: .language-bash}

If we want to reach way back in time we can do
~~~
git checkout <hash> <filename>
~~~
{: .language-bash}

Where the `<hash>` is one of the long alphanumeric strings that are shown when we run `git log`.
Having good commit messages will make it easier to tell which commit we should be going back to.

> ## Small changes, often
> It is good practice, where possible, to make many small commits rather than a few large commits.
> This strategy will help you have a finer grained 'undo', and when you start branching and merging, it will result in fewer and smaller merge conflicts.
> 
{: .callout}

Now we have some first step that we can come back to later if we mess things up.