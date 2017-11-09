# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:03:26 2017

@author: ADMIN
"""

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np
import time as t

speed = t.time()

N = 10
M = 10
startPop = 1
time = 100
t_1 = 0
aStoC = 1.0
bCtoS = 0.8 
alpha = 1
beta = 10

x = 11
y = 11
z = 100

def lastList(abar, bCtoS, alpha, beta, N, M, start, time, t_1, iter): 
    #runs app_sim 'iter' times and lists the last element per iteration
    probVal = []
    for i in range(iter):
        x = app.app_sim(abar, bCtoS, alpha, beta, N, M, start, time, t_1)[-1]
        if x==0:
            probVal.append(0.0)
        else:
            probVal.append(1.0)
    return probVal
    
def vectorData(bCtoS, beta, x, y, z):
    abarRange = np.linspace(0,1,x)
    startRange = np.linspace(0,100,y)  
    
    n = 0
    
    abar = np.zeros(len(abarRange)*len(startRange))
    start = np.zeros(len(abarRange)*len(startRange))
    dx = np.zeros(len(abarRange)*len(startRange))
    dy = np.zeros(len(abarRange)*len(startRange))
    rawHeat = np.zeros(len(abarRange)*len(startRange))
        
    for i in range(len(abarRange)):
        for j in range(len(startRange)):
            k = lastList(abarRange[i], bCtoS, alpha, beta, N, M, startRange[j], time, t_1, z)
            abar[n] = (abarRange[i])
            start[n] = (startRange[j])
            if sum(k)/len(k) >= 0.5:
                if startRange[j] > np.floor(app.steady_nC(abarRange[i], bCtoS, alpha, beta, N*M, 1)):
                    dy[n] = -max(startRange)/(y-1)
                elif startRange[j] == np.floor(app.steady_nC(abarRange[i], bCtoS, alpha, beta, N*M, 1)):
                    dy[n] = 0
                else:
                    dy[n] = max(startRange)/(y-1)
            else:
                dy[n] = -max(startRange)/(y-1)
            rawHeat[n] = abs(sum(k)/len(k) - 0.5)/0.5
            n += 1
            print(t.time() - speed)
            
    #print(rawHeat)        
    #writes ilist,meanlist, and stdlist into a txt file
    filename = 'b = ' + str(bCtoS) + ', beta = ' + str(beta) + ', x = ' + str(x) + ', y = ' + str(y) + ', z = ' + str(z) + '.txt'    
    with open(filename,'w') as f:
        lis=[abar,start,dx,dy,rawHeat]
        for x in zip(*lis):
            f.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(*x))        
            
    #return rawHeat    
    

    
    
    
    
    
    