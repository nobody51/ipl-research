# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:42:13 2018

created to compare the effects of the different feedbacks

@author: ADMIN
"""



import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np
import time

N = 315
M = 315
population = N * M
t = 60
t_1 = 1
C = 0
aStoC = 1
bCtoS = 0.8
alpha = 1
beta = 1

start_time = time.time()

fig = plt.figure()
ax = fig.add_subplot(111)
#sim1 = app.app_sim(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1)
sim2 = app.sim_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1)
#sim3 = app.sim_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1,0,1)
#plt.plot(sim1, color='b')
plt.plot(sim2, color='r')
#plt.plot(sim3, color='g')

ax.text(1,5,'N = '+str(population), fontsize=15)

plt.title('$a = $'+str(aStoC)+' $b = $'+str(bCtoS)+r' $\alpha=$'+str(alpha)+r' $\beta=$'+str(beta),fontsize=20)
plt.xlabel('Time',fontsize=18)
plt.ylabel('State'+r' $n_{c}$',fontsize=18)
#plt.ylim(0,110)
plt.savefig('sim2.png')
plt.show()
print(sim2)
print(str(time.time() - start_time) + ' seconds')
