# r2d4
1. To run these scripts, the user must have a working version of psychopy installed. It is recommended to install psychopy and its dependencies in a virtual environment. 
3. If using ubuntu, download and install  anaconda (http://continuum.io/downloads), [bash Anaconda.sh]
4. On coax lab machines, choose the home directory for the install location (home/coaxlab/anaconda). 
5. Then install psyhopy (pip install psychopy)
6. If you do not have pyglet installed, install by typing (pip install pyglet)
7. Install wxpython (conda install wxpython)
3. You may be missing additional dependencies which you will discover when executing r2d4_pilot.py

# To conduct the experiment. 
1. Use genStims.py to generate random and sequence blocks of stimuli. These will be saved under stimuli.csv. genStims should be executed each time the user wants new stimuli, i.e. for a new subject.
2. r2d4.py will generate a data folder, and save subjects performance in that folder under three files.  

