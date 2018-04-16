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
beta0 = 0.25
bb = 1.00
############

set key font ",19"
set key outside top right
set title sprintf("b = %0.2f",bb) font "Times New Roman,26"

plot [-N:N][0:1][-N*0.15:N] abarf(t,bb,0.1),t lw 3 title '{/Symbol b}=0.1', \
			     	  abarf(t,bb,0.5),t lw 3 title '{/Symbol b}=0.5', \
			     	  abarf(t,bb,1),t lw 3 title '{/Symbol b}=1', \
		     	  	  abarf(t,bb,3),t lw 3 title '{/Symbol b}=3', \
			     	  abarf(t,bb,5),t lw 3 title '{/Symbol b}=5', \
			     	  abarf(t,bb,10),t lw 3 title '{/Symbol b}=10', \
			     	  abarf(t,bb,100),t lw 3 title '{/Symbol b}=100', \
			    	  t/N,0 lw 3 lt 8 title 'trivial'



