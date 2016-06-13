# How to run current experiments
Instructions to run all current experiments are below.  If the experiment you are running is not listed please [email me](mailto:kathryn.schuler@gmail.com) and remind me to update it.



## For most experiments
The preferred method for running most experiments is to use the psychopy package from within atom.  The following experiments can be run using this method.
- [0104-inconinput-1day-pluralmorph-6733-training](https://www.dropbox.com/sh/shsocn1wmsurzc7/AAAkqM7ausOZJVn4b7C4iBaZa?dl=0)
- [0164-empiricalyang-9noun-mfrule-tophalf-child](https://www.dropbox.com/sh/8es4zzff09f245q/AADTMm_qAixYBfUHes61yTraa?dl=0)
- [0400-condvar-exp1-purevcond](https://www.dropbox.com/sh/8jlpkr4chowqjj8/AAB8wzYZvBg-eIOjVIYEaBiNa?dl=0)

But see these instructions for running 0035 (Mackenzie)
- [0035-babysaffran-srt-patient](#0035-babysaffran-srt-patient)

In general, follow these steps when running an experiment:
###### Before the subject arrives:
1. Get subject and condition information from subject tracking sheet.
2. Setup the experiment with [Atom](https://atom.io/packages/psychopy). (video instructions below)

###### While you are running the subject:
3. Read all instructions to participant and offer a sticker at all breaks
4. Make sure you record participant responses on the written data sheet

###### After the subject leaves:
5. Copy participant to raw-data folder and update subject-tracking sheet

[![Running experiments with atom](http://img.youtube.com/vi/v=tSyBMPg3bsQ/0.jpg)](https://www.youtube.com/watch?v=tSyBMPg3bsQ)

---

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
