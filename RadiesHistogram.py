# -*- coding: utf-8 -*-
"""
Histogram of radii
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                               Data Import
# =============================================================================
t_sun = 5800
r_sun   = 701461097
sun_lum = 3.85 * 10**26



file = 'hygdata_v3.csv'

lum  = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (33)).T
ci   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (16)).T

# =============================================================================
#                               Calculations
# =============================================================================
temp   = []
radius = []
lum_i  = []

for i in range (len(ci)):
 

    t = 4600*((1/(.92*ci[i]+1.7))+1/(.92*ci[i]+.62))
    r = np.sqrt(((lum[i]) * (sun_lum)) /(4*np.pi*(5.67*(10**(-8))*t**4)))
    if r/r_sun < 70:        
        radius.append(r/r_sun)
            
            
            
# =============================================================================
#                               Plot
# =============================================================================
plt.hist(radius, bins=100)
plt.title('Radial Distribution', fontsize=40)
plt.xlabel(r'$\frac{R}{R_{\odot}}$', fontsize=50)

