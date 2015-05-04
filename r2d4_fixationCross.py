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
import scipy.io

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'fixation_cross'  # from the Builder filename that created this script
expInfo = {'participant':u'', 'session':u''}
endExpNow = False  # flag for 'escape' or other condition => quit the exp


# Setup the Window
win = visual.Window(size=(500, 500), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


fixation = visual.ShapeStim(win,
    vertices=((0, -0.2), (0, 0.2), (0,0), (-0.15,0), (0.15, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor='white')

globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

t = 0
frameN = -1

trial = -1
while globalClock.getTime() < 500:

    fixation.setAutoDraw(True)
    win.flip()
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
win.close()
core.quit()
