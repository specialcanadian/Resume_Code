# -*- coding: utf-8 -*-
"""
Find the vales of a and B for 

            L = (R**a)(T**B)

And plot fit
"""            

import numpy as np
import matplotlib.pyplot as plt
import math

# =============================================================================
#                               Data Import
# =============================================================================

file = 'hygdata_v3.csv'

lum  = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (33)).T
ci   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (16)).T
                  
# =============================================================================
#                               Parameters
# =============================================================================

t_sun   = 5800
sun_lum = 3.85 * 10**26
r_sun   = 701461097


del_r = r_sun/100
r_min = r_sun - del_r
r_max = r_sun + del_r

del_t = t_sun/65
t_min = t_sun - del_t
t_max = t_sun + del_t

# =============================================================================
#                               Calculations
# =============================================================================


temp   = []
radius = []
lum_i  = []
beta_i = []
alpha_i= []

"""
To view plot of L vs T
    set const_R = True
    
To view plot of L vs R
    set const_R = False
"""
const_R = False ######################################

if const_R == True:
    const_T = False
else:
    const_T = True


for i in range (len(ci)):
    if np.isnan(ci[i]) == False:
        t = 4600*((1/(.92*ci[i]+1.7))+1/(.92*ci[i]+.62))
    if np.isnan(lum[i]) == False:
        r = np.sqrt(((lum[i]) * (sun_lum)) /(4*np.pi*(5.67*(10**(-8))*t**4)))
    
    if const_R == True and r_min < r < r_max:
        temp.append((t/t_sun))
        radius.append(r)
        lum_i.append(lum[i])
        
        beta_x = math.log(lum[i],t/t_sun)
        beta_i.append(beta_x)
        
    if const_T == True and t_min < t < t_max:
        temp.append(t)
        radius.append(r/r_sun)
        lum_i.append(lum[i])
        
        alpha_x = math.log(lum[i], r/r_sun)
        if alpha_x > -1000:  #eliminating outlire print min(alpha_i)
            alpha_i.append(alpha_x)

# =============================================================================
#                           Plots
# =============================================================================
"""
To view plot of L vs T
    set const_R = True
    
To view plot of L vs R
    set const_R = False
"""
    
if const_R == True:
    plt.scatter(temp,lum_i, c = 'k', label = 'Data')  
    
    beta = np.mean(beta_i) 
    print 'Beta =', beta
    
    x = np.linspace(.6,2.1,100)
    y = x**beta
    plt.plot(x,y, c = 'g', label = 'T**Beta \n Beta = 4.0039')
    plt.title('Luminosity vs Temperature \n Radius resticted to Rsun +- 1/100 Rsun')
    plt.xlabel(r'$\frac{T}{T_{\odot}}$')
    plt.ylabel(r'$\frac{L}{L_{\odot}}$', rotation = 0)
    plt.legend()

if const_T == True:
    plt.scatter(radius,lum_i, c = 'k', label = 'Data') 
       
    alpha = np.mean(alpha_i) 
    print 'Alpha =', alpha
    
    x = np.linspace(.6,7500,100)
    y = x**alpha
    plt.plot(x,y, c = 'g', label = 'R**Alpha \n Alpha = 2.0091')
    plt.title('Luminosity vs Radius \n Temperature resticted to Tsun +- 1/65 Tsun')
    plt.xlabel(r'$\frac{R}{R_{\odot}}$')
    plt.ylabel(r'$\frac{L}{L_{\odot}}$', rotation = 0)
    plt.legend()