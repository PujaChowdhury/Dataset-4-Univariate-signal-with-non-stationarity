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

plt.close('all')


#%% Load and plot data
D = np.loadtxt('Impulse_test.lvm',skiprows=23)

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
plt.tight_layout()
plt.savefig('plot.pdf')
plt.savefig('plot_1.png')
plt.savefig('plot_2.png',dpi=300)











































































