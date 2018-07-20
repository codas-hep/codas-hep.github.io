Title: Advance preparation for laptops
date: 2017-07-01 07:51
slug: preparation.html
Authors: Peter Elmer
Summary: Advance preparation for laptops
Template: page

### Advance preparation for laptops

  In order to perform the exercises during the school, we will provide 
login access for school participants on machines in one of the Princeton 
clusters as well as in the Microsoft Azure Cloud.

  Some exercises can also be easily executed on the personal laptop of
the participants, however certain tools (compilers, etc.) must be 
installed in advance. This page describes how to install appropriate
versions as well as simple tests to 

## MacOSX

Install ROOT from https://root.cern.ch/content/release-61002

Install GNU c++ compiler >= 4.8. If you already use MacPorts or Homebrew, use that.

Otherwise installing Homebrew seems easier, see https://brew.sh/.

Apparently (maybe g++):

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install gcc

## Linux

Install ROOT from https://root.cern.ch/content/release-61002

Make sure you have GNU c++ compiler >= 4.8 installed.

## Windows

Windows10 -- setup Linux shell, then follow Linux instructions.

## Testing ROOT Installation

    # Setup root environment
    # e.g. for bash: . path-to-root/bin/thisroot.sh
    cd $ROOTSYS/tutorials
    root -l hsimple.C
    
## Testing gcc / make for Thursday session on vectorization

    git clone git@github.com:osschar/mtorture.git
    cd mtorture
    # For osx, modify Makefile to set CXX to your gcc
    # In principle, this should be enough: CXX := c++-mp-5
    make t1
    ./t1
    # should print out about 30 lines of numbers 
