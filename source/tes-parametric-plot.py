# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:27:23 2017

@author: Anton Cruz
"""
import matplotlib.pylab as plt
import numpy as np
import sys, getopt, random

alpha = 0.7
N = 100
b = 0.3

def class2(n, beta):
    #return alpha*np.sin(t+beta)*np.sin(3*t), alpha*np.cos(t+beta)*np.sin(3*t)
    return b*(N-1)*(N-1)/(N-n)/(N-1+n*beta)

for beta in [1, 5, 10]:
    plt.plot(np.linspace(0, np.pi, 100), class2(np.linspace(0, np.pi, 100),beta),
               label='$\\beta={:.3f}$'.format(beta))
plt.legend()
plt.show()

