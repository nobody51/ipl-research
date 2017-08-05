import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt
import applause_model_1 as app

N = 10
M = 10
population = N * M
time = 300 #iterations
t_1 = 25 #iterations of forcing function
AGENT = zeros((N,M)) # agent is either clapping (1) or silent (0), agent starts silent
aStoC = 0.9 #probability to start
bCtoS = 0.25 #probability to stop
alpha = 0.0
beta = 1
xgraph = []
aygraph = []
bygraph = []

for beta in app.frange(0.01,1.0,0.01):
    steady_nC_3a = quad_eq(aStoC*beta, (population-1)*bCtoS + aStoC*((population - 1)-beta*population), -(aStoC)*(population-1)*(population),1)
    steady_nC_3b = quad_eq(aStoC*beta, (population-1)*bCtoS + aStoC*((population - 1)-beta*population), -(aStoC)*(population-1)*(population),-1)

    xgraph.append(beta)
    aygraph.append(steady_nC_3a)
    bygraph.append(steady_nC_3b)
    

    
plt.plot(xgraph,aygraph, 'r')
plt.plot(xgraph,bygraph, 'g')
plt.xlim(-0.1,1)
plt.show()    
    
