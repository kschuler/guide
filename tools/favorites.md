# Favorite tools for common tasks

These are my favorite tools for common lab-related tasks.  Some links say "lab members only". You must request my permission for access to those links.

## Documentation

* [**GitHub / git **][2] : for version control and hosting repositories
*  [**mkdocs**][3] : python library for writing documentation in markdown
*  [**gitbooks**](https://www.gitbook.com) : for writing documentation in markdown (this site was built with it!)

## Making stimuli

See [the guidelines](../guidelines/making-stimuli.md) for how to make stimuli for one of my experiments.

### Artificial Languages
* **artificial languages from past experiments**
	* [ **stimuli/languages** (lab members only)](): repository of past artificial languages.
* **making artificial languages**
	* **white board / excel workbook**:  there is really no substitute for doing this by hand.
	* **a friend (or 3)**: to double check your work!

### Sounds
* **sound files from past experiments**
	* [**stimuli/sounds** (lab members only)](): repository of sound files used in my experiments.
* **recording sound files**
	* **Marantz PMD671** (professional quality): located in BldgD 145-D. [manual](../static/manuals/marantz-pmd671.pdf) | [lab instructions](../guidelines/making-stimuli.md#how-to-record-sounds)
	* **USB microphone** (in a pinch): we have a few of [these](http://www.amazon.com/dp/B0012AUHXW/ref=pd_lpo_sbs_dp_ss_1/182-9815211-7619413?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=lpo-top-stripe-1&pf_rd_r=12J1B313G5HCXKNAAGGQ&pf_rd_t=201&pf_rd_p=1944687542&pf_rd_i=B001R76D42) and they are actually not terrible.  
* **synthesizing sound files: **
	* [**Mac Text-to-Speech**](../guidelines/making-stimuli.md#how-to-synthesize-sounds): using the terminal command `say`
		* [**Acapela**][9]: natural sounding child and adult voices in many languages
		* borrow my synthesizing scripts: [synth-a-little.py](https://raw.githubusercontent.com/kschuler/helpers/master/synth-a-little.py) | [synth-a-lot.py]()
*  **editing sound files**
	* [**Audacity**][12]: works well for the editing I need. [Here is the manual.][13]
	* [**Praat**][14]: people who do phonetics and phonology stuff like Praat. [Here is a nice tutorial.][15]

### Images
* **image files from past experiments**
	* [**stimuli/images** (lab members only)]: repository of image files used in my experiments. (lab members only)
* **finding image stimuli** (open-source)
	* **[freepik][17]**: free photos and vector graphics, searchable by category
	* **[Vecteezy][18]**: free vector graphics, searchable by category
	* [**Glitch the game**][19]: art from a game that was released for public use.
	* [**Open Game Art**][20]: a very large collection of open source game art  
	* [**Cog-sci stimuli sets**][21]: a nice list of standardized stimuli others have used (by Sebastian Mathôt)  
*  **editing images**
	* **[Inkscape][22]**: a free, open-source version of Adobe Illustrator.  [Inkscape tutorials][23]
	* **[Gimp][24]**: an free, open-source version of Photoshop. [Gimp tutorials][25]

### Videos
* **video files from past experiments**
	* [**stimuli/videos** (lab members only) ][26]: repository of image files used in my experiments.
* **making video stimuli**
	* I haven’t done this in years, but whenever people do, they usually use the resources in [Ted’s lab][27].  (ask Lissa)
	* **[Cog-sci stimuli sets][28] **: mostly images, but a few standardized video stimuli sets (by Sebastian Mathôt)
* **editing videos**
	* **[Quicktime][29]**: for very quick and simple edits. [manuals for older Quicktime versions][30]
	* **[iMovie][31]**: for slightly more complex edits. [iMovie manual][32]
	* **[HandBrake][33]**: for when you need to convert video formats. [HandBrake wiki][34]

## Creating experiments
### with Applications (no code required)
* **[PsychoPy Standalone App ][35]**
	* this one is my favorite  - it is actively developed and there is a great community of contributors
		* **builder tutorials** : [here ][36]is a tutorial for making a stroop task, and [here][37] is one I made for language tasks
		* [**psychopy-users**][38] : google group where you can find answers and ask questions
* **[OpenSesame][39]**
	* I haven’t used it, but some people I know really like it.
		* **tutorials:** [here][40] is the main tutorial and here are [some examples][41].

### with Code \(python)
I love python, so my favorite experiment coding resources are all python-based.  [Matlab][42] is also very good - if you prefer matlab, be sure to check out the [psychtoolbox][43] for creating experiments.

* ** Learning python**
	* [**Learn python the hard way**][44]: free self-paced course for learning python (how I first learned!)
	* [**Treehouse python track**][45]:  good video courses that are easy to follow and understand.
* **Good text editors**
	*  **[Atom][46]** : my current favorite - free and great interaction with GitHub with [git-plus][47] package
	* **[Text-wrangler][48]** : my oldest friend - still great and free
	* **[Sublime Text][49]** : widely loved - free if you don’t mind occasional pop-ups asking you to buy it.
* **Creating lab experiments**
	* [**anaconda (miniconda)  OSX**][50]: free python distribution for managing packages and environments.
	*  **[PsychoPy ][51]**: python package for creating psych experiments (I'm a huge fan).
		* **[and friends][52] **: PsychoPy relies on lots of other packages (like [pygame][53] and [pyglet][54])
	* see [my instructions][55] for setting up a computer with miniconda, psychopy and its dependencies.
* **Creating mechanical turk experiments**
	* **[Digital Ocean][56]**: build and maintain linux servers with simple/intuitive interface
	* [**anaconda (miniconda) Linux**][57]: free python distribution for managing packages and environments.
	* **[psiTurk][58]** : great python package for creating and deploying mechanical turk experiments
	* see [my instructions][55] for setting up a server on digital ocean and installing miniconda and psiturk.

## Data analysis & visualization
* **Analysis**
  *  [**Jupyter notebook**](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html): dynamic report generation (similar concept to [knitr](http://yihui.name/knitr/) R package)
  * [**Pandas**](http://pandas.pydata.org/): python library for data analysis and data structures
  * [**R-Studio**](https://www.rstudio.com/): user-interface for R 
* **Visualization**
  * [**Seaborn**](https://web.stanford.edu/~mwaskom/software/seaborn/): data visualization library for python
  * [**ggplot2**](http://ggplot2.org/): data visualization package for R


## Publishing & presenting
There are lots and lots of great tools for publishing and presenting your work.  In my opinion, the very best tools are the ones that make it easy for you to work collaboratively with your advisor (and colleagues).  My advisor likes to work in Microsoft Office, so for me, that is the most efficient option. All of my final versions of things are done in Word and Powerpoint.   (And remember, it is really about delivering the content! The tool itself is whatever helps you do that best.)  

With that said, here are some tools you might find useful:

* **bibliography management**
	* [**BibDesk**](http://bibdesk.sourceforge.net/) : the one I use because it is simple and I always have.  
	* there are many others (also good) - [Zotero](https://www.zotero.org/), [Papers](http://papersapp.com/), [Mendeley](https://www.mendeley.com), etc..
* **writing papers**
	* [**Ulysses**](http://www.ulyssesapp.com/): writing in Markdown (not free, but so worth it)
	* [**Dillinger**](http://dillinger.io/): writing in Markdown (what I used before [Heidi](https://heidigetz.com/) told me about Ulysses)
	* [**LaTex**](https://www.sharelatex.com/): A great tool if you have self-control (I find it too tempting to spend hours on formatting)
* **making presentations**
	* [**Remark.js**](http://remarkjs.com/) : a free javascript library for writing presentations in Markdown
	* [**Deckset**](http://www.decksetapp.com/) : a (not free) app for writing presentations in Markdown.
	* [**Beamer**](https://www.sharelatex.com/learn/Beamer) : A LaTex class for presentations (also requires self-control)
	* [**Slidify**](http://slidify.org/) : Write slides in R markdown
* **making posters**
	* [**Inkscape**][22] : a free version of Illustrator


[1]:	../guidelines/documenting-exps.md
[2]:	https://github.com/kschuler
[3]:	https://github.com/mkdocs/mkdocs
[4]:	analyzing-data.md#guidelines
[6]:	https://github.com/kschuler/lab-docs/tree/master/stimuli/sounds
[7]:	manuals/marantz-pmd671.pdf
[9]:	http://www.acapela-group.com/acapela-for-osx/
[10]:	https://www.dropbox.com/s/8wqcmw6u6dk0x7q/synth-words.py?dl=0
[11]:	https://www.dropbox.com/s/8wqcmw6u6dk0x7q/synth-words.py?dl=0
[12]:	http://www.audacityteam.org/
[13]:	http://manual.audacityteam.org/
[14]:	http://www.fon.hum.uva.nl/praat/
[15]:	http://savethevowels.org/praat/
[16]:	https://github.com/kschuler/lab-docs/tree/master/stimuli/images
[17]:	http://www.freepik.com/free-vectors/graphics
[18]:	http://www.vecteezy.com/
[19]:	https://www.glitchthegame.com/public-domain-game-art/
[20]:	http://opengameart.org/
[21]:	http://www.cogsci.nl/stimulus-sets
[22]:	https://inkscape.org/en/
[23]:	https://inkscape.org/en/learn/
[24]:	https://www.gimp.org/
[25]:	https://www.gimp.org/tutorials/
[26]:	https://github.com/kschuler/lab-docs/tree/master/stimuli/videos
[27]:	https://cbpr.georgetown.edu/faculty/ted_supalla
[28]:	http://www.cogsci.nl/stimulus-sets
[29]:	https://support.apple.com/en-us/HT201066
[30]:	https://support.apple.com/en_US/manuals/quicktime
[31]:	http://www.apple.com/mac/imovie/
[32]:	http://help.apple.com/imovie/mac/10.1/
[33]:	https://handbrake.fr/
[34]:	https://trac.handbrake.fr/wiki/HandBrakeGuide
[35]:	http://www.psychopy.org/
[36]:	https://www.youtube.com/watch?v=VV6qhuQgsiI
[37]:	https://www.youtube.com/watch?v=WKJBbVnQkj0
[38]:	https://groups.google.com/forum/#!forum/psychopy-users
[39]:	http://osdoc.cogsci.nl/
[40]:	https://www.youtube.com/watch?time_continue=118&v=eiGXe-t-C28
[41]:	https://github.com/smathot/OpenSesame/tree/ising/extensions/example_experiments/examples
[42]:	http://www.mathworks.com/products/matlab/?requestedDomain=www.mathworks.com
[43]:	http://psychtoolbox.org/
[44]:	http://learnpythonthehardway.org/
[45]:	https://teamtreehouse.com/tracks/learn-python
[46]:	https://atom.io/
[47]:	https://github.com/akonwi/git-plus
[48]:	http://www.barebones.com/products/textwrangler/
[49]:	https://www.sublimetext.com/
[50]:	https://www.continuum.io/
[51]:	http://www.psychopy.org/installation.html
[52]:	http://www.psychopy.org/installation.html#dependencies
[53]:	http://www.pygame.org/hifi.html
[54]:	https://bitbucket.org/pyglet/pyglet/wiki/Home
[55]:	../tools/computer-setup.md
[56]:	https://www.digitalocean.com/
[57]:	http://conda.pydata.org/miniconda.html
[58]:	https://psiturk.org/
