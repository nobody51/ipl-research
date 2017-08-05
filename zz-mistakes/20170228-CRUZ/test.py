import applause_functions as app
import matplotlib.pyplot as plt


N = 10
M = 10
time = 1000
t_1 = 3
aStoC = 1.0
bCtoS = 0.1 
alpha = 0.5
beta = 0.5

def lol(aStoC, bCtoS, alpha, beta, population, color):

    xgraph = []
    ygraph = []
    y2graph= []

    for v in app.frange(0.01,1.01,0.01): #v -> parameter to be varied; for this case, alpha
        steady_nC_1 = app.steady_nC(aStoC, bCtoS, v, beta, N*M, 1)
        steady_nC_2 = app.steady_nC(aStoC, bCtoS, v, beta, N*M, -1)
        xgraph.append(v)
        ygraph.append(steady_nC_1)
        y2graph.append(steady_nC_2)
    
   
    plt.plot(xgraph,ygraph, color=color, label=beta)
    plt.plot(xgraph,y2graph, color=color)
    plt.axhline(app.steady_nC(aStoC, bCtoS, alpha, beta, N*M, 0), color='b')


for y in np.arange(0,1.0,0.1):
   for x in np.arange(0,1.0,0.1):

   
       lol(y, x, alpha, 0.1, N*M,'r')
       lol(y, x, alpha, 0.3, N*M,'c')
       lol(y, x, alpha, 0.5, N*M,'y')
       lol(y, x, alpha, 0.7, N*M,'m')
       lol(y, x, alpha, 0.9, N*M,'g')
       plt.legend(loc = 3)
       plt.xlabel('alpha')
       plt.ylabel('steady nC')
       plt.title('a = ' + str(y) + ', b = ' + str(x))
       figure = plt.gcf()
       plt.savefig('a = ' + str(y) + 'b = ' + str(x) + '.png', dpi=100)
       plt.show()
       
#plt.plot(app.app_sim(aStoC, bCtoS, alpha, beta, N, M, t, t_1))
#plt.show()


