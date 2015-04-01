#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'testing_r2d4'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
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
win = visual.Window(size=[1440, 900], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True
    )
win.waitBlanking=False
#Add context
context = visual.Rect(win, width=1, height=1, autoDraw = True, lineColor='black', lineWidth = 6)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'In this experiment, you will see an image displayed on the screen. \nThis image corresponds to a specific finger movement. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()

image = visual.ImageStim(win=win, name='image', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[128,128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Feedback
practiceFeedback = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'Press the space bar to continue. \n',    font=u'Arial',
    pos=[0, -.6], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)



# This feedback puts a small red x underneath the stimulus
# Right_1 = visual.TextStim(win=win, ori=0, name='Right_1',
#     text='X',    font='Arial',
#     pos=[0, -.3], height=0.1, wrapWidth=None,
#     color='green', colorSpace='rgb', opacity=1,
#     depth=-6.0)


Wrong_1 = visual.Circle(win=win, units = 'pix', radius = 100,lineColor='red', fillColor = 'red')



# Initialize components for Routine "Begin_Blocks"
Begin_BlocksClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'End of practice rounds. Press any key to continue. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Block"
BlockClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[200,200],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'End of Block. Press any key to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "End_Experiment"
End_ExperimentClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Experiment is completed. Thank you for your participation.\n',    font=u'Arial',
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
# update component parameters for each repeat
instructions_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
instructions_response.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instrText)
InstructionsComponents.append(instructions_response)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)

    # *instructions_response* updates
    if t >= 0.0 and instructions_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_response.tStart = t  # underestimates by a little under one frame
        instructions_response.frameNStart = frameN  # exact frame index
        instructions_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instructions_response.status == STARTED:
        theseKeys = event.getKeys()

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

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
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=3, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'test_stim.csv'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop.keys():
        exec(paramName + '= thisPractice_loop.' + paramName)

for thisPractice_loop in practice_loop:

    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop.keys():
            exec(paramName + '= thisPractice_loop.' + paramName)

    #------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()
    routineTimer.add(10)  # clock

    frameN = -1
    # update component parameters for each repeat
    image.setImage(img_id)
    Practice_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Practice_response.status = NOT_STARTED
    # keep track of which components have finished
    practiceComponents = []
    practiceComponents.append(image)
    practiceComponents.append(Practice_response)
    practiceComponents.append(Wrong_1)
    practiceComponents.append(practiceFeedback)

    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "practice"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if t >= .25 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)

        # *Practice_response* updates
        if t >= .25 and Practice_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Practice_response.tStart = t  # underestimates by a little under one frame
            Practice_response.frameNStart = frameN  # exact frame index
            Practice_response.status = STARTED
            # keyboard checking is just starting
            Practice_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Practice_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '3', '4', '5'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Practice_response.keys == []:
                    Practice_response.keys = theseKeys[0]  # just the last key pressed

                    Practice_response.rt = Practice_response.clock.getTime()
                    # was this 'correct'?
                    if (Practice_response.keys == str(cor_ans)) or (Practice_response.keys == cor_ans):
                        Practice_response.corr = 1

                    else:
                        Practice_response.corr = 0
                        Wrong_1.setAutoDraw(True)
                    practiceFeedback.setAutoDraw(True)

        # a response ends the routine
        if practiceFeedback.status == STARTED and event.getKeys(keyList=['space']):
            continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Store nothing

# completed 2 repeats of 'practice_loop'


#------Prepare to start Routine "Begin_Blocks"-------
t = 0
Begin_BlocksClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
Begin_BlocksComponents = []
Begin_BlocksComponents.append(text_3)
Begin_BlocksComponents.append(key_resp_3)

for thisComponent in Begin_BlocksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Begin_Blocks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Begin_BlocksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Begin_BlocksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Begin_Blocks"-------
for thisComponent in Begin_BlocksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Begin_Blocks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block_Loop = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'block_loop.csv'),
    seed=None, name='Block_Loop')
thisExp.addLoop(Block_Loop)  # add the loop to the experiment
thisBlock_Loop = Block_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock_Loop.rgb)
if thisBlock_Loop != None:
    for paramName in thisBlock_Loop.keys():
        exec(paramName + '= thisBlock_Loop.' + paramName)

