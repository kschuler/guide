
# Data Day!  (Number 1)



- [The evolution of experiments](#The-evolution-of-experiments)
    - The importance of planning ahead and the "test" analysis
- [The jupyter notebook](#The-Jupyter-Notebook)
    - What it is and why I use it
    - How to install and launch a jupyter notebook
    - Tour of jupyter features
    - The R kernel in jupyter

- [Analysis style guide](#Analysis-style-guide)
    - [For documentation (Katie's method)](#For-documentation)
    - [For R code](#For-R-code)

- [Intro to my favorite packages](#Intro-to-my-favorite-packages)
    - [magrittr (pipe!)](#magrittr-the-%>%)
    - [dplyr](#dplyr)
    - [ggplot2](#ggplot2)


## The evolution of experiments
- The importance of "test" analysis
- [example 0164](https://mammothhq.com/boards/156832-empirical-yang)

## The Jupyter Notebook

- Demo; You'll need:
    - Internet (Saxanet with your netID and password)
    - terminal
    - [guide.kathrynschuler.com](https://guide.kathrynschuler.com)

## Analysis style guide

### For documentation
##### Naming files
- lowercase with dash between words
- each folder has it's own naming convention
- always starts with EXPID number
```
0104-inconinput-1day-pluralmorph-6733-training-analysis
```

##### The notebook / summary
- Tour of analysis template notebook for production /rating data
- Required fields and how to add analysis to it
- Saving a `summary` file (.html)

### For R code

- [The style I follow](http://adv-r.had.co.nz/Style.html) (with some modifications) and why you should, too

#### Style


##### Naming variables
- ALLUPPERCASE uppercase words, underscore between words; concise and meaninful 
- avoid existing function names
```
PROD_DATA
PROD_PLOT
RATE_DATA
RATE_PLOT
```

##### Spacing
- space around all operators (=, +, -, <=)
- space after but not before commas (like regular english)
```
average <- mean(feet / 12 + inches, na.rm = TRUE)
```
- the exception is `:`, `::`, and `:::` (no spaces there)
```
x <- 1:10
dplyr::bind_rows
```

- before paratheses, except in a function
```
if (debug) do(x)
plot(x,y)
```

- add spaces if they make it prettier (better alignment)
```
list(
  total =  a + b + c,
  mean  = (a + b + c) / n
)
```
- no spaces in parentheses or sqare brackets
```
if (debug) do(x)
diamonds[5, ]
```


##### Curly braces

- Open curly braces should never go on their own line and should always be followed by a new line
- Closing curly braces should always go on their own lines (unless they are followed by else)

```
if (y < 0) {
  message("Y is negative")
}

if (y == 0) {
  log(x)
} else {
  y ^ x
}
```

##### Indentation
- Always use two space to indent code (never tabs)
- Except if you have a super long function; then indent to the functions definition
```
long_function <- function(a = "one arg",
                          b = "another arg",
                          c = "a third arg") {
}
```

##### Assignment
- Use `<-` not `=` for assignment
```
x <- 5
```

##### Commenting
- Comments explain the why, NOT the what
- Comments should begin with comment symbol (#) followed by a space
```
# Eliminate outliers
```

- Use commented lines of `-` to break up your file into chunks if you need to 
```
# Load data ----------------------------
```

##### Calling functions
Use double colons to clarify function provenance
```
dplyr::filter()
```

#### Data format
- all data relevant files `subject-tracking`, `raw-data`, and `processed-data` should be `.csv` files.
- all data relevant files should be tidy (`tidyr` can help you if it isn't)
    - each variable forms a column
    - each observation forms a row
    - each type of observational unit forms a table
    
- all files should be read in with `readr` using `readr::read_csv()`
    - and the `stringsAsFactors` argument should be set to `TRUE`

#### Piping

Consecutive commands should be chained together with `magrittr` pipe (`%>%`).  This makes things more readable and avoids creating new variables.

#### Visualization

- Use `ggplot2` for visualization.  
- All plots use the theme `ggplot2::theme_classic()`.
- All plots are saved with EXPID number and a human readable description to the FIGUREPATH
```
ggplot2::ggsave('0104-production-barplot.png')
```

## Intro to my favorite packages

### `magrittr ` the `%>%`
Magrittr is about creating pipelines!  You can write nested functions as a pipeline instead.  This is a neat trick because (1) it is easier to read (especially when your functions have arguments).


```R
# get the numbers 1 through 10, take the sqrt, take the log of that, and take the mean of that
# notice that the arguments are really far away from the function names
mean(sqrt(log(1:10, base=2)), trim=0.1)
```




1.49909140226409




```R
# load the dplyr package
library(dplyr)
```


```R
# try it with pipe!  (args are now really close to the functions)
# this is much more readable
1:10 %>% 
    log(base=2) %>% 
    sqrt() %>%
    mean(trim=0.1)
```




1.49909140226409



And it (2) saves computing power


```R
# you'll see lots of code that saves dataframes and then manipulates the next one
# piping lets you pass the output of one function as the first argument of the next
# and doesn't save additional dataframes to your computers memory.  This makes things work faster
```

###  `dplyr` 
#### grammar for data manipulation
- [`select()`](http://www.rdocumentation.org/packages/dplyr/functions/select) - removes columns
- [`filter()`](http://www.rdocumentation.org/packages/dplyr/functions/filter) - removes rows
- [`arrange()`](http://www.rdocumentation.org/packages/dplyr/functions/filter) - reorders rows
- [`mutate()`](http://www.rdocumentation.org/packages/dplyr/functions/mutate) - uses data to build new columns of values
- [`summarize()`](http://www.rdocumentation.org/packages/dplyr/functions/summarise) - calculates summary statistics

###  `ggplot2`
#### grammar for data visualization

- essential elements (layers)
    - data - the dataset being plotted
    - aesthetics - the scales onto which we map our data
    - geomteries - the visual element used for our data
- other elements (layers)
    - facets - plotting small multiples
    - statistics - representaitons of our data to aid understanding
    - coordinates - the space on which the data will be plotted
    - themes - all non-data ink
