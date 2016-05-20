#!/usr/bin/env python
"""
DIST-LEARN-ADULT Paradigm
Updated Version: May 5, 2016, Kathryn Schuler

OSX Version: 10.10
PsychoPy Version: 1.82.01

Documentation available at: https://github.com/kschuler/dist-learn-adult/wiki
------------------------
"""
# make sure we are using the pygame audio library (because pyo is not supported for OSX 64-bit python)
from psychopy import prefs, gui, core
prefs.general['audioLib'] = ['pygame']

# Before we start the experiment, request user input with dialog box
# setup the parameters you want to collect from the user
EXP_INFO = {
	'exp-id': '0000',
	'subject':'', 				                # subject ID (requests typing)
	'condition': ['A', 'B']   	# list of possible conditions (user selects one or the other)
}
# display a dialog box and wait for user input
if not gui.DlgFromDict(
    EXP_INFO,                                   # the dictionary of experiment information EXP_INFO
    fixed = ['exp-id'],                         # list of which items are fixed (user cannot change)
    order=['exp-id','subject', 'condition']     # list of order you want them to display in
    ).OK:
		core.quit()

# import the psychopy modules we are using
from psychopy import visual, core, event, data, sound
# import datetime, os, sys, itertools

class DistLearnExperiment(object):
    def __init__(self):
        self.expWindow = visual.Window( # psychopy visual.Window()
			units = 'pix',
		 	winType = 'pyglet',
			screen = 0,
			color = 'black',
		 	size = [1440, 900],
			fullscr = True,
			allowGUI = False
		)
        self.expMouse = event.Mouse( # psychopy event.Mouse()
		 	win = self.expWindow,
		 	visible = False
		)
        self.instructions = visual.TextStim( # psychopy visual.TextStim()
			win = self.expWindow,
			pos = [0, 300],
			color = 'white',
			height = 20,
			font = 'Helvetica',
			wrapWidth = 800
		)
        self.progBarOutline = visual.Rect( # psychopy visual.Rect()
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 23,
			lineColor =  'white'
		)
        self.progBar = visual.Rect( # psychopy visual.Rect()
			win = self.expWindow,
			pos = [0, 350],
			width = 680,
			height = 20,
			fillColor = 'gray',
			opacity = 0.8
		)
        self.ratingScale = visual.RatingScale( # psychopy visual.RatingScale()
			win = self.expWindow,
			pos = [0, -150],
			low = 1,
			high = 5,
			precision = 1,
            choices = (1,2,3,4,5),
			textColor = 'white',
			marker = 'triangle',
			size = 1.0,
			stretch = 1.0,
			lineColor = 'white',
			markerColor = 'blue',
			scale = None
		)
    def runExperiment(self):
        #self.displayInstructions('Do this first')
        #self.displayInstructions('Then do this.')
        self.exposurePhase(condFile = EXP_INFO['condition']+'-exposure.csv', reps = 1)

    def setupExperiment(self):
        pass

    def displayInstructions(self, theseInstructs):
        self.instructions.setText(theseInstructs)
        self.instructions.draw()
        self.expWindow.flip()
        event.waitKeys('space')

    def exposurePhase(self, condFile = None, reps = 1):
		# test has rating, exposure has break
        self.generateDisplay()
        self.conditionsFile = data.importConditions('conditions/'+condFile)
        self.trials = data.TrialHandler(self.conditionsFile, method = 'sequential', nReps = reps, extraInfo = EXP_INFO)
        for trial in self.trials :
            thisSequence = [trial.A]
            for item in thisSequence:
                self.playSound(whichSound='sounds/'+str(item)+'.wav', ISI = 0.50)
			# core.wait(0) # uncomment to add silence between trials (in addition to ISI after each sound) replace 0 with amount of time
            if event.getKeys(['escape']): core.quit()
        self.trials.saveAsWideText(thisPhase+'datafile.csv', delim=",")

    def testPhase(self, condFile = None, reps = 1):
		# test has rating, exposure has break
        self.generateDisplay()
        self.conditionsFile = data.importConditions('conditions/'+condFile)
        self.trials = data.TrialHandler(self.conditionsFile, method = 'sequential', nReps = reps, extraInfo = EXP_INFO)
        for trial in self.trials :
            # fix filter NA for future
            thisSequence = [trial.A]
            for item in thisSequence:
                self.playSound(whichSound='sounds/'+str(item)+'.wav', ISI = 0.50)
            if thisPhase == 'test':
                rating = self.collectRating()
                self.trials.addData('rating', rating)
            if event.getKeys(['escape']): core.quit()
        self.trials.saveAsWideText(thisPhase+'datafile.csv', delim=",")

    def generateDisplay(self, drawList = None):
        if drawList :
            for item in drawList :
                item.draw()
        self.expWindow.flip()

    def playSound(self, whichSound, waitDur = True, ISI = 0.0, whatVolume = 1.0):
        thisSound = sound.Sound(whichSound)
        thisSound.setVolume(whatVolume)
        thisSound.play()
        dur = thisSound.getDuration()
        if waitDur :
            core.wait(dur)
        core.wait(ISI)

    def collectRating(self, instructs = None):
        self.ratingScale.reset()
        while self.ratingScale.noResponse:
            self.ratingScale.draw()
            # if instructs :
            #     self.expText.setText(instructs)
            #     self.expText.draw()
            self.expWindow.flip()
            if event.getKeys(['escape']): core.quit()
        self.expWindow.flip()
        return self.ratingScale.getRating()

exp = DistLearnExperiment()
exp.runExperiment()
