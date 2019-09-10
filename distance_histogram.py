# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:04:22 2019

@author: Eric Matteini

Creates histogram of distance away the stars are
"""


import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
#                               Data Import
# =============================================================================
file = 'hygdata_v3.csv'
dist = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (9)).T
# =============================================================================
#                               Calculations
# =============================================================================
dist_new=[]
      
#=============================================================================
#         
# =============================================================================
plt.figure(figsize=(8, 8), dpi=78)      
plt.hist(dist, bins = 8000, color = 'orange')
plt.xlim(0,1010)
plt.ylim(0,6000)
plt.title('Number of Stars Vs. Distance', fontsize = 18)
plt.xlabel('Parsecs', fontsize = 12)
plt.ylabel('# \n Stars', fontsize = 12, rotation = 0)