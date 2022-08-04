Title: Advance preparation for laptops
date: 2017-07-01 07:51
slug: preparation
Authors: Peter Elmer
Summary: Advance preparation for laptops
Template: page

Most of the exercises to be performed during the school are intended to be done on
public cloud resources (Binder, Google Colab) as recommended by the instructors. But the
exercises can be also be done on personal laptops with suitable preparation.

Also, some of the exercises require downloading, compiling, and running files, either
directly on the personal laptops of the participants, or on resources that may be available
at the participants' home institutions and can be accessed remotely through laptops. In order
to do the exercises directly on personal laptops, certain tools (compilers, etc.)
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

Apple's Xcode is required in order to compile anything on macOS, even if you use conda.
Xcode is a free (if slow) download from the App Store.

If you are already familiar with a package manager like MacPorts or Homebrew,
use that to install the requirements. Otherwise, we highly recommend Homebrew;
please visit [https://brew.sh/](https://brew.sh/) and see the post ["Setup a new Mac"](https://iscinumpy.gitlab.io/post/setup-a-new-mac/)
to learn about it. To install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

If Apple's Xcode Command Line Tools weren't previously installed, then the
Homebrew installation should have taken care of that for you as well.

**Install a recent C/C++ compiler.** The default Apple system compiler (clang) does not support OpenMP out of the box, which is
used in some lectures, so please also install the GNU Compiler Collection
(GCC), version >= 4.8.

In the terminal, these are the commands to install GCC in Homebrew:
    
```bash
brew install gcc
```

The default version of GCC installed by Homebrew is currently gcc-11. Thus the
correct command to use for calling the C/C++ compiler is `gcc-11` or `c++-11`. These commands
are located in /usr/local/bin, which should be in your PATH. (Be aware that
macOS has similar commands called `gcc` and `c++` in /usr/bin, but `gcc` is just
clang in a `gcc` emulation mode, while `c++` is a symlink to `clang++`.)

## Linux

**Make sure you have a GNU C/C++ compiler** >= 4.8 installed.

## Windows

Windows 10 -- set up a Linux shell with [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/), [install git](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git), then follow Linux instructions.

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

Then compile and run the file as follows (you may need to substitute `gcc-11` as your compiler name in macOS, see above):

```bash
gcc -fopenmp -o omptest; ./omptest
```

The output should contain one occurrence of "Hello world" for each virtual core in your system.

## Setup instructions for the ML tutorial

The machine learning tutorial will use Google Colab.
Detailed setup instructions can be found [here](https://github.com/savvy379/codashep_ml_2022/#readme).
