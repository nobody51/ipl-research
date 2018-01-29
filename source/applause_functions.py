from random import random
from numpy import zeros, sqrt, nan_to_num
from math import isnan

#function that forces agents to go to state C
def force_func(t, end):
    if t < end:
        return 1
    else:
        return 0

#f'(alpha); feedback based on the number of ppl already in state C; the more ppl in state C, the more ppl will clap
def feedback_alpha(alpha, nC, population):
    return alpha * nC / (population - 1)
    
#g'(beta)
def feedback_beta(beta, nC, population):
    return 1 / (1 + beta * nC / (population - 1))
    
#spatial-dependent feedack, '180 degrees'    
def feedback_space(system,system_row, M):
    applause_state = [0]
    for i in range(system_row):
        applause_state.append(sum(system[i]))
    return nan_to_num(sum(applause_state)/(system_row*M))

#quadratic equation    
def quad_eq(x,y,z,sign):
    return (-y + sign * (sqrt((y ** 2) - 4 * x * z))) / 2 * x

#do i still need this??!?!
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
   
#creates 'network' of audience        
def audience(N,M,C):
    agents = zeros((N,M))
    
    for i in range(N):
        for j in range(M):
            if sum(agents) == C:
                break
            else:
                agents[i][j]=1
    
    return agents

#the actual simulator            
def app_sim(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1):
    population = N * M
    AGENT = audience(N, M, C)
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

#sim with spatial dependence    
def sim_space(aStoC, bCtoS, alpha, beta, N, M, C, t, t_1):
    population = N * M
    AGENT = audience(N, M, C)
    graph = []

    for k in range(t):
        nC = sum(AGENT) #number of people clapping
        graph.append(nC)
        for i in range(N):
            for j in range(M):
                if AGENT[i,j] == 0:
                    if random() <= aStoC * (1 - (1-force_func(k, t_1)) * (1 - feedback_space(AGENT,i, M))):
                        AGENT[i,j] += 1
                else:
                    if random() <= bCtoS * feedback_beta(beta, nC, population):
                        AGENT[i,j] -= 1
    return graph    
    
#graphs theoretical steady_state based on parameters    
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
                if isnan(quad_eq(1, ((population*aStoC*alpha*beta)-(population*aStoC*alpha)+(aStoC*alpha))/(-aStoC*alpha*beta), (((population**2)*aStoC*alpha) - (population*aStoC*alpha) - ((population**2)*bCtoS) + (2*population*bCtoS) - (bCtoS))/(-aStoC*alpha*beta), sign)) == True:
                    return 0
                else:
                    return quad_eq(1, ((population*aStoC*alpha*beta)-(population*aStoC*alpha)+(aStoC*alpha))/(-aStoC*alpha*beta), (((population**2)*aStoC*alpha) - (population*aStoC*alpha) - ((population**2)*bCtoS) + (2*population*bCtoS) - (bCtoS))/(-aStoC*alpha*beta), sign)
    
