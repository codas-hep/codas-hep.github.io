Title: Advance preparation for laptops
date: 2017-07-01 07:51
slug: preparation.html
Authors: Peter Elmer
Summary: Advance preparation for laptops
Template: page

### Advance preparation for laptops

  In order to perform the exercises during the school, we will provide 
login access for school participants on machines in one of the Princeton 
clusters as well as other resources.

  Some exercises can also be easily executed on the personal laptops of
the participants, provided that certain tools (compilers, etc.) are 
installed in advance. This page describes how to install the appropriate
software versions, as well as how to perform simple tests to verify that a
laptop installation works correctly.

## macOS

Install a recent version of ROOT, for example from [https://root.cern.ch/content/release-61400](https://root.cern.ch/content/release-61400).

Apple's Xcode is required in order to run ROOT, assuming that you installed
ROOT from one of CERN's binary distributions for Mac. Xcode is a free (if slow)
download from the App Store.

The default Apple system compiler (clang) does not support OpenMP, which is
used in some lectures, so please also install the GNU Compiler Collection
(GCC), version >= 4.8.

If you are already familiar with a package manager like MacPorts or Homebrew,
use that to install GCC. Otherwise, getting started with Homebrew seems
easiest; see [https://brew.sh/](https://brew.sh/).

In Terminal, these are the commands to install Homebrew, then GCC:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install gcc

If Apple's Xcode Command Line Tools weren't previously installed, then the
Homebrew installation should have taken care of that for you as well.

The default version of gcc installed by Homebrew is currently gcc-8. Thus the
correct command to use for calling the c++ compiler is c++-8. These commands
are located in /usr/local/bin, which should be in your PATH. (Be aware that
macOS has similar commands called gcc and c++ in /usr/bin, but gcc is just a
minor variant of clang, while c++ is a symlink to clang++.)

## Linux

Install a recent version of ROOT, for example from [https://root.cern.ch/content/release-61400](https://root.cern.ch/content/release-61400)

Make sure you have GNU c++ compiler >= 4.8 installed.

## Windows

Windows10 -- setup Linux shell, then follow Linux instructions.

## Testing ROOT Installation

    # Setup root environment in bash shell
    source <path-to-root>/bin/thisroot.sh
    # Run a quick test
    root -l $ROOTSYS/tutorials/hsimple.C
    
## Testing gcc / make for Thursday session on vectorization

    git clone https://github.com/osschar/mtorture.git
    cd mtorture
    # For macOS, modify Makefile to set CXX to your c++
    # e.g., for Homebrew, this should be enough: CXX := c++-8
    make t1
    ./t1
    # should print out about 30 lines of numbers 
