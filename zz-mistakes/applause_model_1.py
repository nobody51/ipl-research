import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt, sum

N = 10
M = 100
population = N * M
time = 300 #iterations
t_1 = 25 #iterations of forcing function
AGENT = zeros((N,M)) # agent is either clapping (1) or silent (0), agent starts silent
aStoC = 0.9 #probability to start
bCtoS = 0.25 #probability to stop
alpha = 0.0
beta = 0.9
graph = []

def force_func(start, end):
    if start <= end:
        return 1
    else:
        return 0
        
def feedback_alpha(nC):
    return alpha * ( ( nC / (population - 1) )**1.5 )
    
def feedback_beta(nC):
    return 1 / (1 + beta * (nC / (population - 1))**1.5 )
    
def quad_eq(x,y,z,sign):
    return (-y + sign * (sqrt((y ** 2) - 4 * x * z))) / 2 * x

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

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

steady_nC_1 = (aStoC * population) / (aStoC+bCtoS) #equation 1 for steady state in research ntbk
if alpha!=0:
    steady_nC_2 =  population - (bCtoS * (population - 1)) / (aStoC * alpha) #equation 2 for steady state with fprime
else:
    steady_nC_2 = 0.0

steady_nC_3a = quad_eq(aStoC*beta, (population-1)*bCtoS + aStoC*((population - 1)-beta*population), -(aStoC)*(population-1)*(population),1)
steady_nC_3b = quad_eq(aStoC*beta, (population-1)*bCtoS + aStoC*((population - 1)-beta*population), -(aStoC)*(population-1)*(population),-1)

print(steady_nC_1)
fig = plt.figure() #creates figure
plt.plot(graph) #plots graph, then adds to figure
plt.axhline(steady_nC_1, color='k') #horizontal line to figure
ax = fig.add_subplot(111) #for words (see matplotlib example)
#ax.text(0.65 * t, steady_nC_1+1, steady_nC_1, fontsize=12) #labels steady state

plt.axhline(steady_nC_2, color='r') #horizontal line to figure
#ax.text(65 * t, steady_nC_2+1, steady_nC_2, fontsize=12) #labels steady state

plt.axhline(steady_nC_3a, color='y') #horizontal line to figure
plt.axhline(steady_nC_3b, color='g') #horizontal line to figure


plt.show()
