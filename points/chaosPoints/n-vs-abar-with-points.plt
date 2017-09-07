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
 bb = 0.8
set key font ",19"
set key noautotitle
#set label 1 sprintf("b = %0.2f",bb) at screen 0.5,0.25 font "Times New Roman,20"

#set label 2 sprintf("{/Symbol b} = %0.2f",beta0) at screen 0.5,0.35 font "Times New Roman,20"

set key at 0.2,100
set title sprintf("b = %0.2f",bb) font "Times New Roman,26"

plot [-(N-2):N-2][0:1][-5:105] 	"b = 0.8, beta = 10, startPop = 5.txt" using 1:2:3 w yerrorbars ls 1 title 'startPop = 5', \
				"b = 0.8, beta = 10, startPop = 10.txt" using 1:2:3 w yerrorbars ls 2 title 'startPop = 10', \
				"b = 0.8, beta = 10, startPop = 20.txt" using 1:2:3 w yerrorbars ls 3 title 'startPop = 20', \
				"b = 0.8, beta = 10, startPop = 30.txt" using 1:2:3 w yerrorbars ls 4 title 'startPop = 30', \
				"b = 0.8, beta = 10, startPop = 40.txt" using 1:2:3 w yerrorbars ls 5 title 'startPop = 40', \
				"b = 0.8, beta = 10, startPop = 60.txt" using 1:2:3 w yerrorbars ls 7 title 'startPop = 60', \
			     	abarf(t,bb,10),t lw 3 title '{/Symbol b}=10', \
			     	t/N,0 lw 3 lt rgb "black"