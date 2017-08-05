import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sum

N = 30
M = 20
population = N * M
time = 100 #iterations
t_1 = 20 #iterations of forcing function
AGENT = zeros((N,M)) # agent is either clapping (1) or silent (0), agent starts silent
aStoC = 0.8 #probability to start
bCtoS = 0.6 #probability to stop
alpha = 0.1
beta = 0.0
graph = []

def force_func(t, end):
    if t <= end:
        return 1
    else:
        return 0
        
def feedback_alpha(nC):
    return alpha * nC / (population - 1)
    
def feedback_beta(nC):
    return 1 / (1 + beta * nC / (population - 1))

for t in range(time):
    nC = sum(AGENT) #number of people clapping
    graph.append(nC)
    for i in range(N):
        for j in range(M):
            if AGENT[i,j] == 0:
                if random() <= aStoC * (1 - (1-force_func(t, t_1)) * (1 - feedback_alpha(nC))):
                    AGENT[i,j] += 1
            else:
                if random() <= bCtoS * feedback_beta(nC):
                    AGENT[i,j] -= 1

plt.plot(graph)
#plt.ylim(0,6)
plt.show()
