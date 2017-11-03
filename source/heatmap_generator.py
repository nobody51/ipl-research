# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:14:50 2017

@author: ADMIN
"""

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np
import time as t

speed = t.clock()

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

#a = app.app_sim(aStoC, bCtoS, alpha, beta, N, M, startPop, time, t_1)

def probFilter(a): #converts all non-zero values in a list to 1
    for q in range(len(a)):
        if a[q] != 0:
            a[q] = 1

def lastList(abar, bCtoS, alpha, beta, N, M, start, time, t_1, iter): 
    #runs app_sim 'iter' times and lists the last element per iteration
    finalVal = []
    probVal = []
    for i in range(iter):
        x = app.app_sim(abar, bCtoS, alpha, beta, N, M, start, time, t_1)[-1]
        finalVal.append(x)
        if x==0:
            probVal.append(0.0)
        else:
            probVal.append(1.0)
    return finalVal, probVal
    
    
def heatData(bCtoS, beta, x, y, z):
    abarRange = np.linspace(0,1,x)
    startRange = np.linspace(0,100,y)  
    
    n = 0
    
    abar = np.zeros(len(abarRange)*len(startRange))
    start = np.zeros(len(abarRange)*len(startRange))
    rawHeat = np.zeros(len(abarRange)*len(startRange))
        
    for i in range(len(abarRange)):
        for j in range(len(startRange)):
            k = lastList(abarRange[i], bCtoS, alpha, beta, N, M, startRange[j], time, t_1, z)
            abar[n] = (abarRange[i])
            start[n] = (startRange[j])
            rawHeat[n] =(sum(k[1])/len(k[1]))
            n += 1
            print(t.clock() - speed)
            
    #writes ilist,meanlist, and stdlist into a txt file
    filename = 'b = ' + str(bCtoS) + ', beta = ' + str(beta) + ', x = ' + str(x) + ', y = ' + str(y) + ', z = ' + str(z) + '.txt'    
    with open(filename,'w') as f:
        lis=[abar,start,rawHeat]
        for x in zip(*lis):
            f.write("{0}\t{1}\t{2}\n".format(*x))        
            
    #return abar,start,rawHeat
    
        

        
        
    
    
    
    
        
        
        