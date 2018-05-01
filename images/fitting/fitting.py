# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:24:36 2018

@author: ADMIN
"""
import matplotlib.pyplot as plt
import numpy as np

real  = np.loadtxt('realData.txt')
realSize = real[:,0]
realApplause = real[:,1]
realSTD = real[:,2]

sim = np.loadtxt('simData.txt')
simSize = sim[:,0]
simApplause = sim[:,1]
simSTD = sim[:,2]

fig = plt.figure()
ax = fig.add_subplot(111,xscale="log") 
x = realSize 
y = realApplause 
z = 2.223*np.log(x)-0.0607
plt.errorbar(x, y, xerr=0, yerr=realSTD, fmt='o', color='black')
plt.plot(x,z,color='r') 
ax.text(1000,10,'$2.223ln(x)-0.0607$', fontsize=15)
ax.text(1000,6,'$R^2 = 0.882$', fontsize=15)
plt.title('Real Applause',fontsize=18)
plt.xlabel('Audience Size',fontsize=15)
plt.ylabel('Applause Duration',fontsize=15)
plt.savefig('real.png')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,xscale="log") 
x = simSize 
y = simApplause
z = 2.1875*np.log(x)+0.8159
plt.errorbar(x, y, xerr=0, yerr=simSTD, fmt='o',color='black') 
plt.plot(x,z,color='r')
ax.text(2000,13,'$2.1875ln(x)+0.8159$', fontsize=15)
ax.text(2000,11,'$R^2 = 0.9715$', fontsize=15)
plt.title('Simulated Applause',fontsize=18)
plt.xlabel('Audience Size',fontsize=15)
plt.ylabel('Applause Duration',fontsize=15)
plt.savefig('sim.png')
plt.show()