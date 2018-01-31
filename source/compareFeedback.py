# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:42:13 2018

created to compare the effects of the different feedbacks

@author: ADMIN
"""



import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np

N = 10
M = 10
population = N * M
time = 500
t_1 = 1
C = 0
aStoC = 0.8
bCtoS = 0.1
alpha = 1
beta = 5

fig = plt.figure()
ax = fig.add_subplot(111)
sim1 = app.app_sim(aStoC, bCtoS, alpha, beta, N, M, C, time, t_1)
sim2 = app.sim_space(aStoC, bCtoS, alpha, beta, N, M, C, time, t_1,M)
sim3 = app.sim_space(aStoC, bCtoS, alpha, beta, N, M, C, time, t_1,0)
plt.plot(sim1, color='b')
plt.plot(sim2, color='r')
plt.plot(sim3, color='g')

ax.text(5,101,'N = '+str(population), fontsize=15)

plt.title('$a = $'+str(aStoC)+' $b = $'+str(bCtoS)+r' $\alpha=$'+str(alpha)+r' $\beta=$'+str(beta),fontsize=20)
plt.xlabel('Time',fontsize=18)
plt.ylabel('State'+r' $n_{c}$',fontsize=18)
plt.ylim(0,110)
#plt.savefig('sim2.png')
plt.show()
