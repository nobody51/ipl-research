#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,18"
set termopt enhanced  
unset key

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N = 100.0

abarf(n,b,beta) = b*(N-1)*(N-1)/(N-n)/(N-1+n*beta)

nstarf(abar,b) = N - b/aa*(N-1)

betaf(n,b,abar) = ( b*(N-1)/abar/(N-n) - 1.0 )*(N-1)/n

bf(n,abar,beta) = abar * (N-n) * ( N-1 + n*beta ) / (N-1.0) / (N-1.0)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
set xlabel "Parameter @^{/=30-}a" font "Times New Roman,24"
set ylabel "State n_{c}" font "Times New Roman,24"
set key at 0.6,100
set title sprintf("b = %0.2f",bb) font "Times New Roman,26"

set multiplot

#set palette model XYZ rgbformulae 7,5,15
set size 1,1
set origin 0,0
plot [0:1][-5:105] 'b = 0.8, beta = 10, x = 11, y = 11, z = 10.txt' using 1:2:3:4 with vectors head filled lt 2

set size 1,1
set origin 0,0
set parametric
set samples 5000
beta0 = 1.0
bb = 0.8
plot [-(N-2):N-2][0:1][-5:105] 	abarf(t,bb,10),t lw 3 lt rgb "blue" title '{/Symbol b}=10', \
				t,0 lw 3 lt rgb "black" title 'trivial solution'
								
unset multiplot





								
