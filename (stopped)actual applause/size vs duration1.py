# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:19:08 2016

@author: ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

############################################
# Plots audience size vs applause duration #
# Audience size is set in logscale         #
# Best fit line taken from sir bantang     #
############################################



file = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\PHYSICS\\research\\data.txt")
size = file[:,0]
time_interval = file[:,1]
plt.xscale('log')
plt.plot(size,time_interval, "ko")
plt.xlabel("Audience Size")
plt.ylabel("Applause Duration (s)")


x = []
y = []
T_0 = 1
s_0= 0.4
for s in np.linspace(10,10 ** 5,10):
    x.append(s)
    y.append(T_0 * m.log(s ** 2 / s_0 ** 2))
    
plt.plot(x,y)
#plt.text(0,0,"T(s) = T_0ln{\frac{s^2}{(s_0)^2}}")

plt.savefig("size-vs-duration-logscale-with-best-fit-line")


plt.show()
