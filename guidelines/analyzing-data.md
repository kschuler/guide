# Analyzing data 

UNDER CONSTRUCTION

>Note that this is the current method used to analyze data (from July 2016 onward).

I analyze my data using an [R Notebook](http://rmarkdown.rstudio.com/). An R Notebook is an R Markdown document that contains executable code along with text and figures. [Here](https://www.dropbox.com/home/Research/summaries?preview=0010-srt-pilot.html) is an example of one of my analysis notebooks.

I also perform some statistical analyses using SPSS, particularly repeated-measures ANOVAs.  Instructions for doing so can also be found below. 

- [Analyzing data in an R Notebook](#analyzing-data-in-an-r-notebook)
    - [Getting started](#getting-started)
    - [Analysis notebook boilerplate and conventions](#analysis-notebook-conventions)
    - [Default data cleaning and exclusion criteria](#default-data-cleaning-and-exclusion-criteria)
    - [Default analysis strategies](#default-analysis-strategies)
- [Analyzing data in SPSS](#analyzing-data-in-spss)
    - [T-tests](#t-tests)
    - [Repeated-measures ANOVA](#repeated-measures-ANOVA)


## Analyzing data in an R Notebook
### Getting started

A good place to start is reading this nice paper about how to do good things with your data and analyses. I follow this rules in my own research, and it is a nice way of understanding why we do things the way we do them.

- [Read **Ten Simple Rules for Effective Statistical Practice**](https://www.dropbox.com/s/v1u7r3ul0e6ur2b/2016-ten-simple-rules-stats.pdf?dl=0)

If you are absolutely new to the idea of R and/or Markdown, start here:

- [Complete this Markdown tutorial (~ 10 minutes)](http://www.markdowntutorial.com)
- [Complete this basic R tutorial (~ 20-30 minutes)](http://tryr.codeschool.com)

If you already know the basics of R but want to learn some intermediate skills, the following courses from DataCamp would provide you with enough information to do basic data manipulation and visualization.  Ask Katie for the lab login for DataCamp if you are interested.  I'd recommend doing them in this order:

1. [Cleaning data in R (with tidyr package)](https://www.datacamp.com/courses/cleaning-data-in-r)
2. [Data manipulation in R with dplyr](https://www.datacamp.com/courses/dplyr-data-manipulation-r-tutorial)
3. [Joining data in R with dplyr](https://www.datacamp.com/courses/joining-data-in-r-with-dplyr)
4. [Data visualization with ggplot2 (part 1)](https://www.datacamp.com/courses/data-visualization-with-ggplot2-1)
5. [Data visualization with ggplot2 (part 2)](https://www.datacamp.com/courses/data-visualization-with-ggplot2-2)
6. [Reporting with R Markdown](https://www.datacamp.com/courses/reporting-with-r-markdown)

Finally, when you are ready to get started you can install R studio. (Lab computers should already have this installed, but you may need to updated to version 1.0 or higher to use R notebooks).

- [Install R Studio](https://www.rstudio.com/products/rstudio/download/)

### Analysis notebook boilerplate and conventions

All analysis notebooks follow the same basic format, with each section containing the same information. This information allows the notebook to stand alone as a full summary of the experiment and ensure that all experiments contain all of the important information.  The final experiment notebook will be published in my [lab notebook](http://kathrynschuler.com/labnotebook) repository. Click on each link below to see details about each section.

- [Header content](#header-content)
- [Introduction](#introduction)
- Materials and Method
    - Subjects
    - Materials
    - Procedure
- Results and analysis
    - Preregistration
    - Participants
    - Data type 1
    - Data type 2
- Conclusions
- Next steps
- Important files

#### Header content

All R notebook files are `.Rmd` format and have a header of `.yaml` information that is used to format the notebook, including the title, author, and date.  The title should always be the experiment name - `EXPID-collection-descriptive-experiment-title` - and the author and the data should be formatted as follows.  The date should be updated each time you make changes to the notebook.

```yaml
title: "0167-empiricalyang-9noun-hfrule-adults-fastproduction"
author: "Kathryn Schuler"
date: "last updated 2017-02-01"
output: 
  html_document:
    theme: default
    toc: TRUE
    toc_float: FALSE
    toc_depth: 2
```

To initiate the R notebook and setup some options, the following code is required after the header information above.

```R
{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, warning = FALSE)
```

Next I include a little bit of background information about the logistics of the study.  This includes collaborators, research assistants, and lab managers involved; when the data was collected; and where the experiment is reported (or planned to be reported).  Here is an example:

>This experiment was conducted by Kathryn Schuler (graduate student) and Elissa Newport (advisor) and was based on a theory and computational model proposed by Charles Yang (U. Penn) and the declarative-procedural memory circuit framework proposed by Michael Ullman (Georgetown University). The lab manager at the time of running was Jaclyn Horowitz and the research assistant involved in this project was Gabriella Iskin (undergraduate RA).  The data was collected at Georgetown University from November 11, 2016 to ONGOING.

>- This experiment was reported in:
    - nothing, yet.
- And is planned to be reported in:
    - 2017 - Katie's job talk at Penn
    - 2017 - Katie's dissertation

#### Introduction

In the introduction, I provide a little bit of informal rational as to why we conducted this experiment. This should be no more than a few paragraphs.  The primary purpose of this section is so that I remember the circumstances that lead us to run the experiment.  Here is an example:

>### Introduction

>This experiment was run based on a suggestion from Michael Ullman in Katie's dissertation committee meeting (suggested July 2016).  In our original Tolerance Principle work we found that TP predicts categorically when children will form productive rules but not when adults will adults.  Adults instead matched the token frequency of the regular form in thier input (exactly as they had done in our inconsistent input work).  We had discussed how we might force adults to behave like kids.  We tried a series of experiments on mechanical turk in which the language was much more complex (a la Hudson-Kam & Newport, 2009) and we found that adults continued to match the token frequency. In some conversations with Michael, we discussed the evidence for the role of the declarative (hippoampal) and procedural (basal ganglia) memory circuits in storing exceptions and forming rules. And further that adults learn second languages via declariative memory.  This lead to the hypothesis that if we could prevent adults from accessing their declarative memory circuit, they would be forced to rely on the procedural circuit as children may do.  A quick way to ask that was to force adults to respond very quickly, as the retrieval from declarative memory is hypothesized to take longer.

>Here we re-ran our original Tolerance Principle experiment, except we gave adults a strict time limit of 1.5 seconds in which to produce sentences in the production test. After 1.5 seconds, the screen would turn red and participants would hear a beep. To encourge them to comply, they were told they would recieve a $0.50 bonus for every sentence they could complete before the screen turned red and the computer beeped.

#### Materials and Method

In the Materials and Method section, I include information about the materials and methods use in the experiment. This is divided into the sub-sections: Subjects, Materials, and Procedure.

##### Subjects

Here I describe the subjects include how many were run, how many were excluded and why, and how they were recruited and reimbursed. Here is an example:

>### Subjects
- Adults:
    - 21 adults recruited at Georgetown University (13 female)
    - additional 2 excluded for failing to complete the study (2 male)
    - native English speakers (but multilingual permitted)
    - compensated $15.00 ($10.00 with a $5.00 bonus)

##### Materials

Here I describe the materials that were used in the experiment, including equipment, models, languages, and stimuli lists.  Note that the funny text is latex math notation (rendered by R markdown). Here is an example:

>#### Equipment
  - Hardware: 
      - Macbook Air (OSX) 
      - Sennheiser HD555 open-air headphones
      - Internal microphone of Macbook Air
  - Software: Python, PsychoPy 
      - Note: Audacity used for some recordings as PsychoPy's microphone API unreliable

>#### Model
  - The Tolerance Principle (Yang, 2016)
  - Learners will form a productive rule wheh it is more computationally efficient
  - Let R be a rule that is applicable to N items, of which e are exceptions.  R is productive iff:
       - $\textrm{e} \leq \theta_{N} \quad \textrm{where} \quad \theta_{N} := \frac{N}{ln(N)}$

>#### Language
- 15 total nouns: 
    - 9 familiar: `mawg`, `tombur`, `glim`, `zup`, `spad`, `daygin`, `flairb`, `clidam`, `lapal`
    - 6 novel: `bleggin`, `daffin`, `norg`, `sep`, `flugit`, `geed` 
- 1 verb: `gentif` (means "there is" or "there are")
- 7 plural markers: 
    - 1 regular form: `ka` (applied to most frequent nouns)
    - 6 exceptions: `po`, `lee`, `bae`, `tay`, `muy`, `woo`
- Sentences constructed:
    - Singular: `V` + `N` + `null` (e.g. `gentif mawg`)
    - Plural: `V` + `N` + `MARKER` (e.g. `gentif mawg ka`)
- Conditions:
     - Compute the threshold for forming a productive rule by the Tolerance Principle (for our 9 nouns):
        -  $\textrm{e} \leq \theta_{9}  \quad \textrm{where} \quad  \theta_{9} := \frac{9}{ln(9)} = 4.096$
        - Thus, can tolerate 4 exceptions to the rule (regular form), but not 5 or more.
    - 5R4E Exposure: 5 most frequent types take the regular form `ka` and 4 remaining types take exceptions.
        - Language A: Noun rank in Zipfian distribution is as listed above (`mawg` is most frequent)
        - Language B: Noun rank is reversed (`lapal` is most frequent)
    - 3R6E Exposure: 3 most frequent types take the regular form `ka` and 6 remaining types take exceptions.
        - Language A: Noun rank in Zipfian distribution is as listed above (`mawg` is most frequent)
        - Language B: Noun rank is reversed (`lapal` is most frequent)

>#### Stimuli
- Images of "toasters" and pre-recorded words (adult female voice)
    - Mechanical turk version uses written sentences
- Exposure set: 
    - 72 total sentences paired with corresponding picture
    - each noun is paired with a specific plural marker (see [Language](#language))
    - 1/3 of presentations were singular and 2/3 plural for each noun
    - plurals appeared in groups of 2, 4, or 6
    - Zipfian distribution
- Production test set:
    - All novel nouns presented twice: `bleggin`, `daffin`, `norg`, `sep`, `flugit`, `geed`
    - plurals appeared in groups of 3 or 5
- Rating test set:
    - All 9 familiar nouns presented 4 times in 2AFC
        - paired with four different incorrect plural markers


##### Procedure

Here I describe the procedure that were used in the experiment, including all phases of the experiment. Here is an example:



>### Procedure
- Exposure: 
    - see a picture and hear the sentence that goes with the picture
    - repeat the sentence
    - break every 18 trials (for sticker)
- Production test:
    - modeled after wug test (Berko, 1958)
    - see a singular picture and hear corresponding sentence
    - participant asked to produce plural sentence for same noun
    - importantly, adults are given a 1.5 second time limit
        - hear a beep and box on screen turns red to indicate end of time limit
        - told they will get a 50 cent bonus for every trial on which they can produced within the time limit
- Rating test:
    - 2AFC test in which there is a child in a purple shirt and a child in a green shirt on the screen. 
    - A test image appears in the box and the two cartoon children take turns producing a sentence to match the picture.
    - participants must decide which child said the sentences correctly in silly speak


#### Results and analysis




#### Conclusions
#### Next steps
#### Important files





## Default data cleaning and exclusion criteria

### Exclusion criteria

We exclude participants who:

- Did not meet inclusion criteria (e.g. age, language experience, normal to corrected-to-normal hearing/vision, wrong-handed, participated in similar experiment within the last 3 months)
- Did not complete the study
- Experienced equipment malfunction during experiment
- Did not produce the noun correctly on >50% of trials in production tests
    - for experiments in which the noun is given; indicates they did not understand the task
- Chose the same value on all but 2 trials on Rating tests
    - indicates they did not understand the task

We exclude trials on which:

- For production tests:
    - The participant did not produce the noun correctly on production tests
        - no way to know they were paying attention to the trial
    - participant was prompted for the noun or plural marker by researcher (verb prompt ok)
        - research assistants are instructed not to prompt participants for noun or plural marker
- For rating tests:
    - participant provided no rating
- For SRT data:
    - 

### Data cleaning

- 

### Default analysis strategies

## Analyzing data in SPSS

### T-tests

Coming soon...

### Repeated measures ANOVAs

Coming soon...

