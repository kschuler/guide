# How to run current experiments

- [Instructions for running (most) experiments](#instructions-for-running-experiments)
  - [Good experiment hygiene](#good-experiment-hygiene)
  - [Running experiments](#running-experiments)
  - [Troubleshooting](#troubleshooting)
- [Special exceptions](#special-exceptions)

## Instructions for running experiments
The preferred method for running most experiments is to use the psychopy package from within [Atom](https://atom.io/packages/psychopy).  Unless otherwise specified, all lab experiments can be run using this method.

The following studies require special methods (click to view these methods):
- [0035-babysaffran-srt-patient](#0035-babysaffran-srt-patient)

### Good experiment hygiene
1. Make sure the experiment has been throughly tested on the computer you are using.
2. Before running an experiment
  - Turn off the internet
  - Ensure all applications are closed (nothing is running)
  - Turn off Dropbox syncing
  - Make sure you are running the correct experiment
3. After running an experiment
  - Turn on the internet
  - Turn on Dropbox syncing
  - Make sure the data you have collected syncs to Dropbox
  - Turn the computer off completely (end of day)

### Running experiments
In general, follow these steps when running an experiment.  These steps are auxillary to the lab's subject running checklists linked here.
- [subject running checklist for kids](https://www.dropbox.com/s/j8w62vo4umn8yrr/LDL%20Checklist%20-%20Running%20Kids.docx?dl=0)
- [subject running checklist for adults](https://www.dropbox.com/s/lokr1wa93d069h8/LDL%20Checklist%20-%20Running%20Adults.docx?dl=0)

##### Before the subject arrives:
- Get subject and condition information from subject tracking sheet.
-  Setup the experiment with [Atom](https://atom.io/packages/psychopy). ([silent video demonstration below](#how-to-setup-the-experiment-with-atom))
- Make sure you are ready to record the complete study with Audacity

##### While you are running the subject:
- Read all instructions to participant and offer a sticker at all breaks
-  Make sure you record participant responses on the written data sheet

##### After the subject leaves:
-  Copy participant to raw-data folder and update subject-tracking sheet
- Export the Audacity recording as .wav and save in the raw-data folder as:
  - **STUDYID-SUBJECTID-audio.wav**
  - e.g. 0164-S24-audio.wav.
-  Scan any physical data sheets and save to raw-data folder as:
  - **STUDYID-SUBJECTID-data-sheet.pdf**
  - e.g. 0164-S24-data-sheet.pdf

##### How to setup the experiment with Atom

[![Running experiments with atom (silent video demo)](http://img.youtube.com/vi/tSyBMPg3bsQ/0.jpg)](https://www.youtube.com/watch?v=tSyBMPg3bsQ)

---

### Troubleshooting

**"I ran the study in ATOM and I got an error message"**

> **Solution 1: Has the experiment been tested on this exact computer?**
  If no, the experiment is unlikely to work.  One thing you can try is to make sure Dropbox has updated (or "synced").  If you think this is the issue, you should always run the study through as a test BEFORE testing any additional subjects.  It is not guaranteed that this will fix your problem.  You need to test all conditions of the experiment on the computer you intend to use to guarantee it will work.
  
> **Solution 2: Was ATOM properly shut down before you opened your new experiment?**
Atom will cache experiment folders that are left open.  This can lead to error messages in subsequent experiments in which PsychoPy is unable to find files (like images, sounds, or conditions files).  Shutting down ATOM completely and reopening it fresh with your experiment is likely to solve this issue.



---
## Special exceptions
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
