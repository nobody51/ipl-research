# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:28:37 2017

@author: ADMIN
"""
import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt, sum
import applause_functions as app


N = 10
M = 10
population = N * M
time = 500
t_1 = 0
C = 28
aStoC = 1
bCtoS = 0.5
alpha = 0.2
beta = 10

x = []
y = []
yneg = []
for alpha in np.arange(0,1.01,0.01):
    x.append(alpha)
    y.append(app.steady_nC(aStoC, bCtoS, alpha, beta, population, 1))
    yneg.append(app.steady_nC(aStoC, bCtoS, alpha, beta, population, -1))
    
plt.plot(x,y)
plt.plot(x,yneg)
plt.show()