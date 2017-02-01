# How to run current experiments
Instructions to run all current experiments are below.  

## For most experiments
The preferred method for running most experiments is to use the psychopy package from within [Atom](https://atom.io/packages/psychopy).  Unless otherwise specified, all lab experiments can be run using this method.

The following studies require special methods (click to view these methods):
- [0035-babysaffran-srt-patient](#0035-babysaffran-srt-patient)

### Follow these steps
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
