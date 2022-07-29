Title: Advance preparation for laptops
date: 2017-07-01 07:51
slug: preparation.html
Authors: Peter Elmer
Summary: Advance preparation for laptops
Template: page

In order to perform the exercises during the school, we will provide 
login access for school participants on machines in one of the Princeton 
clusters as well as other resources.

Most exercises can also be easily executed on the personal laptops of
the participants, provided that certain tools (compilers, etc.) are 
installed in advance. This page describes how to install the appropriate
software versions, as well as how to perform simple tests to verify that a
laptop installation works correctly.

## GitHub account

All participants should have a GitHub account.

## Anaconda

The Python and most ROOT portions of the workshop can be run in Conda, which you can obtain here: [miniconda](https://docs.conda.io/en/latest/miniconda.html) or here: [Anaconda](https://www.anaconda.com/distribution/#download-section). We will provided suggested environment files, so miniconda is fine unless you already have Anaconda. You can always write `conda install anaconda` to install the rest of the Anaconda default package collection if you really want to. We will be using the `conda-forge` and `pytorch` channels. The ROOT sections will not work on Conda on Windows.

## macOS

Apple's Xcode is required in order to run ROOT and to compile anything on macOS, even if you use conda.
Xcode is a free (if slow) download from the App Store.

If you are already familiar with a package manager like MacPorts or Homebrew,
use that to install the requirements. Otherwise, we highly recommend Homebrew;
get from [https://brew.sh/](https://brew.sh/), and see the post ["Setup a new Mac"](https://iscinumpy.gitlab.io/post/setup-a-new-mac/). To install Homebrew:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


If Apple's Xcode Command Line Tools weren't previously installed, then the
Homebrew installation should have taken care of that for you as well.

**Install a recent version of ROOT.** The offical ROOT binaries are available from [https://root.cern.ch/content/release-61800](https://root.cern.ch/content/release-61800), but they have some issues, such as being compiled against the system Python 2 and with the minimum C++ standard setting (11). If you use Homebrew to install ROOT, you will get a highest C++ standard setting allowed by your macOS version and Python 3 as well.

Alternatively, you can [use conda to install ROOT](https://github.com/conda-forge/root-feedstock) if you are on a Linux or macOS install of Conda (Conda on Windows is 64 bit, and ROOT 6 does not support 64 bit binaries on windows).

```bash
brew install root
```

**Install a recent C++ compiler.** The default Apple system compiler (clang) does not support OpenMP out of the box, which is
used in some lectures, so please also install the GNU Compiler Collection
(GCC), version >= 4.8.

In the terminal, these are the commands to install GCC in homebrew:
    
```bash
brew install gcc
```

The default version of gcc installed by Homebrew is currently gcc-9. Thus the
correct command to use for calling the c++ compiler is c++-9. These commands
are located in /usr/local/bin, which should be in your PATH. (Be aware that
macOS has similar commands called gcc and c++ in /usr/bin, but gcc is just
clang in a GCC 4.2 emulation mode, while c++ is a symlink to clang++.)

## Linux

**Install a recent version of ROOT**, for example from [https://root.cern.ch/content/release-61800](https://root.cern.ch/content/release-61800). You can use conda and the conda-forge ROOT install as well;
unlike on macOS, these come with recent GCC compilers instead of LLVM, so you will likely have everything you need.

**Make sure you have GNU c++ compiler** >= 4.8 installed.

## Windows

Windows10 -- setup Linux shell, then follow Linux instructions.

## Testing ROOT Installation

```bash
# Setup root environment in bash shell (skip this if using conda)
source <path-to-root>/bin/thisroot.sh

# Run a quick test
root -l $ROOTSYS/tutorials/hsimple.C
```
    
## Testing gcc / make for Thursday session on vectorization

```bash
git clone https://github.com/osschar/mtorture.git
cd mtorture
# For macOS, modify Makefile to set CXX to your c++
# e.g., for Homebrew, this should be enough: CXX := c++-9
make t1
./t1
```

This should print out about 30 lines of numbers.


