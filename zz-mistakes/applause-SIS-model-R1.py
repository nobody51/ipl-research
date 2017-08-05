import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt, sum

N = 10
M = 10
population = N * M
time = 100 #iterations
t_1 = 5 #iterations of forcing function
AGENT = zeros((N,M)) # agent is either clapping (1) or silent (0), agent starts silent
aStoC = 0.9 #probability to start
bCtoS = 0.09 #probability to stop
alpha = 0.5
beta = 0.2
graph = []

def force_func(start, end):
    if start <= end:
        return 1
    else:
        return 0
        
def feedback_alpha(nC):
    return alpha * nC / (population - 1)
    
def feedback_beta(nC):
    return 1 / (1 + beta * nC / (population - 1))

def quad_eq1(x,y,z):
    return (-y + sqrt((y ** 2) - 4 * x * z)) / 2 * x
    #can be changed by all-addition formula
    
def quad_eq2(x,y,z):
    return (-y - sqrt((y ** 2) - 4 * x * z)) / 2 * x

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
steady_nC_2 = (aStoC * population * feedback_alpha(nC)) / (aStoC * feedback_alpha(nC) +bCtoS) #equation 2 for steady state with fprime
#steady_nC_2 =  population - (bCtoS * (population - 1)) / (aStoC * alpha)
steady_nC_3a = quad_eq1(1, ((population-1)*bCtoS + aStoC*((population - 1)-beta*population))/aStoC*alpha*beta, (-(aStoC)*(population-1))/aStoC*alpha*beta)
steady_nC_3b = quad_eq2(aStoC*beta, (population-1)*bCtoS + aStoC*((population - 1)-beta*population), -(aStoC)*(population-1))

print(steady_nC_1)
fig = plt.figure() #creates figure
plt.plot(graph) #plots graph, then adds to figure
#plt.axhline(steady_nC_1, color='k') #horizontal line to figure
ax = fig.add_subplot(111) #for words (see matplotlib example)
#ax.text(0.65 * t, steady_nC_1+1, steady_nC_1, fontsize=12) #labels steady state

plt.axhline(steady_nC_3a, color='r') #horizontal line to figure
ax.text(0.65 * t, steady_nC_3a+1, steady_nC_3a, fontsize=20) #labels steady state

#plt.axhline(steady_nC_3a, color='y') #horizontal line to figure


plt.title('a = '+str(aStoC)+' b = '+str(bCtoS)+' alpha = '+str(alpha)+' beta = '+str(beta))
plt.xlabel('Time')
plt.ylabel('State C')
plt.savefig('a = '+str(aStoC)+' b = '+str(bCtoS)+' alpha = '+str(alpha)+' beta = '+str(beta)+'.png')
plt.show()
