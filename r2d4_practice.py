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
expName = 'r2d4_practice'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
data_out = pd.DataFrame(columns=('block','response','rt', 'type'))

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
win = visual.Window(size=[400,400], fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True
    )

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


#store Summary statistics for each subject/run

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'The practice session is about to begin. Press any key to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()

image = visual.ImageStim(win=win, name='image', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[200,200],
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
# Wrong_1 = visual.TextStim(win=win, ori=0, name='Right_1',
#     text='X',    font='Arial',
#     pos=[0, 0], height=.5, wrapWidth=None,
#     color='red', colorSpace='rgb', opacity=1,
#     depth=-6.0)


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
#initialize n_corr and mean_Rt

text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='',    font=u'Arial',
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


##Generate practice stimuli:
block_loops = pd.DataFrame()
block_loops['Block_id'] = ['block_1_img','block_2_img' ]
block_loops['Block_ans'] = ['block_1_ans','block_2_ans' ]
block_loops.to_csv('practice_blocks.csv', index= False)

img_dict = {2: 'image_folder/stim_2.png', 3: 'image_folder/stim_3.png', 4: 'image_folder/stim_4.png', 5: 'image_folder/stim_5.png'}
key_dict = {2:'2', 3:'3', 4:'4', 5:'5'}#key mapping
length = 256 # number of trials within a  block should be 256
dfStims = pd.DataFrame()
block_ids = [1, 1] #1 is random #2 is sequence

#Generate Pseudo-Random Stimuli Ordering
def genRandom(length):
    random_stims = []
    random_img_ids = []
    random_ans = []
    for x in range(0,length):
        if len(random_stims) == 0:
            random_stims.append(randint(2,6))
        elif len(random_stims) > 0:
            val = randint(2,6)
            while val == random_stims[x-1]:
                val = randint(2,6)
            random_stims.append(val)
        random_img_ids.append(img_dict[random_stims[x]])
        random_ans.append(key_dict[random_stims[x]])
    random_img_ids = np.asarray(random_img_ids)
    random_ans= np.asarray(random_ans)
    return (random_img_ids, random_ans)

#Generate Sequence Ordering --.
def genSequence(length):
    #Generate Sequence Stimuli Ordering.
    sequence_stims = [4,5,3,4,2,5,3,2,4,5,4,5,2,4,5,3,2,3,5,3,4,2,3,2,3,5,4,2,4,2,3,5]
    rota_ind = randint(1,31)
    sequence_stims = sequence_stims[rota_ind:]  + sequence_stims[:rota_ind]
    sequence_img_ids = []
    sequence_ans = []
    sequence_stims= np.tile(sequence_stims,8)
    for x in range(0,length):
        sequence_img_ids.append(img_dict[sequence_stims[x]])
        sequence_ans.append(key_dict[sequence_stims[x]])
    return (sequence_img_ids, sequence_ans)

for type in range(0,len(block_ids)):
    if block_ids[type] == 1:
        img_ids, ran_ans = genRandom(length)
        dfStims['block_'+str(type+1)+'_img'] = img_ids
        dfStims['block_'+str(type+1)+'_ans'] = ran_ans
    elif block_ids[type] == 2:
        img_ids, seq_ans = genSequence(length)
        dfStims['block_'+str(type+1)+'_img'] = img_ids
        dfStims['block_'+str(type+1)+'_ans'] = seq_ans

dfStims.to_csv('practice_stims.csv', index= False)


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

t = 0

# set up handler to look after randomisation of conditions etc
Block_Loop = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'practice_blocks.csv'),
    seed=None, name='Block_Loop')


thisExp.addLoop(Block_Loop)  # add the loop to the experiment
thisBlock_Loop = Block_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock_Loop.rgb)
if thisBlock_Loop != None:
    for paramName in thisBlock_Loop.keys():
        exec(paramName + '= thisBlock_Loop.' + paramName)

nBlock = 0
max_rt = 1
iti = .25
RTclock = core.Clock()

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
        trialList=data.importConditions(u'practice_stims.csv'),
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
        #see if this works better:

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

            image_2.setAutoDraw(True)
            win.flip()
            RTclock.reset()
            event.clearEvents(eventType='keyboard')
            theseKeys = event.waitKeys(max_rt,('2','3','4','5'), timeStamped = RTclock)

            if theseKeys is None:
                key_response.corr = 0
                key_response.keys=None
                key_response.rt = float('nan')
                Wrong_1.setAutoDraw(True)
                win.flip()
                core.wait(0.1)
                continueRoutine=False

            elif(len(theseKeys[0]) > 0):
                key_response.keys = theseKeys[0][0]  # just the last key pressed
                key_response.rt = theseKeys[0][1]
                # was this 'correct'?
                if (key_response.keys == str(eval(Block_ans))) or (key_response.keys == eval(Block_ans)):
                    key_response.corr = 1

                else:
                    key_response.corr = 0
                    Wrong_1.setAutoDraw(True)
                    win.flip()
                    core.wait(0.1)
                continueRoutine = False

            for thisComponent in BlockComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    win.flip()

            core.wait(iti)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # store data for trials (TrialHandler)
        trials.addData('key_response.keys',key_response.keys)
        trials.addData('key_response.corr', key_response.corr)
        if key_response.keys != None:  # we had a response
            trials.addData('key_response.rt', key_response.rt)

        thisExp.nextEntry()
        block_rts = np.append(block_rts,key_response.rt)
        acc_last_block = np.append(acc_last_block, key_response.corr)

        #save data in case program crashes -- remove this if its causing any hold ups
        if nBlock in [1,2,6]:
            trial_type = 1
        elif nBlock in [2,4,5,7]:
            trial_type = 2
        #ocasionally key is
        if not key_response.rt:
            key_response.rt = float('nan')
        #add data to file
        data_out.loc[len(data_out)+1]=[nBlock, key_response.corr, key_response.rt, trial_type]
        #'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
    #build adaptive rt design.

    n_corr = np.sum(acc_last_block)
    acc_last_block = n_corr/len(acc_last_block)
    mean_rt = np.nanmean(block_rts)
    std_rt = np.nanstd(block_rts)
    adapt_rt = mean_rt+std_rt

    if (adapt_rt <.200 or acc_last_block < 0.75) or (nBlock == 6 or nBlock == 7) :
        max_rt = 1.0
    else:
        max_rt = adapt_rt

    # completed 1 repeats of 'trials'

    #feedback text component after block completion.
    text_4 = visual.TextStim(win=win, ori=0, name='text_2',
        text='End of Block. You got %i  trials correct out of 256. Your mean response time was : %.2f. \n Press any key to continue' %(n_corr,mean_rt),    font=u'Arial',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'white', colorSpace='rgb', opacity=1,
        depth=0.0)

    #------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    FeedbackComponents = []
    FeedbackComponents.append(text_4)
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
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index

            text_4.setAutoDraw(True)
            event.clearEvents(eventType='keyboard')
            core.wait(.5)
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


#build summary statistics file

win.close()
core.quit()
