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

plt.figure('beam data',figsize=(5.5,2.5))
plt.plot(tt,dd,'-')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('acceleration (ms$^2$)')
plt.title('beam data')
plt.xlim([3.25,4])
# plt.savefig('figure/beamdata', dpi=300)
# plt.savefig('figure/beamdata.pdf', dpi=300)ss


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
plt.title('FFT')
plt.tight_layout()
# plt.savefig('figure/FFT', dpi=300)
# plt.savefig('figure/FFT.pdf', dpi=300)









































































