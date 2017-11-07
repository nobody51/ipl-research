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
set multiplot

set palette model CMY rgbformulae 7,5,15
set size 1,1
set origin 0,0
plot [0:1][-5:105] 'b = 0.8, beta = 10, x = 11, y = 11, z = 100.txt' with image

set size 0.889,1
set origin 0,0
set parametric
set samples 5000
beta0 = 1.0
bb = 0.8
plot [-(N-2):N-2][0:1][-5:105] 	abarf(t,bb,10),t lw 3 title '{/Symbol b}=10'
								#t/N,0 lw 3 lt rgb "black"
								
unset multiplot



								
