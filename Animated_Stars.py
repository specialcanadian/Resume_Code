# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:31:35 2019

@author: Eric Matteini
#==============================================================================
This program takes (x, y, z) coordinates of the stars from the 
HYG-star database, then takes their corresponding velocity in each of the 
directions, and finally runs an animated graph of the stars moving, 
relative to the sun. 
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# =============================================================================
# get some data
# =============================================================================
file = 'hygdata_v3.csv'

x_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (17)).T

y_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (18)).T   

z_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (19)).T

v_x   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (20)).T

v_y   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (21)).T   

v_z   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (22)).T


# =============================================================================
# Generate / format data                      
# =============================================================================
"""
This section does a few things 

1.) asks the user how many stars they want to see

2.) Checks to see if the star is in bounds (dist < 100000)

3.) Checks for repeated stars
"""
#print(v_x[10], v_y[10], v_z[10])
""" Gets user input"""
#N_stars = int(input("number of stars: "))
N_stars = 5
"""Time step"""
time = np.arange(0,50000000,500000)

"""Picks random stars from the data set"""
star = np.random.randint(0, 119610+1, N_stars)

"""Finds avg velocities of stars in each direction"""
#v_x_sum = np.sum(v_x)
#v_x_lentgh = len(v_x)
#v_x_avg = (v_x_sum)/(v_x_lentgh)

"""
This part checks to make sure no star is over 1000 units away in any (x,y,z) 
direction
"""
for j in range(len(star)):
    while np.absolute(x_coord[star[j]]) >= 1000:
#        
        star[j]=np.random.randint(0, 119610+1,1)
#       
    while np.absolute(y_coord[star[j]]) >= 1000:
#        
        star[j]= np.random.randint(0, 119610+1,1)
#        
    while np.absolute(z_coord[star[j]]) >= 1000:
#        
        star[j]= np.random.randint(0, 119610+1,1)
#        f
    """This part Checks for repeats"""
    for i in range(len(star)):
            while star[j]==star[i] and i!=j:
#                
                star[j]= np.random.randint(0, 119610+1,1)
                
print("Star id in database",star)

# =============================================================================
# Create animated graph
# =============================================================================
"""Time step"""
time = np.arange(0,50000000,500000)

"""Animated graph of the stars """
for t in time:

    for s in star:
        # This piece plots the linear path of the given star ==================
       
        plt.rcParams['grid.color'] = "purple"
        Xpos0 = ((x_coord[s] + v_x[s] * t))
        Ypos0 = ((y_coord[s] + v_y[s] * t))
        Zpos0 = ((z_coord[s] + v_z[s] * t))
        
        Xline0 = [x_coord[s], Xpos0]
        Yline0 = [y_coord[s], Ypos0]
        Zline0 = [z_coord[s], Zpos0]
        
        
        #ax.scatter(Xpos0, Ypos0, Zpos0)
        ax.plot(Xline0, Yline0, Zline0, c=("c"))
        
        # Plots (x, y, z) coordinates of given stars ==========================
        ax.scatter(x_coord[s], y_coord[s], z_coord[s], s= 100, c=([0.9, 0.3,0.3]),zorder=5)
        if t <= 550000:
            
            ax.legend(fontsize=30)
#    ax.xaxis.pane.fill = False
#    ax.yaxis.pane.fill = False
#    ax.zaxis.pane.fill = False
#
#    
#    ax.w_xaxis.set_pane_color((0, 1, 0))
#    ax.w_yaxis.set_pane_color((0, 1, 0))
#    ax.w_zaxis.set_pane_color((0, 1, 0))
    ax.w_xaxis.set_pane_color([0, 0, 0 , 1])
    ax.w_yaxis.set_pane_color([0, 0, 0 , 1])
    ax.w_zaxis.set_pane_color([0, 0, 0 , 1])
    
   
    ax.patch.set_facecolor([0.7, 0.7, 0.7])
    ax.set_xlim(-800, 800)
    ax.set_ylim(-800, 800)    
    ax.set_zlim(-800, 800)
    ax.set_xlabel('X')
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    # plots sun ==============================================================
    ax.scatter(0.000005, 0, 0, s= 200, c=([1, 0.8, 0]), label="Sun",zorder=2)
    #ax.text(0.000005, -80, 100,"SUN",size=15,zorder=0)
    plt.pause(0.000005)
#    ax.legend(None)
#    ax.legend()
    plt.show() 
