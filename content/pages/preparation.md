Title: Laptop Software Environment
date: 2017-07-01 07:51
slug: preparation
Authors: Peter Elmer
Summary: Laptop Softwre Environment - 2025 Version
Template: page

  Most exercises during the school can be performed on the provided (hosted)
Binderhub resources (Kaggle, etc.). The Binderhub will be available for
a period after the school. We will not have a large GPU reservation at that 
point, but it should often be able to get a GPU. You can also get access
to hosted resources after the school via [Google Colab](https://colab.research.google.com).

  For many purposes, it can also be useful to set up a software environment
on your laptop. A common way to do this is by installing [Conda](https://www.anaconda.com/download/success) and use that to install various software configurations. On that page you will see "Distribution Installers" and "Miniconda Installers". Most people will want to install the "Miniconda" option it is more lightweight for laptop purposes.

  Once you have installed Conda, you can use that to install specific
software configurations (combinations of packages that have been 
curated by somone with the correct versions for a given purpose).
These are typically provided as "environment.yml" files (or similar names).
For example the environments provided for the CoDaS-HEP 2025 school
were:

  * [Python environment](https://github.com/iris-hep/codas-hep-2025/blob/python/binder/environment.yml)
  * [ML environment](https://github.com/iris-hep/codas-hep-2025/blob/ml/binder/environment.yml)
  * [GPU environment](https://github.com/iris-hep/codas-hep-2025/blob/gpu/binder/environment.yml)  ## Requires a machine with a GPU

Note that each environmnet.yml file has a "name" inside that you can change.
Conda allows you to have multiple environments installed on your laptop
with different names.

One you have an environment.yml file, and Conda set up, you can tell Conda
to download all of the relevant packages and create an environment with
the specified name:

```
conda env create --file environment.yml
```

Once an environment has been created (with relevant software packages downloaded and installed) some useful conda commands include:

  * conda activate [name-of-environment]   # setup a given environment in your shell
  * conda deactivate  # deactivate a given environment in a shell
  * conda env list    # show list of available/installed laptops
  * conda list    # (Once an enviroment is activated) show list of packages/versions in the current activated environment


You can also launch a local JupyterLab that uses that software environment
by first activating the desired environment in a shell and then launching
JupyterLab with:

```
jupyter lab
```
