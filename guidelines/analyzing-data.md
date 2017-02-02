# Analyzing data 

>Note that this is the current method used to analyze data (from July 2016 onward).

I analyze my data using an [R Notebook](http://rmarkdown.rstudio.com/). An R Notebook is an R Markdown document that contains executable code along with text and figures. [Here](https://www.dropbox.com/home/Research/summaries?preview=0010-srt-pilot.html) is an example of one of my analysis notebooks.

- [Getting started](#getting-started)
- [Analysis notebook boilerplate and conventions](#analysis-notebook-conventions)
- [Default data cleaning and exclusion criteria](#default-data-cleaning-and-exclusion-criteria)
- [Default analysis strategies](#default-analysis-strategies)


## Getting started

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

## Analysis notebook boilerplate and conventions

All analysis notebooks follow the same basic format, with each section containing the same information.  Click on each link below to see details about each section.

- Header content
- Introduction
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

Next I include a little bit of background information about the logistics of the study.  This includes collaborators, research assistants, and lab managers involved; when the data was collected; and where the experiment is reported (or planned to be reported).  Here is an example:

>This experiment was conducted by Kathryn Schuler (graduate student) and Elissa Newport (advisor) and was based on a theory and computational model proposed by Charles Yang (U. Penn) and the declarative-procedural memory circuit framework proposed by Michael Ullman (Georgetown University). The lab manager at the time of running was Jaclyn Horowitz and the research assistant involved in this project was Gabriella Iskin (undergraduate RA).  The data was collected at Georgetown University from November 11, 2016 to ONGOING.

>- This experiment was reported in:
    - nothing, yet.
- And is planned to be reported in:
    - 2017 - Katie's job talk at Penn
    - 2017 - Katie's dissertation

#### Introduction
#### Materials and Method
#### Results and analysis
#### Conclusions
#### Next steps
#### Important files





## Default data cleaning and exclusion criteria
## Default analysis strategies

