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
startPop = 10
time = 100
t_1 = 0
aStoC = 1.0
bCtoS = 0.8 
alpha = 1
beta = 10
###Point Generator Parameters###
Trials = 50
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
        list_a.append(app.app_sim(aStoC, bCtoS, i, beta, N, M, startPop, time, t_1)[time-1]) #takes the last number from the appsim vector
    mean = np.mean(np.array(list_a))
    std = np.std(np.array(list_a))  
    meanlist.append(mean)
    stdlist.append(std)
    ilist.append(i)
#    plt.scatter(i,mean, color='k')

ilist = np.array(ilist)
meanlist = np.array(meanlist)
stdlist = np.array(stdlist)

#valuesmatrix = np.vstack((ilist,meanlist,stdlist)).T
filename = 'b = ' + str(bCtoS) + ', beta = ' + str(beta) + '.txt'
#np.savetxt(filename, valuesmatrix, delimiter = ',')

with open(filename,'w') as f:
    lis=[ilist,meanlist,stdlist]
    for x in zip(*lis):
        f.write("{0}\t{1}\t{2}\n".format(*x))


                   
plt.title('b = ' + str(bCtoS) + ', beta = ' + str(beta) + ', startPop = ' + str(startPop))
plt.xlabel('a * alpha')
plt.ylabel('n')
plt.scatter(ilist,meanlist)
plt.show()

