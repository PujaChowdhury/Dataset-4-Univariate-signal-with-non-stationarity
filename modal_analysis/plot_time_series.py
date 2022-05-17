#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Austin Downey
"""


import IPython as IP
IP.get_ipython().magic('reset -sf')

import numpy as np
import scipy as sp
from scipy import fftpack, signal # have to add 
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

plt.close('all')


#%% Load and plot data
D = np.loadtxt('data/timeseries_data.lvm',skiprows=23)

tt = D[:,0]
dd = D[:,1]

plt.figure('beam data',figsize=(6.5,3))
plt.plot(tt,dd,'-',label='data 1')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('acceleration (ms$^2$)')
plt.title('beam data')
plt.xlim([-0.1,45])
plt.legend(framealpha=1,loc=0)



N = tt.shape[0]
T = tt[1]-tt[0]
x = np.linspace(0.0, N*T, N, endpoint=False)
y_fft = fft(dd)
yf = 2.0/N * np.abs(y_fft[0:N//2])
xf = fftfreq(N, T)[:N//2]

plt.figure()
plt.semilogy(xf, yf)
plt.grid()
plt.xlim([0,130])
plt.ylabel('|P|')
plt.xlabel('frequency (Hz)')
plt.tight_layout()










































































