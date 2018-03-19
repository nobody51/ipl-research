# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:22:19 2018

@author: ADMIN
"""

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np

N = 10
M = 10
population = N * M
time = 100
t_1 = 5
C = 0
aStoC = 0.2
bCtoS = 0.8
alpha = 1
beta = 10

trials = 10
popSet = [2,3,4,5,6,7,8,9,10,15,18,20,25,28,32,54,70,86,100] #set sqrt numbers that encompass the log scale

#used to take the index for which SIM becomes 0; gets the applause duration
def indexFilter(value,qlist,r1,r2):
    try:
        return qlist.index(value,r1,r2)
    except ValueError:
        return -1

#lists to be graphed
duration = []
durationSTD = []
population = []

for pop in popSet: #goes thru popSet
    appDurationTrials = [] #temporary holder of trials to be averaged   
    for j in range(trials): #simulates parameters and population TRAIL times
        N = pop
        sim = app.app_sim(aStoC, bCtoS, alpha, beta, N, N, C, time, t_1)
        appDurationTrials.append(indexFilter(0,sim,1,time))


    duration.append(np.mean(appDurationTrials))
    durationSTD.append(np.std(appDurationTrials))
    population.append(N*N)

#scatter plot with error bars
plt.subplot(111, xscale="log") 
x = population 
y = duration 
plt.errorbar(x, y, xerr=0, yerr=durationSTD, fmt='o') 
plt.show() 

