# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:39:25 2019

@author: Eric Matteini
#=============================================================================
Plots histograms of apparent magnitude and absolute magnitude
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# import data 
# =============================================================================

file = 'hygdata_v3.csv'
# Magnitude at 10 parsecs (Absolute Magnitude)
absmag        = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (14)).T

mag        = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (13)).T

dist   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (9)).T 
# =============================================================================
# take every 100th data point
# =============================================================================
dist   = dist[0::200]
mag    = mag[0::200]
absmag = absmag[0::200]

# MAgnitude note: larger mag means the star is dimmer read(visual magnitude)                       

plt.xlim(0,1500)                           
plt.scatter(dist, mag, c="r", label="Apparent Magnitude")
plt.scatter(dist, absmag, c="b", label="Absolute Magnitude" ) 
plt.legend(fontsize=20)
plt.show()                         