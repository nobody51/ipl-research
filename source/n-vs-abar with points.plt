#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,18"


set termopt enhanced   
unset key


N = 100.0


abarf(n,b,beta) = b*(N-1)*(N-1)/(N-n)/(N-1+n*beta)

nstarf(abar,b) = N - b/aa*(N-1)

betaf(n,b,abar) = ( b*(N-1)/abar/(N-n) - 1.0 )*(N-1)/n

bf(n,abar,beta) = abar * (N-n) * ( N-1 + n*beta ) / (N-1.0) / (N-1.0)


set parametric

set samples 5000



set xlabel "Parameter @^{/=30-}a" font "Times New Roman,24"

set ylabel "State n_{c}" font "Times New Roman,24"
beta0 = 1.0
 bb = 0.5
set key font ",19"
set key noautotitle
#set label 1 sprintf("b = %0.2f",bb) at screen 0.5,0.25 font "Times New Roman,20"

#set label 2 sprintf("{/Symbol b} = %0.2f",beta0) at screen 0.5,0.35 font "Times New Roman,20"

set key at 0.14,100
set title sprintf("b = %0.2f",bb) font "Times New Roman,26"

plot [-(N-2):N-2][0:1][-5:105] abarf(t,bb,0.1),t lw 3 title '{/Symbol b}=0.1', \
			     abarf(t,bb,1),t lw 3 title '{/Symbol b}=1', \
			     abarf(t,bb,10),t lw 3 title '{/Symbol b}=10', \
'F:\Research\points\txt\b = 0.5, beta = 0.1.txt' using 1:2:3 w yerrorbars ls 7 title 'Data', \
'F:\Research\points\txt\b = 0.5, beta = 1.txt' using 1:2:3 w yerrorbars ls 7, \
'F:\Research\points\txt\b = 0.5, beta = 10.txt' using 1:2:3 w yerrorbars ls 7, \
			     0.163,44   with points ls 2 title 'Vertex', \
			     t/N,0 lw 3 lt rgb "black"



, \