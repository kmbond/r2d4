# Before executing r2d4.py
1. To run these scripts, the user must have a working version of psychopy installed. It is recommended (and required on coax lab machines running ubuntu) to install psychopy and its dependencies in a virtual environment. To set up the virtual environment correctly, follow these instructions in this order. It is not necessary to install psychopy's builder app to use these scripts. 
2. If using ubuntu, download and install anaconda (http://continuum.io/downloads), [bash Anaconda.sh]
3. On coax lab machines, choose the home directory for the install location (home/coaxlab/anaconda). 
4. conda install pip
5. Then install psyhopy (pip install psychopy) 
6. If you do not have pyglet installed, install by typing (pip install pyglet)
7. Install wxpython (conda install wxpython), and pip install seaborn. 
8. You may be missing additional dependencies which you will discover when executing r2d4_pilot.py.

# To conduct the experiment. 
cd into the directory containing the experimental scripts. 
1. The stimuli for each of the event related (r2d4_MM_MRI) and block design (r2d4_SvR_MRI) and behavioral tests (r2d4_behavior) will be generated automatically for each subject when executing the file. 
2. Each of these scripts will generate a 4 dataframes, correpsonding to the all of the output data (log), summary data (summary), onsets, and plots.  
2. Encoding of blocks: 1:random, 2:sequence
4. For the MRI experiments (MM and SvR), enter the Run number as the session number. 
5. 
