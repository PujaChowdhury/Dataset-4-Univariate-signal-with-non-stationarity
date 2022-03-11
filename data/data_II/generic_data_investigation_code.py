
"""
@author: Austin Downey

This script is for the user's to generate bacis plots of the data

"""
#%% Load Libraries
import IPython as IP
IP.get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

#%% Load and processes data

D = np.loadtxt('Test_4.lvm',skiprows=23)
tt = D[:,0]     # time
vv = D[:,1]     # Voltage
ff = D[:,2]     # Force
aa = D[:,3]     # Acceleration


delta_tt = []
for i in range(tt.shape[0]-1): 
    delta_tt.append(tt[i+1]-tt[i]) 
delta_tt = np.asarray(delta_tt)

#%% Plot the data

plt.figure()
plt.plot(tt,aa,'-o')
plt.xlabel('time (s)')


plt.figure()
plt.plot(aa,'-o')
plt.xlabel('time (s)')



























