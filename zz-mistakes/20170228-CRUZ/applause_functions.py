import matplotlib.pyplot as plt
from random import random
from numpy import zeros, sqrt, sum


def force_func(t, end):
    if t <= end:
        return 1
    else:
        return 0
        
def feedback_alpha(alpha, nC, population):
    return alpha * nC / (population - 1)
    
def feedback_beta(beta, nC, population):
    return 1 / (1 + beta * nC / (population - 1))
    
def quad_eq(x,y,z,sign):
    return (-y + sign * (sqrt((y ** 2) - 4 * x * z))) / 2 * x

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
        
def app_sim(aStoC, bCtoS, alpha, beta, N, M, t, t_1):
    population = N * M
    AGENT = zeros((N,M))
    graph = []

    for k in range(t):
        nC = sum(AGENT) #number of people clapping
        graph.append(nC)
        for i in range(N):
            for j in range(M):
                if AGENT[i,j] == 0:
                    if random() <= aStoC * (1 - (1-force_func(k, t_1)) * (1 - feedback_alpha(alpha, nC, population))):
                        AGENT[i,j] += 1
                else:
                    if random() <= bCtoS * feedback_beta(beta, nC, population):
                        AGENT[i,j] -= 1
    return graph
    
def steady_nC(aStoC, bCtoS, alpha, beta, population, sign):
    if beta == 0:
        if alpha == 0:
            return (aStoC * population) / (aStoC+bCtoS)
        else:
            if sign == 1:
                return population - (bCtoS * (population - 1)) / (aStoC * alpha)
            else:
                return 0
    else:
        if alpha == 0:
            return 0
        else:
            if sign == 0:
                return 0
            else:
                return quad_eq(1, -((population*aStoC*alpha*beta)-(population*aStoC*alpha)+(aStoC*alpha))/(aStoC*alpha*beta), -(((population**2)*aStoC*alpha) - (population*aStoC*alpha) - ((population**2)*bCtoS) + (2*population*bCtoS) - (bCtoS))/(aStoC*alpha*beta), sign)
    
