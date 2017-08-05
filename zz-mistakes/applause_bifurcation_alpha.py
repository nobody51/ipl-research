import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt
import applause_functions as app

N = 10
M = 10
population = N * M
time = 300 #iterations
t_1 = 25 #iterations of forcing function
AGENT = zeros((N,M)) # agent is either clapping (1) or silent (0), agent starts silent
aStoC = 0.9 #probability to start
bCtoS = 0.25 #probability to stop
alpha = 0.5
beta = 0
xgraph = []
ygraph = []

steady_nC_2 =  population - (bCtoS * (population - 1)) / (aStoC * alpha) #equation 2 for steady state with fprime

for alpha in app.frange(0.01,1.0,0.01):
    steady_nC_2 = app.steady_nC(aStoC, bCtoS, i, beta, population, 1)
    xgraph.append(alpha)
    ygraph.append(steady_nC_2)
    

    
plt.plot(xgraph,ygraph)
plt.axhline(0, color='b')
plt.ylim(-100,100)
plt.show()    

