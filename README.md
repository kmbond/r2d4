# Before executing r2d4.py
1. To run these scripts, the user must have a working version of psychopy installed. It is recommended (and required on coax lab machines running ubuntu) to install psychopy and its dependencies in a virtual environment. To set up the virtual environment correctly, follow these instructions in this order. It is not necessary to install psychopy's builder app to use these scripts. 
3. If using ubuntu, download and install anaconda (http://continuum.io/downloads), [bash Anaconda.sh]
4. On coax lab machines, choose the home directory for the install location (home/coaxlab/anaconda). 
5. Then install psyhopy (pip install psychopy)
6. If you do not have pyglet installed, install by typing (pip install pyglet)
7. Install wxpython (conda install wxpython)
3. You may be missing additional dependencies which you will discover when executing r2d4_pilot.py.

# To conduct the experiment. 
cd into the directory containing the experimental scripts. 
1. Use genStims.py to generate random and sequence blocks of stimuli (in the terminal enter python genStims.py). These will be saved under stimuli.csv. genStims should be executed each time the user wants new stimuli, i.e. for a each new subject.
2. The order of random and sequence blocks can be modified by modifying the block_id vector in genStims.py. 1 corresponds to a random presentation of stimuli, 2 corresponds to the sequence presentation of stimuli. 
3. r2d4.py will generate a data folder, and save each subject's performance in that folder under three separate files.
4. N.B The user will be prompted to enter the subjects unique id and session number at the start of each experiment. 
