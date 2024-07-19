Title: Advance preparation for laptops
date: 2017-07-01 07:51
slug: preparation
Authors: Peter Elmer
Summary: Advance preparation for laptops
Template: page

Most of the exercises to be performed during the school are intended to be done on
cloud-based resources (e.g., the SSL BinderHub at U. of Chicago) as recommended by the instructors. But the
exercises can be also be done on personal laptops with suitable preparation.

Also, some of the exercises require downloading, compiling, and running files,
either directly on the personal laptops of participants, or on other resources that
are available and can be accessed remotely through laptops. In order
to do the exercises directly on a personal laptop, certain tools (compilers, etc.)
must be installed in advance. This page describes how to install the appropriate
software versions, as well as how to perform simple tests to verify that a
laptop installation works correctly.

## Git & GitHub

* All participants should have a GitHub account. It's free.
* Please create a SSH key pair and add it to your GitHub account. This is required
  in order to push local changes to a GitHub repository.
  For this, please follow the [instructions from GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)
  (note that you can select your operating system on the top).
* While we try to repeat the basics, some familiarity with git is recommended.
  A good starting point (aimed at complete beginners) is for example [this tutorial](https://swcarpentry.github.io/git-novice/).
* If you have learned about git previously,
  how about taking a look at [a git cheat sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf) to refresh your knowledge?

## conda & Anaconda

The Python portions of the workshop can be run in a local conda environment. You can obtain [miniconda](https://docs.conda.io/en/latest/miniconda.html) or
[Anaconda](https://www.anaconda.com/distribution/#download-section) for this purpose. We will provided suggested environment files, so miniconda is fine unless you already have the Anaconda Python distribution. You can always type `conda install anaconda` to install the rest of the Anaconda default package collection if you really want to. We will be using the `conda-forge` and `pytorch` channels.

## macOS

The Terminal app provides you with a Unix shell, either bash or zsh, as well as many command-line tools.
Much of what you will need (apart from miniconda) seems to be preinstalled on the latest M1-, M2-, and
M3-based Macs with macOS Sonoma.

For installing the other requirements, we highly recommend the Homebrew package manager.
(If you are already familiar with MacPorts, you can use it instead.) Learn more about Homebrew at
[https://brew.sh/](https://brew.sh/). To install it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Be sure to follow the instructions in the output to add Homebrew's path to your shell environment.

If Apple's Xcode Command Line Tools weren't previously installed (and if your Mac needs them),
then the Homebrew installation should have taken care of that for you as well. You may also
find that Apple's full Xcode distribution is required in order to build codes successfully
on macOS, even if you use conda and Homebrew. Xcode is a free (if slow) download from the App Store.

**Now, install a recent C/C++ compiler, or at least an OpenMP library.** The default Apple system
compiler (clang) does not support OpenMP out of the box, which is used in some lectures. One way
to overcome this problem is to install the GNU Compiler Collection (GCC), version >= 4.8.

In the terminal, these are the commands to install GCC in Homebrew:
    
```bash
brew install gcc
```

The default version of GCC installed by Homebrew is currently gcc-14. Thus the
correct command to use for calling the C/C++ compiler is `gcc-14` or `c++-14`. These commands
are located in /usr/local/bin, which should be in your PATH. (Be aware that
macOS Sonoma has similar, built-in commands called `gcc` and `c++` in /usr/bin, but all such
commands are straight-up copies of `clang`. Similarly, in earlier versions of macOS, `gcc`
is just Clang in an emulation mode, while `c++` is a symlink to `clang++`.)

For those who would prefer to do the exercises with Apple Clang, instructions on how to install
and use a compatible OpenMP library are [here](https://iscinumpy.dev/post/omp-on-high-sierra/).
Again, Homebrew is a very convenient source for obtaining the necessary software. If you are
interested in enhancing your Homebrew installation with other useful tools, see the post
["Setup a new Mac"](https://iscinumpy.gitlab.io/post/setup-a-new-mac/) or
["Setup an Apple Silicon Mac"](https://iscinumpy.gitlab.io/post/setup-apple-silicon/) for
suggestions.

## Linux

**Make sure you have a GNU C/C++ compiler** >= 4.8 installed.

## Windows

Windows 10 and 11 -- set up a Linux shell with [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/), [install git](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git), then follow Linux instructions.

## Compiler test

Edit a file containing the following C program. Call it omptest.c:

```
#include <omp.h>
#include <stdio.h>

void main () {
    #pragma omp parallel
    {
        printf("Hello world\n");
    }
}
```

Then compile and run the file as follows (you may need to substitute `gcc-14` as your compiler name in macOS, see above):

```bash
gcc -fopenmp -o omptest; ./omptest
```

The output should contain one occurrence of "Hello world" for each virtual core in your system.

## Setup instructions for the ML tutorial

The machine learning tutorial will use the SSL BinderHub at U. of Chicago.
Detailed setup instructions will be presented during the school.
