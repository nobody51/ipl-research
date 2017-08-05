####################################################################################
#Takes the last point of the simulation (Trials) times then calculates mean and std#
#Does so for varying a-bar values                                                  #
#Creates .csv file with columns: a-bar, mean, std                                  #
#Plots the data points                                                             #
#Parameters can be adjusted accordingly below                                      #
####################################################################################

import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np

#####Simulation Parameters#####
N = 10
M = 10
time = 100
t_1 = 3
aStoC = 1.0
bCtoS = 0.8 
alpha = 1
beta = 10
###Point Generator Parameters###
Trials = 10
interval = 0.02
##############################

xgraph = []
ygraph = []
meanlist = []
stdlist = []
ilist = []
for i in np.arange(0,1.0,interval):
    list_a = []
    for j in range(Trials):
        list_a.append(app.app_sim(aStoC, bCtoS, i, beta, N, M, 0, time, t_1)[time-1]) #takes the last number from the appsim vector
    mean = np.mean(np.array(list_a))
    std = np.std(np.array(list_a))  
    meanlist.append(mean)
    stdlist.append(std)
    ilist.append(i)
#    plt.scatter(i,mean, color='k')

ilist = np.array(ilist)
meanlist = np.array(meanlist)
stdlist = np.array(stdlist)

valuesmatrix = np.vstack((ilist,meanlist,stdlist)).T
filename = 'b = ' + str(bCtoS) + ', beta = ' + str(beta) + '.csv'
np.savetxt(filename, valuesmatrix, delimiter = ',')
                   
plt.title('b = ' + str(bCtoS) + ', beta = ' + str(beta))
plt.xlabel('a * alpha')
plt.ylabel('n')
plt.scatter(ilist,meanlist)
plt.show()

