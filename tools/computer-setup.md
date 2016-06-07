
# Setting up a computer

These instructions are for setting up a lab computer (OS X) to run one of my experiments.  To set up a computer to run one of my experiments, start at the top with [install required software](#install-required-software).  To adapt one of my experiments for your own use, skip install required software and start with [get Miniconda](#get-miniconda).

- [Install required software](#install-required-software)
- [Get Miniconda](#get-miniconda)
- [Get PsychoPy and required packages](#get-psychopy-and-required-packages)

## Install required software
Check to make sure the computer you are using has (at least) Audacity and Dropbox. Make sure Dropbox has been configured with the lab login information (ask Sarah for this information if you need it).  If the computer is missing either of these programs, please download them.

*  **[Audacity][1]**  - download and install
*  **[Dropbox][2]** - download and install (and configure with lab login)

## Get Miniconda
[Miniconda][3] is Anaconda’s minimalist python distribution.  I prefer it to full Anaconda because it is much smaller and it doesn’t come with so many unnecessary packages (that I never use).  

First, check to make sure miniconda is not already installed
```bash
conda info

```
If you get information about the current conda install, you can skip to [Get PsychoPy & required packages](#get-psychopy-required-packages).  If you get a notice `-bash: conda: command not found`, then proceed with installing miniconda.

Download latest distribution of miniconda for OSX (64-bit is the only option)
```bash
curl -O https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh  
```
and install it
```bash
bash Miniconda2-latest-MacOSX-x86_64.sh  
```

You'll be asked a few questions.  You want to answer 'yes' to all of them, and press Enter whenever it prompts you to.

To start using miniconda, close and then reopen the terminal.
Check that miniconda is installed
```bash
conda info
```

And make sure miniconda has added itself to your path to become your default python.

```bash
which python
```

Now make sure everything is up to date
```bash
conda update conda
```

Great! Now you can start using conda.  You can check what packages are already installed with
```bash
conda list
```

And you can see what environments you have with
```bash
conda env list
```

For more information on how to use conda, refer to the official conda documentation.

## Get PsychoPy and required packages

### PsychoPy

Now that you have miniconda, you can use it to get psychopy and its dependencies.  You can get the version of psychopy that works for my experiments by using my conda recipe.  My recipe depends on a number of other packages from the anaconda channel `http://conda.anaconda.org/erik`.  First add this channel to your conda configuration.
```
conda config --add channels http://conda.anaconda.org/erik
```
Next you can install psychopy and its dependencies from my recipe.
```
conda install -c kschuler psychopy=1.82.01
```

This will install almost all the packages required by psychopy (and my experiments).  Answer yes to all the questions and press Enter when required.  It will take a long time.

### Pygame
In order for my experiments to play sound, you need to install Pygame and the packages it requires.  To do this, we first want to get the packages pygame requires.  Install homebrew to get these packages ([why?](https://groups.google.com/forum/#!topic/psychopy-dev/dratQzqNJ-k)).

Make sure you have xcode-select installed
```
xcode-select –install
```
Then install homebrew
```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

and install the pygame dependencies with it
```bash
brew install sdl sdl_ttf sdl_image sdl_mixer portmidi
```

Now you can install the OSX-friendly version of pygame.  Make sure you do this part exactly - other conda recipes for pygame my not build properly on OSX.
```bash
conda install anaconda-client
```
```bash
conda install -c https://conda.binstar.org/quasiben pygame
```

### Pyglet
The last package to install is pyglet (used for presenting visual stimuli).  To make sure we get the right version, we want to create our conda environment first, and then install the package into it.
Create a conda envirnoment called kschuler with pyschopy and pygame.
```bash
conda create -n kschuler psychopy pygame
```

Then you can navigate into this environment with conda
```bash
source activate psychopyenv
```

and use pip to install pyglet
```bash
pip install pyglet
```

You should be all set to [run my experiments](../current/how-to-run.md) on your computer.


[1]:	http://www.audacityteam.org/download/mac/
[2]:	https://www.dropbox.com/
[3]:	http://conda.pydata.org/docs/install/quick.html
