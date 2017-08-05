# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:37:44 2017

@author: Anton Cruz
"""

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np


N = 10
M = 10
population = N * M
time = 100
t_1 = 3
aStoC = 1.0
bCtoS = 0.5
alpha = 0.8
beta = 2

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(app.app_sim(aStoC, bCtoS, alpha, beta, N, M, time, t_1))
plt.axhline(app.steady_nC(aStoC, bCtoS, alpha, beta, population, 0), color='r')
ax.text(0.5*time,app.steady_nC(aStoC, bCtoS, alpha, beta, population, -1)+1,'Steady-state: '+str(app.steady_nC(aStoC, bCtoS, alpha, beta, population, -1)), fontsize=20)
ax.text(90,100,'N = '+str(population))
plt.title('a = '+str(aStoC)+' b = '+str(bCtoS)+' alpha = '+str(alpha)+' beta = '+str(beta))
plt.xlabel('Time')
plt.ylabel('State C')
plt.savefig('a = '+str(aStoC)+' b = '+str(bCtoS)+' alpha = '+str(alpha)+' beta = '+str(beta)+'.png')
plt.show()