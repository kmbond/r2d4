# Before running these programs:
1. The user must have a working version of psychopy installed. It is recommended to install psychopy and its dependencies in a virtual environment. To set up the virtual environment correctly, follow these instructions in this order. It is not necessary to install psychopy's gui to run these scripts.
2. Download and install anaconda (http://continuum.io/downloads), [bash Anaconda.sh]
3. On coax lab machines, choose the home directory for the install location (home/coaxlab/anaconda). 
4. Install additional dependencies:
  a. Install pip, (conda install pip)
  b. Install psyhopy (pip install psychopy) 
  c. Install pyglet (pip install pyglet)
  d. Install wxpython (conda install wxpython), and seaboorn, pip install seaborn. 
5. Depending on your python environment, you may be need to install additional dependencies which you will discover when executing r2d4_behavior.py or the MRI experiments.

# To conduct the experiment. 
1. cd into the directory containing the experimental scripts. 

2. The stimuli for each of the event related (r2d4_MM_MRI) and block design (r2d4_SvR_MRI) and behavioral tests (r2d4_behavior) will be generated automatically for each subject when executing the file.

3. Each of these scripts will generate a 4 data objects, correpsonding to the all of the output data (log), summary data (summary), onsets, and plots.  

4. Encoding of blocks: 1:random, 2:sequence

5. For the MRI experiments (MM and SvR), enter the Run number as the session number. 
