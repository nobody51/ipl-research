# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:22:19 2018

@author: ADMIN
"""

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np
import time

N = 10
M = 10
population = N * M
t = 100
t_1 = 5
C = 0
aStoC = 1
bCtoS = 0.8
alpha = 0.2
beta = 1

start_time = time.time()
trials = 5
popSet = [4,5,6,7,8,9,10,15,18,20,25,28,32,54,70,86,100]#,159,223,274,315] #set sqrt numbers that encompass the log scale

#used to take the index for which SIM becomes 0; gets the applause duration
def indexFilter(value,qlist,r1,r2):
    try:
        return qlist.index(value,r1,r2)
    except ValueError:
        return 0

for alpha_iter in range(2,10,1):
    for bCtoS_iter in range(2,10,1):
        
        #lists to be graphed
        duration = []
        durationSTD = []
        population = []
        
        for pop in popSet: #goes thru popSet
            appDurationTrials = [] #temporary holder of trials to be averaged   
            for j in range(trials): #simulates parameters and population TRAIL times
                N = pop
                sim = app.sim_space(aStoC, bCtoS_iter*0.1, alpha_iter*0.1, beta, N, N, C, t, t_1)
                appDurationTrials.append(indexFilter(0,sim,1,t))
                print('Trial ' + str(j) + ' complete ')
        
            duration.append(np.mean(appDurationTrials))
            durationSTD.append(np.std(appDurationTrials))
            population.append(N*N)
            print("Population " + str(pop) + " complete " + str(time.strftime("%Y-%m-%d %H:%M:%S")))
        #scatter plot with error bars
        #plt.subplot(111, xscale="log")
        fig = plt.figure()
        ax = fig.add_subplot(111,xscale="log") 
        x = population 
        y = duration 
        plt.errorbar(x, y, xerr=0, yerr=durationSTD, fmt='o') 
        plt.title('$a = $'+str(aStoC)+' $b = $'+str(bCtoS_iter*0.1)+r' $\alpha=$'+str(alpha_iter*0.1)+r' $\beta=$'+str(beta),fontsize=20)
        plt.xlabel('Size',fontsize=18)
        plt.ylabel('Time',fontsize=18)
        #plt.savefig('a = '+str(aStoC)+' b = '+str(bCtoS_iter*0.1)+r' alpha='+str(alpha_iter*0.1)+r' beta='+str(beta)+'.png')
        plt.show()
        print(str(time.time() - start_time) + ' seconds; ' + str(time.strftime("%Y-%m-%d %H:%M:%S")))
        


