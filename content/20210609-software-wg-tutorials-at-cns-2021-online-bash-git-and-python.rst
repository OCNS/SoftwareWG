Software WG tutorials at CNS*2021 Online: Bash, Git, and Python
###############################################################
:date: 2021-06-09 10:47:23
:modified: 2021-06-09 10:47:23
:authors: Ankur Sinha
:category: Events
:tags: CNS2021Online, Community, Linux, Python, Software development, Bash, Tutorials, Git, GitHub
:slug: software-wg-tutorials-at-cns-2021-online-bash-git-and-python
:summary: The Software Working Group is holding three beginner level tutorials at the upcoming CNS*2021 Online conference. These will cover using the command line (Bash_), using Git_ and GitHub_, and development in the Python_ programming language.


The Software Working Group is holding three beginner level tutorials at the upcoming CNS*2021 Online conference. These will cover using the command line (Bash_), using Git_ and GitHub_, and development in the Python_ programming language.

To attend these, and other tutorials at `CNS*2021`_, please register for the conference `here <https://www.cnsorg.org/cns-2021-registration-fees>`__.

Effective use of Bash
---------------------

- Instructor(s): Felix B. Kern (`@kernfel <https://github.com/kernfel>`__)
- Date/Time: `28 June, 2021 1200 UTC <https://www.timeanddate.com/worldclock/fixedtime.html?msg=CNS%2A2021%3A+Effective+use+of+Bash&iso=20210628T08&p1=179&ah=3>`__

**Abstract**

The purpose of this tutorial is to introduce participants to the tools they need in order to comfortably and confidently work with a Unix/Linux command line terminal.
Unlike graphical user interfaces, which are often self-explanatory or have obvious built-in help options, the purely text-based nature of a command line terminal can be intimidating and confusing to novice users.
Yet, once mastered, the command line offers more flexibility and smoother workflows for many tasks, while being entirely irreplaceable for things such as cluster access.

In this tutorial, we aim to introduce participants to the concepts and tools they need to confidently operate within a Unix/Linux command line environment.
In particular, the tutorial is developed for Bash (as per the title), which should cover most Linux and MacOS\* use cases.
We hope to provide participants with a firm understanding of the basics of using a shell, as well as an understanding of the advantages of working from a command line.

The tutorial is aimed not only at novices who have rarely or never used a command line, but also at occasional or even regular users of bash who seek to expand or refresh their repertoire of everyday commands and the kinds of quality-of-life tricks and shortcuts that are rarely covered on StackExchange questions.

\* While MacOS has switched from :code:`bash` to :code:`zsh` as its default shell, :code:`zsh`'s operation is sufficiently similar for the purposes of this tutorial.

**Prerequisites**

A working copy of bash; participants on Linux and MacOS are all set.

Participants on Windows have several options to get hold of a bash environment without leaving familiar territory:

* Install `Git for Windows <https://gitforwindows.org/>`__, which includes a Git Bash emulation with most of the standard tools you might expect in a Linux/Unix environment, plus of course Git.
* Alternatively, `enable WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install-win10#install-the-windows-subsystem-for-linux>`__ and `install Ubuntu <https://www.microsoft.com/en-gb/p/ubuntu/9nblggh4msv6>`__ as a virtual machine hosted by Windows. Somewhat ironically, this requires at least one use of a command line terminal (though not bash); on the upside, the Linux-on-Windows experience can be a smooth and safe first step into Linux territory.

**Topics**

* Basics to refer back to: Operating your bash shell (with key bindings and patience)
* The grammar of a shell command line
* Getting around: navigating within and beyond your computer: :code:`~`, :code:`pwd`, :code:`cd`, :code:`pushd`/:code:`popd`, :code:`ssh`
* Seeing what's there: :code:`ls`, globbing, and strategies for naming your files
* File system manipulations: :code:`mv`, :code:`cp`/:code:`scp`, :code:`rm`, :code:`mkdir`, :code:`rmdir`, :code:`ln -s`, :code:`touch`
* Looking into files: :code:`cat`, :code:`head` & :code:`tail`, :code:`more` or :code:`less`, :code:`grep`, :code:`diff`
* Text manipulation: :code:`sed`, :code:`sort`, :code:`uniq`, :code:`cut`, :code:`column`
* Putting things together: piping and redirection
* What to do when stuck: :code:`man`, I need some :code:`help` here :code:`apropos` of this command...


Effective use of Git
---------------------

- Instructor(s): Ankur Sinha (`@sanjayankur31 <https://github.com/sanjayankur31>`__)
- Date/time: `June 28, 2021 1700 UTC <https://www.timeanddate.com/worldclock/fixedtime.html?msg=CNS%2A2021%3A+Effective+use+of+Git&iso=20210628T13&p1=179&ah=3>`__

