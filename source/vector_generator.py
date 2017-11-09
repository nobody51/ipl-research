# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:03:26 2017

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

def lastList(abar, bCtoS, alpha, beta, N, M, start, time, t_1, iter): 
    #runs app_sim 'iter' times and lists the last element per iteration
    probVal = []
    for i in range(iter):
        x = app.app_sim(abar, bCtoS, alpha, beta, N, M, start, time, t_1)[-1]
        y = app.steady_nC(abar, bCtoS, alpha, beta, N*M, 1)
        if x==0:
            probVal.append(0.0)
        else:
            probVal.append(1.0)
    return finalVal, probVal