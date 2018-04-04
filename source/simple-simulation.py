#####################################################
#Simulates applause for a specific set of parameters#
#Displays the appropriate steady state value        #
#Parameters can be adjusted accordingly below       #
#####################################################


import applause_functions as app
import matplotlib.pyplot as plt
import numpy as np

N = 10
M = 10
population = N * M
time = 500
t_1 = 2
C = 0
aStoC = 1
bCtoS = 0.8
alpha = 0.6
beta = 1

fig = plt.figure()
ax = fig.add_subplot(111)
sim = app.app_sim(aStoC, bCtoS, alpha, beta, N, M, C, time, t_1)
plt.plot(sim)
ax.text(0.45*time,1,'Steady-state:'+str(round(app.steady_nC(aStoC, bCtoS, alpha, beta, population, 1),0)), fontsize=20)
ax.text(0.45*time,10,'Mean: '+str(round(np.mean(sim),1))+'$\pm$'+str(round(np.std(sim),2)), fontsize=20)
ax.text(10,100,'N = '+str(population), fontsize=15)
plt.axhline(np.mean(sim), color = 'r')
plt.axhline(app.steady_nC(aStoC, bCtoS, alpha, beta, population, 1), color = 'g')
plt.title('$a = $'+str(aStoC)+' $b = $'+str(bCtoS)+r' $\alpha=$'+str(alpha)+r' $\beta=$'+str(beta),fontsize=20)
plt.xlabel('Time',fontsize=18)
plt.ylabel('State'+r' $n_{c}$',fontsize=18)
plt.xlim(0,time)
plt.ylim(0,110)
plt.savefig('ssB.png')
plt.show()
