# How to run current experiments
Instructions to run all current experiments are below.  If the experiment you are running is not listed please [email me](mailto:kathryn.schuler@gmail.com) and remind me to update it.

- [0104-inconinput-1day-pluralmorph-6733-training](#0104-inconinput-1day-pluralmorph-6733-training)
- [0164-empiricalyang-9noun-mfrule-tophalf-child](#0164-empiricalyang-9noun-mfrule-tophalf-child)
- [0400-condvar-exp1-pureincon](#0400-condvar-exp1-pureincon)
- [0302-hierarchical-srt-thompsonnewport-nocue](#0302-hierarchical-srt-thompsonnewport-nocue)
- [0035-babysaffran-srt-patient](#0035-babysaffran-srt-patient)

### 0104-inconinput-1day-pluralmorph-6733-training
##### Before running
- Open the [0104 subject tracking sheet](https://www.dropbox.com/s/twajhafd1wr8r64/0104-inconinput-1day-pluralmorph-6733-training-track.csv?dl=0)
  - fill in participant information
  - get subject id number (SID) and condition
- Setup the experiment
  - In terminal, navigate to the experiment `cd ~/Dropbox/Kschuler-current/experiments/0104-inconinput-1day-pluralmorph-6733-training-exp`
  - Enter my conda environment with `source activate kschuler`
- Start the experiment
  - Type `pythonw run-exp.py`
  - Enter requested information 

##### During running
- Read all on-screen instructions to participant
- Offer a sticker at each break
- Record responses on [0104 data sheet](https://www.dropbox.com/s/rbcvs9ak21dmu15/0164-empericalyang-9noun-mfrule-tophalf-child-data-sheet.docx?dl=0)

##### After running
- Exit my conda environment with `source deactivate`
- Copy participant data to [0164 raw-data folder](https://www.dropbox.com/sh/ne3y6a280gwqvqb/AABVJX9J-izvHfLeF13FXZLGa?dl=0)
- Fill in final columns of [0164 subject tracking sheet](https://www.dropbox.com/s/mtp8m18hzwu0k4v/0164-empiricalyang-9noun-mfrule-tophalf-child-track.csv?dl=0)


### 0164-empiricalyang-9noun-mfrule-tophalf-child

##### Before running
- Open the [0164 subject tracking sheet](https://www.dropbox.com/s/mtp8m18hzwu0k4v/0164-empiricalyang-9noun-mfrule-tophalf-child-track.csv?dl=0)
  - fill in participant information
  - get subject id number (SID) and condition
- Setup the experiment
  - In terminal, navigate to the experiment `cd ~/Dropbox/Kschuler-current/experiments/0164-empericalyang-9noun-mfrule-tophalf-child-exp`
  - Enter my conda environment with `source activate kschuler`
- Start the experiment
  - Type `pythonw run-exp.py`
  - Enter requested information 

##### During running
- Read all on-screen instructions to participant
- Offer a sticker at each break
- Record responses on [0164 data sheet](https://www.dropbox.com/s/rbcvs9ak21dmu15/0164-empericalyang-9noun-mfrule-tophalf-child-data-sheet.docx?dl=0)

##### After running
- Exit my conda environment with `source deactivate`
- Copy participant data to [0164 raw-data folder](https://www.dropbox.com/sh/ne3y6a280gwqvqb/AABVJX9J-izvHfLeF13FXZLGa?dl=0)
- Fill in final columns of [0164 subject tracking sheet](https://www.dropbox.com/s/mtp8m18hzwu0k4v/0164-empiricalyang-9noun-mfrule-tophalf-child-track.csv?dl=0)

### 0400-condvar-exp1-pureincon
##### Before running
- Open the [0400 subject tracking sheet]()
  - fill in participant information
  - get subject id number (SID) and condition
- Setup the experiment
  - In terminal, navigate to the experiment `cd ~/Dropbox/Kschuler-current/experiments/0400-condvar-exp1-pureincon-exp`
  - Enter my conda environment with `source activate kschuler`
- Start the experiment
  - Type `pythonw run-exp.py`
  - Enter requested information (select correct day 1 or 2)

##### During running
- Read all on-screen instructions to participant
- Offer a sticker at each break
- Record responses on [0400 data sheet]()

##### After running
- Exit my conda environment with `source deactivate`
- Copy participant data to [0400 raw-data folder]()
- Fill in final columns of [0400 subject tracking sheet]()

### 0302-hierarchical-srt-thompsonnewport-nocue
##### Before running
- Open the [0302 subject tracking sheet]()
  - fill in participant information
  - get subject id number (SID) and condition
- Setup the experiment
  - In terminal, navigate to the experiment `cd ~/Dropbox/Kschuler-current/experiments/0302-hierarchical-srt-thompsonnewport-nocue-exp`
  - Enter my conda environment with `source activate kschuler`
- Start the experiment
  - Type `pythonw run-exp.py`
  - Enter requested information 

##### During running
- Read all on-screen instructions to participant

##### After running
- Exit my conda environment with `source deactivate`
- Copy participant data to [0302 raw-data folder]()
- Fill in final columns of [0302 subject tracking sheet]()

### 0035-babysaffran-srt-patient
##### Before running
- Open the [0035 subject tracking sheet]()
  - fill in participant information
  - get subject id number (SID) and condition
- Setup the experiment
  - In terminal, navigate to the experiment `cd ~/Dropbox/Kschuler-current/experiments/0035-babysaffran-srt-patient-exp`
  - Start in terminal (depending on condition)
    - Lang A Test A: `python 0035_langA_testA.py`
    - Lang A Test B: `python 0035_langA_testB.py`
    - Lang B Test A: `python 0035_langB_testA.py`
    - Lang B Test B: `python 0035_langB_testB.py`
  - Enter requested information 

##### During running
- Read all on-screen instructions to participant

##### After running
- Copy participant data to [0035 raw-data folder]()
- Fill in final columns of [0035 subject tracking sheet]()
