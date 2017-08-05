# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:19:08 2016

@author: ADMIN
"""

import numpy as np
import pylab as plt

file = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\PHYSICS\\research\\data.txt")
x = file[:,1]
y = file[:,0]
plt.yscale('log')
plt.plot(x,y, "ko")
plt.xlabel("Applause Duration")
plt.ylabel("Audience Size")

plt.show()