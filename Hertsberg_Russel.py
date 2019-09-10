# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:01:07 2019

@author: Eric Matteini
#==============================================================================

This program makes a scatter plot of luminosity vs temperature
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# =============================================================================
#                               Data Import
# =============================================================================
t_sun = 5800
r_sun   = 701461097


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
sun_lum = 3.85 * 10**26
for i in range (len(ci)):
    if radial_v[i] != 0:
                
        r_v.append(radial_v[i])
    if lum[i] <= (10**10):
        # using ballestero's formula
        t = 4600*((1/(.92*ci[i]+1.7))+1/(.92*ci[i]+.62))
        
        r = np.sqrt(((lum[i]) * (sun_lum)) /(4*np.pi*(5.67*(10**(-8))*t**4)))
        if r/r_sun < 100:
            
            temp.append(t/t_sun)
            radius.append(r/r_sun)
            lum_i.append(lum[i])
#=============================================================================
#                               Plot
# =============================================================================
        
# ============= Hertsberg-Russel =================================
fig = plt.figure(figsize=(15, 15), dpi=80)
ax = fig.add_axes([.1,.1,.85,.8])
#ax.set_axis_bgcolor('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.set_title('Hertzsprung-Russell \n Diagram', fontsize=18)
ax.title.set_position([.5, 1.03])
ax.set_ylabel(r'$\frac{L}{L_{\odot}}$', color = 'black', rotation = 0)
ax.yaxis.label.set_fontsize(20)
ax.title.set_fontsize(25)
ax.set_xlabel(r'$\frac{T}{T_{\odot}}$',fontsize=14)
ax.xaxis.label.set_fontsize(20)
ax.scatter(np.log(temp), np.log(lum_i), s = 0.05 , c = np.log(radius))
plt.gca().invert_xaxis()
ax.annotate(
    'main sequence', xy=(0.6, 0.5), xycoords='data',
    fontsize='14', color='red',
    xytext=(-40, -40), textcoords='offset points',
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=-3.0",
        color='red'))
ax.annotate(
    'Super-Giants', xy=(0.2, 18), xycoords='data',
    fontsize='14', color='red',
    xytext=(-40, 40), textcoords='offset points',
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=-.2",
        color='red'))
ax.annotate(
    'White-Dwarfs', xy=(0.3, -10), xycoords='data',
    fontsize='14', color='red',
    xytext=(-40, -40), textcoords='offset points',
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=-.2",
        color='red'))
ax.annotate(
    'Giants', xy=(-0.7, 5), xycoords='data',
    fontsize='14', color='red',
    xytext=(-40, 50), textcoords='offset points',
    arrowprops=dict(
        arrowstyle="->",
        connectionstyle="arc3,rad=-2",
        color='red'))
ax.scatter(0,0, c = 'r', s = 100, label = 'Sun')

ax.legend()