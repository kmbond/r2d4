import numpy as np
import scipy.io
import pandas as pd

df = pd.read_csv('0273_r2d4_MM_Run6_onsets.csv',header=None)
new_onsets = np.empty((df.shape[1]), dtype=object)
for i in range(0,df.shape[1]):
    new_onsets[i] = np.array(df[i][:,np.newaxis])/2 #/2 to switch to TRs for SPM

data={}
data['ons'] = new_onsets
scipy.io.savemat('TESTING.mat', data)
