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

N = 10
M = 10
population = N * M
t = 500
t_1 = 1
C = 0
aStoC = 0.7
bCtoS = 0.8
alpha = 0.5
beta = 4

start_time = time.time()

fig = plt.figure()
ax = fig.add_subplot(111)
sim1 = app.app_sim(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1)
sim2 = app.feed_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1,M,0)
sim3 = app.feed_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1,0,1)
sim4 = app.feed_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1,0,0)
plt.plot(sim1, color='b', label="FC")
plt.plot(sim2, color='r', label="180deg")
plt.plot(sim3, color='g', label="90deg")
plt.plot(sim4, color='y', label="0deg")
plt.legend(loc=4)

ax.text(1,5,'N = '+str(population), fontsize=15)

plt.title('$a = $'+str(aStoC)+' $b = $'+str(bCtoS)+r' $\alpha=$'+str(alpha)+r' $\beta=$'+str(beta),fontsize=20)
plt.xlabel('Time',fontsize=18)
plt.ylabel('State'+r' $n_{c}$',fontsize=18)
plt.xlim(0,30)
plt.ylim(0,110)
plt.savefig('feedback_sim7.png')
plt.show()
#print(sim2)
#print(str(time.time() - start_time) + ' seconds')
