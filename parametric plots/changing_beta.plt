#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,24"


set termopt enhanced   



N = 100.0


abarf(n,b,beta) = b*(N-1)*(N-1)/(N-n)/(N-1+n*beta)

nstarf(abar,b) = N - b/aa*(N-1)

betaf(n,b,abar) = ( b*(N-1)/abar/(N-n) - 1.0 )*(N-1)/n

bf(n,abar,beta) = abar * (N-n) * ( N-1 + n*beta ) / (N-1.0) / (N-1.0)


set parametric
set samples 5000
set xlabel "Parameter @^{/=32-}a" font "Times New Roman,26"
set ylabel "State n_{c}" offset -2,0 font "Times New Roman,26"

############
beta0 = 0.05
bb = 0.5
############

set key font ",19"
set key bottom right
set title sprintf("{/Symbol b} = %0.2f",beta0) font "Times New Roman,26"

plot [-N*10:N*10][0:1][-N*0.15:N] abarf(t,bb,beta0),t lw 3 lt 3 title 'non-trivial', \
			    t/N,0 lw 3 lt 8 title 'trivial'