**Abstract**

Version control is a necessary skill that users writing any amount of code should possess.
Git is a popular version control tool that is used ubiquitously in software development.

This hands-on session is aimed at beginners who have little or no experience with version control systems and Git.
It will introduce the basics of version control and walk through a common daily Git workflow before moving on to show how Git is used for collaborative development on popular Git forges such as GitHub.
Finally, it will show some advanced features of Git that aid in debugging code errors.

**Prerequisites**

The session is intended to be a hands-on session, so all attendees will be expected to run Git commands.
A working installation of Git is, therefore, required for this session.
We will use GitHub as our Git remote for forking and pull/merge requests.
So a GitHub account will also be required.

- Linux users can generally install Git from their default package manager:

  - Fedora::code:`sudo dnf install git`
  - Ubuntu::code:`sudo apt-get install git`

- Windows users should use `Git for Windows <https://gitforwindows.org/>`__.
- MacOS users should use :code:`brew` to install :code:`git`: :code:`brew install git`.

More information on installing Git can be found on the project website: https://git-scm.com/

**Topics**

- a brief introduction to Git

  - references, options
  - where to get help

- using Git on a daily basis:

  - creating a new repository :code:`init`
  - adding files and staging files: :code:`add, add -i`
  - ignoring files: :code:`.gitingore`
  - stashing: :code:`stash`
  - viewing changes: :code:`diff, log`
  - committing files: :code:`commit`
  - using branches to organise the development workflow: :code:`branch, checkout`
  - tagging: :code:`tag`
  - creating an archive: :code:`archive`

- using Git for collaborative development

  - remotes, forks: :code:`remote`
  - pushing and pulling: :code:`push, pull`
  - pull requests and merging: :code:`merge`
  - merge conflicts and resolving them

- slightly advanced git

  - Git worktrees: :code:`worktree`
  - interactive rebasing: :code:`rebase -i`
  - cherry-picking: :code:`cherry-pick`
  - debugging with git-bisect: :code:`bisect`

Python for beginners
---------------------

- Instructors: Joe Graham (`@joewgraham <https://github.com/joewgraham>`__), Shailesh Appukuttan (`@appukuttan-shailesh <https://github.com/appukuttan-shailesh>`__), Ankur Sinha (`@sanjayankur31 <https://github.com/sanjayankur31>`__)
- Date/time: `29 June, 2021 1300 UTC <https://www.timeanddate.com/worldclock/fixedtime.html?msg=CNS%2A2021%3A+Python+for+beginners&iso=20210629T09&p1=179&ah=3>`__


**Abstract**


Python is amongst the most widely used programming languages today, and is increasingly popular in the scientific domain.
A large number of tools and simulators in use currently are either implemented in Python, or offer interfaces for their use via Python.
Python programming is therefore a very sought after skill in the scientific community.

This tutorial is targeted towards people who have some experience with programming languages (e.g. MATLAB, C, C++, etc), but are relatively new to Python.
It is structured to have you quickly up-and-running, giving you a feel of how things work in Python.
We shall begin by demonstrating how to setup and manage virtual environments on your system, to help you keep multiple projects isolated.
We'll show you how to install Python packages in virtual environments and how to manage them.
This will be followed by a quick overview of very basic Python constructs, leading finally to a neuroscience-themed project that will give you the opportunity to bring together various programming concepts with some hands-on practice.


**Prerequisites**

* shell (participants on Linux and MacOS are all set; see below for Windows users)
* Python 3.6.9 or higher (see below for info on installation)

Participants on Windows have several options to get hold of a shell environment without leaving familiar territory:

* Install `Git for Windows <https://gitforwindows.org/>`_, which includes a Git Bash emulation with most of the standard tools you might expect in a Linux/Unix environment, plus of course Git.
* Alternatively, `enable WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install-win10#install-the-windows-subsystem-for-linux>`_ and `install Ubuntu <https://www.microsoft.com/en-gb/p/ubuntu/9nblggh4msv6>`_ as a virtual machine hosted by Windows. This Linux-on-Windows experience can be a smooth and safe first step into Linux territory.

You will find several resources online for info on installing Python. e.g. https://realpython.com/installing-python/


**Topics**

* Setting up and managing virtual environments
* Installing packages using PyPI (:code:`pip`) and from Git repositories (e.g. GitHub)
* Quick Python 101 - lists, dicts, if...else, loops, functions, error handling, import, help, numpy, matplotlib
* Short neuroscience-themed project - modularizing the code
* Good practices - lint (Flake8)


.. _Bash: https://www.gnu.org/software/bash/
.. _Git: https://git-scm.com
.. _GitHub: https://github.com
.. _Python: https://python.org
.. _CNS*2021: https://www.cnsorg.org/cns-2021
