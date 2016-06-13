# How to run current experiments
Instructions to run all current experiments are below.  If the experiment you are running is not listed please [email me](mailto:kathryn.schuler@gmail.com) and remind me to update it.

- [0104-inconinput-1day-pluralmorph-6733-training](#0104-inconinput-1day-pluralmorph-6733-training)
- [0164-empiricalyang-9noun-mfrule-tophalf-child](#0164-empiricalyang-9noun-mfrule-tophalf-child)
- [0400-condvar-exp1-purevcond](#0400-condvar-exp1-purevcond)
- [0035-babysaffran-srt-patient](#0035-babysaffran-srt-patient)

## For most experiments
The preferred method for running most experiments is to use the psychopy package from within atom.  Each of the experiments listed below can be run in this way.
###### 0104-inconinput-1day-pluralmorph-6733-training
###### 0164-empiricalyang-9noun-mfrule-tophalf-child
###### 0400-condvar-exp1-purevcond

##### Before running
- Open the [0104 subject tracking sheet](https://www.dropbox.com/s/jdwwu7qh79skru6/0104-inconinput-1day-pluralmorph-6733-training-track.xlsx?dl=0)
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
- Record responses on 0104 data sheet

##### After running
- Exit my conda environment with `source deactivate`
- Copy participant data to [0104 raw-data folder](https://www.dropbox.com/sh/tcji2vfs64bp5pg/AAAHdrlhoIuujxG1aYWrq3c5a?dl=0)
- Fill in final columns of [0104 subject tracking sheet](https://www.dropbox.com/s/jdwwu7qh79skru6/0104-inconinput-1day-pluralmorph-6733-training-track.xlsx?dl=0)




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
