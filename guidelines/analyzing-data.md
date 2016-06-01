
# Analyzing data

I analyze my data with an R kernel in [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html).  A Jupyter notebooks is a document that contains executable code along with text and figures. [Here](https://www.dropbox.com/home/Research/summaries?preview=0010-srt-pilot.html) is an example of one of my analysis notebooks.

## Setup Jupyter notebook

Before you can analyze data, you must install the jupyter notebook. You can do this with `conda`. The computer you are using should already be setup with miniconda. You can check whether the computer has miniconda by going to the terminal and typing the following:
```
conda info
```

If you get information about the current conda install, you can proceed. If you get a notice `-bash: conda: command not found`, visit [setting up a computer](tools/computer-setup.md) for instructions on installing miniconda before you proceed.


First we are going to create a conda enviroment for the Jupyter notebook with the packages required to run the R kernel.  We will name the package jupyter.
```
conda create -n jupyter -c r r-essentials
```

Next we navigate to the new conda environment
```
source activate jupyter
```

And install jupyter into that environment
```
conda install jupyter
```



3. 1. make sure miniconda is installed
2. get r-essentials



