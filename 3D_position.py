# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 08:06:44 2019

@author: Eric Matteini

Creates a 3-D plot of the position off all the stars
"""
# import that good kush
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
# get some data
# =============================================================================

x_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (17)).T

y_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (18)).T   

z_coord   = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (19)).T
  
dist = np.genfromtxt(file, dtype=None, skip_header = 1 , delimiter = ',', \
                     usecols = (9)).T  
# =============================================================================
# plot like a disney villan                           
# =============================================================================
dist_new=[]
x_new=[]
y_new=[]
z_new=[]



for i in range (len(dist)):
    if dist[i] <= 900000:
        dist_new.append(dist[i])
        x_new.append(x_coord[i])                  
        y_new.append(y_coord[i])
        z_new.append(z_coord[i])


fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X')
ax.set_ylabel("Y")
ax.set_zlabel("Z")
## Zooms in on close cluster ===================================================
#ax.set_xlim3d(-1500, 1500)
#ax.set_ylim3d(-1500,1500)
#ax.set_zlim3d(-1500,1500)
#ax.scatter(x_close, y_close, z_close, 'r')
#
## Graph of every 10th star ====================================================
#x_new = x_coord[0::10]
#y_new = y_coord[0::10]
#z_new = z_coord[0::10]
###print( len(x_coord), len( x_new))
#ax.scatter(x_new, y_new, z_new, s=10, alpha=0.5)
# Show where sun is ==========================================================
X_sun1 = [-10, 0.000005, 10]
Y_sun1 = [0, 0, 0]
Z_sun1 = [0, 0, 0]

X_sun2 = [0.000005, 0.000005, 0.000005]
Y_sun2 = [-10, 0, 10]
Z_sun2 = [0, 0, 0]

X_sun3 = [0.000005, 0.000005, 0.000005]
Y_sun3 = [0, 0, 0]
Z_sun3 = [-10, 0, 10]

ax.plot(X_sun1, Y_sun1, Z_sun1, c="r")
ax.plot(X_sun2, Y_sun2, Z_sun2, c="r")
ax.plot(X_sun3, Y_sun3, Z_sun3, c="r")
#ax.scatter(0.000005, 0, 0, s= 100)

# Graph of the full data set ==================================================
ax.scatter(x_new, y_new, z_new, 'b')  
ax.set_title("Cartesian Cooardinates, Sun as origin") 
plt.show()                       