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
beta0 = 100
bb = 0.9

set xlabel "Parameter @^{/=30-}a" font "Times New Roman,24"
set ylabel "State n_{c}" font "Times New Roman,24"
set title sprintf("b = %0.2f",bb) font "Times New Roman,26"
set multiplot

load 'plasma.plt'
set palette positive
set size 0.997,1
set origin 0,0
unset key
set cbrange [0:1]
plot [0:1][-5:105] 'b = 0.9, beta = 100, x = 21, y = 21, z = 500.txt' with vectors lw 3 lc palette

set size 0.8867,1
set origin 0,0
set key at 0.13,100
set parametric
set samples 5000
plot [-(N-2):N-2][0:1][-5:105] 	abarf(t,bb,beta0),t lw 3 lt rgb "blue" title '{/Symbol b}=100', \
				t,0 lw 3 lt rgb "black" title 'trivial solution'
								
unset multiplot





								
