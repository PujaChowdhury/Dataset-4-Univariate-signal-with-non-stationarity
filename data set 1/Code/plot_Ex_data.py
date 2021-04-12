# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:23:00 2020

@author: Puja PC
"""



#%% Import library

import IPython as IP
IP.get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import RecurrencePlot
import pandas as pd
import json
import os


#%% Data loading

#file='Labview(PC)/Test_03_13_2020/Data/Ivol_Acc_Load_1S_1STD.lvm'

file='../Data/original/Ivol_Acc_Load_data1_w3_NSTD.lvm'

title = 'Sine wave NSTD'
D=np.loadtxt(file,skiprows=23)      # skiprows mean how many header i the data
#%% Plot Input Vs Force

TT=D[:,0]   # Time

DY1=D[:,1]   # Input
DY2=D[:,2]  # Force
#DY3=D[:,3]  # Acceleration


xl='Time'
yl1='Input Signal (volts)'
#yl2='Acceleration (m/$s^2$)'
yl2='Force (N)'
fig = plt.figure(figsize=(4,1.25))
ax1 = fig.add_subplot()
plt.title(title)
color = 'tab:blue'
ax1.set_xlabel(xl)
ax1.set_ylabel(yl1, color=color)
ax1.plot(TT, DY1 ,'-.', color=color, label = yl1)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel(yl2, color=color)
ax2.plot(TT, DY2 ,'--', color=color, label = yl2)
ax2.tick_params(axis='y', labelcolor=color)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc=4)
#plt.savefig(title+'Single Sine wave STD 5%', dpi=400)
plt.savefig('../Figure/Sine wave NSTD for Input Vs Force', dpi=400)
plt.tight_layout()

#%% Plot Input Vs Acceleration
TT=D[:,0]   # Time
DY1=D[:,1]   # Input
#DY2=D[:,2]  # Force
DY3=D[:,3]  # Acceleration


xl='Time'
yl1='Input Signal (volts)'
yl2='Acceleration (m/$s^2$)'
#yl2='Force (N)'
fig = plt.figure(figsize=(4,1.25))
ax1 = fig.add_subplot()
plt.title(title)
color = 'tab:blue'
ax1.set_xlabel(xl)
ax1.set_ylabel(yl1, color=color)
ax1.plot(TT, DY1 ,'-.', color=color, label = yl1)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel(yl2, color=color)
ax2.plot(TT, DY3 ,'--', color=color, label = yl2)
ax2.tick_params(axis='y', labelcolor=color)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc=4)
plt.savefig('../Figure/Sine wave NSTD for Input Vs Acceleration', dpi=400)
plt.tight_layout()