nBlock = 0
max_rt = .6
iti = .25

for thisBlock_Loop in Block_Loop:
    nBlock = nBlock+1
    currentLoop = Block_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_Loop.rgb)
    if thisBlock_Loop != None:
        for paramName in thisBlock_Loop.keys():
            exec(paramName + '= thisBlock_Loop.' + paramName)

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential',
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(u'stimuli.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    block_rts = []
    acc_last_block = []
    max_rt = max_rt
    for thisTrial in trials:

        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)

        #------Prepare to start Routine "Block"-------
        t = 0
        BlockClock.reset()  # clock
        frameN = -1
        routineTimer.add(iti+max_rt)
        # update component parameters for each repeat
        image_2.setImage(eval(Block_id))
        key_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_response.status = NOT_STARTED
        # keep track of which components have finished
        BlockComponents = []
        BlockComponents.append(image_2)
        BlockComponents.append(key_response)
        BlockComponents.append(Wrong_1)
        for thisComponent in BlockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "Block"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *image_2* updates
            if t >= iti and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            if image_2.status == STARTED and t >= (iti + (max_rt-win.monitorFramePeriod*0.75)): #most of one frame period left
                image_2.setAutoDraw(False)

            # *key_response* updates
            if t >= iti and key_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_response.tStart = t  # underestimates by a little under one frame
                key_response.frameNStart = frameN  # exact frame index
                key_response.status = STARTED
                # keyboard checking is just starting

                key_response.clock.reset()  # now t=0

                event.clearEvents(eventType='keyboard')
            if key_response.status == STARTED and t >= (iti + (max_rt -win.monitorFramePeriod*0.75)): #most of one frame period left
                key_response.status = STOPPED
            if key_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['2', '3', '4', '5'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True


                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_response.keys == []:
                        key_response.keys = theseKeys[0]  # just the last key pressed
                        key_response.rt = key_response.clock.getTime()
                        # was this 'correct'?
                        if (key_response.keys == str(eval(Block_ans))) or (key_response.keys == eval(Block_ans)):
                            key_response.corr = 1

                        else:
                            key_response.corr = 0
                            Wrong_1.setAutoDraw(True)
                            win.flip()
                    continueRoutine = False

            if t > max_rt+iti and key_response.keys in ['', [], None]:  # No response was made
                key_response.keys=None
                key_response.corr = 0
                Wrong_1.setAutoDraw(True)
                win.flip()
                continueRoutine= False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlockComponents:

                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:

                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "Block"-------
        for thisComponent in BlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_response.keys in ['', [], None]:  # No response was made
           key_response.keys=None



           # was no response the correct answer?!
           if str(eval(Block_ans)).lower() == 'none': key_response.corr = 1  # correct non-response
           else: key_response.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_response.keys',key_response.keys)
        trials.addData('key_response.corr', key_response.corr)
        if key_response.keys != None:  # we had a response
            trials.addData('key_response.rt', key_response.rt)

        thisExp.nextEntry()
        block_rts = np.append(block_rts,key_response.rt)
        acc_last_block = np.append(acc_last_block, key_response.corr)

    #build adaptive rt design.

    n_corr = np.sum(acc_last_block)
    acc_last_block = n_corr/len(acc_last_block)
    mean_rt = np.mean(block_rts)
    std_rt = np.std(block_rts)
    adapt_rt = mean_rt+std_rt

    if (adapt_rt <.200 or acc_last_block < 0.75) or (nBlock == 6 or nBlock == 7) :
        max_rt = 0.6
    else:
        max_rt = adapt_rt

    # completed 1 repeats of 'trials'


    #------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    FeedbackComponents = []
    FeedbackComponents.append(text_2)
    FeedbackComponents.append(key_resp_5)
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "Feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)

        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys()

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

# completed 1 repeats of 'Block_Loop'


#------Prepare to start Routine "End_Experiment"-------
t = 0
End_ExperimentClock.reset()  # clock
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
End_ExperimentComponents = []
End_ExperimentComponents.append(text)
for thisComponent in End_ExperimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End_Experiment"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End_ExperimentClock.getTime()
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
    for thisComponent in End_ExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End_Experiment"-------
for thisComponent in End_ExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
