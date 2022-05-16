
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:23:00 2022

@author: Puja PC
"""



#%% Import library

import IPython as IP
IP.get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt
# from pyts.image import RecurrencePlot
import pandas as pd
import json
import os

#%% plotting with specific parameters
# Reseting plot parameter to default
plt.rcdefaults()
# Updating Parameters for Paper
params = {
    'lines.linewidth' :.5,
    'lines.markersize' :1,
   'axes.labelsize': 8,
    'axes.titlesize':8,
    'axes.titleweight':'normal',
    'font.size': 8,
    'font.family': 'Times New Roman', # 'Times New RomanArial'
    'font.weight': 'normal',
    'mathtext.fontset': 'stix',
    'legend.shadow':'False',
   'legend.fontsize': 6,
   'xtick.labelsize': 8,
   'ytick.labelsize': 8,
   'text.usetex': False,
    'figure.autolayout': True,
   'figure.figsize': [5.5,2.5] # width and height in inch (max width = 7.5", max length = 10")
   }
plt.rcParams.update(params)
#%% FFT Data loading

file='data/FFT_data.lvm'

D=np.loadtxt(file,skiprows=24)      # skiprows mean how many header i the data
#%% Plot FFT

TT=D[:,0]   # frequency
DY1=D[:,1]   # amplitude


plt.rcParams.update(params)
fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot()
ax.plot(TT,DY1)

ax.set_title('FFT')
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude')
plt.yscale('symlog')
plt.xlim(0,121)
plt.savefig('figure/FFT', dpi=300)
plt.savefig('figure/FFT.pdf', dpi=300)
plt.tight_layout()
#%%#%% time series data loading

file1='data/timeseries_data.lvm'

D=np.loadtxt(file1,skiprows=24)      # skiprows mean how many header i the data
#%% Plot Input Vs Force

TT=D[:,0]   # time
DY1=D[:,1]   # acceleration

plt.rcParams.update(params)
fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot()
ax.plot(TT,DY1)
plt.grid(True)

plt.tight_layout()
ax.set_title('beam data')
plt.xlabel('time (s)')
plt.ylabel('acceleration (ms$^2$)')
plt.xlim()
plt.savefig('figure/beamdata', dpi=300)
plt.savefig('figure/beamdata.pdf', dpi=300)
plt.tight_layout()