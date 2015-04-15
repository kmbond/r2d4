#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import pandas as pd
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'test_mri'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(500, 500), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'The experiment will begin in 5 seconds. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image = visual.ImageStim(win=win, name='image',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[200,200],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

fixation = visual.ShapeStim(win,
    vertices=((0, -0.2), (0, 0.2), (0,0), (-0.2,0), (0.2, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor='white')

Wrong_1 = visual.TextStim(win=win, ori=0, name='Right_1',
    text='X',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-6.0)


# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'End of Experiment',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(text_2)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED



#######################
#### Set up onsets ####
#######################
corr_thresh = 0.1
dfStims = pd.DataFrame
sequence_img_ids = []
img_dict = {2: 'image_folder/stim_2.png', 3: 'image_folder/stim_3.png', 4: 'image_folder/stim_4.png', 5: 'image_folder/stim_5.png'}
key_dict = {2:'2', 3:'3', 4:'4', 5:'5'}

isDone = 0
while not isDone:
    trial_types = np.asarray([2, 3, 4, 5])
    trial_IDs = np.asarray(range(4))
    trial_freq = np.asarray([12, 12, 12, 12])
    iti_range = np.asarray([2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8])

    n_post = 3
    t_vec = []
    iti_vec = []
    tid_vec = []

    for tt in range(0,len(trial_types)):
        t_vec = np.repeat(trial_types,12)
        iti_vec = np.tile(iti_range,4)

    np.random.shuffle(t_vec)
    np.random.shuffle(iti_vec)
    vec = [0]
    id_vec = vec

    for t in range(0, len(t_vec)):
        vec = vec + [t_vec[t]] +  np.repeat(0,iti_vec[t]).tolist()
    vec = vec + [0,0,0]
    dfStims = pd.DataFrame()

    X = np.zeros((len(vec),len(trial_types)))
    ons = np.zeros((12,4))
    for c in trial_types:
        a = np.where(vec==c)[0]

        ons[:,c-2] = a +1
        for indx in range(0, len(a)):
            name = a[indx]
            X[a[indx]][c-2]= 1


    df=pd.DataFrame(X)
    cxy = df.corr()
    cxy = abs(np.tril(cxy, k=-1))

    if cxy.max() < corr_thresh:
        isDone = 1

for x in range(0,len(vec)):
    if vec[x] == 0:
        sequence_img_ids.append('image_folder/skip.png')
    elif vec[x] != 0:
        sequence_img_ids.append(img_dict[vec[x]])

dfStims['trial_img'] = sequence_img_ids
dfStims['trial_ans'] = vec


#######################
## End Set up onsets ##
#######################

filename = _thisDir + os.sep + 'data/%s_%s_MRI_Onsets_%s' %(expInfo['participant'], expName, expInfo['session'])
np.savetxt(filename, ons, '%5.2f',delimiter=",")
dfStims.to_csv('MRI_onsets.csv', index= False)



#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_2.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'/Users/plb/r2d4/MRI_onsets.csv'),
    seed=None, name='trials')


thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:

    ##### Wait for scanner trigger key #####
    #event.waitKeys(keyList=['t'])
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)


    ##### Wait for scanner trigger key #####
    event.waitKeys(keyList=['t'])
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if trial_img != 'image_folder/skip.png':
        image.setImage(trial_img)
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(image)
        trialComponents.append(key_resp_2)
        trialComponents.append(Wrong_1)
        trialComponents.append(fixation)

        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            fixation.setAutoDraw(True)
            win.flip()
            # *image* updates
            if t >= .5 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            if image.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                image.setAutoDraw(False)

            # *key_resp_2* updates
            if t >= .5 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['2', '3', '4', '5'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str(trial_ans)) or (key_resp_2.keys == trial_ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
           key_resp_2.keys=None
           # was no response the correct answer?!
           if str(trial_ans).lower() == 'none': key_resp_2.corr = 1  # correct non-response
           else: key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        trials.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.nextEntry()
        win.flip()
    elif trial_img == 'image_folder/skip.png':
        fixation.setAutoDraw(True)
        win.flip()
        core.wait(0.5)
        win.flip
    thisExp.nextEntry()


# completed 1 repeats of 'trials'


#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(text)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
