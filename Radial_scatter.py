# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:11:16 2019

@author: Eric Matteini

Creates scatter plot of radial velocity
"""
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
#                               Data Import
# =============================================================================
t_sun = 5800

file = 'hygdata_v3.csv'

lum  = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (33)).T
ci   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (16)).T
dist = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (9)).T
radial_v = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (12)).T 
# =============================================================================
#                               Calculations
# =============================================================================
r_v    = []
temp   = []
radius = []
lum_i  = []
dist_new=[]
for i in range (len(ci)):
    if radial_v[i] != 0:
        
        dist_new.append(dist[i])        
        r_v.append(radial_v[i])
    if lum[i] <= (10**10):
        t = 4600*((1/(.92*ci[i]+1.7))+1/(.92*ci[i]+.62))
        
            
        #r = np.sqrt(((lum[i])*(3.85*(10**26)/(4*np.pi*(5.67*(10**(-27))*t**4)))))
        temp.append(t/t_sun)
        #radius.append(r)
        lum_i.append(lum[i])

# =============================================================================
# 
# =============================================================================
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(dist_new, r_v, c=(0, 0 , 0.4),s=0.7)
ax1.set_title('Radial Velocity vs Distance', fontsize=60)
ax1.set_xlabel("Distance (Parsecs)", fontsize=60)
ax1.set_ylabel("Radial Velocity", fontsize=60)
ax2.hist(r_v, color=(0, 0, 0.4), bins = 1000)
ax2.set_title("Radial Velocity Histogram", fontsize=60)
ax2.set_xlabel("Radial Velocity (Km/s)", fontsize=60)
ax2.set_ylabel("Number of Stars", fontsize=60)
#plt.scatter(dist_new, r_v, s=0.5)
ax1.set_xlim(0,1500)
ax2.grid(axis="y", color="r")
f.patch.set_facecolor((0.7, 0.7, 0.7))
#ax1.set_facecolor((0.7, 0.7, 0.8))
#ax2.set_facecolor((0.7, 0.7, 0.8))

#plt.hist(r_v, bins = 1000)
#ax1.ylim(-600,600)
plt.subplots_adjust(wspace=1)



