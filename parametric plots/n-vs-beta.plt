#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,24"


unset key


N = 100.0


abarf(n,b,beta) = b*(N-1)*(N-1)/(N-n)/(N-1+n*beta)

nstarf(abar,b) = N - b/aa*(N-1)

betaf(n,b,abar) = ( b*(N-1)/abar/(N-n) - 1.0 )*(N-1)/n

bf(n,abar,beta) = abar * (N-n) * ( N-1 + n*beta ) / (N-1.0) / (N-1.0)


set parametric
set samples 2000



set xlabel "Parameter {/Symbol b}" font "Times New Roman,20"

set ylabel "Limit population, {/Times-Italic n}" font "Times New Roman,20"


abar0 = 0.1 
bb = 1
#set label 1 sprintf("b = %0.2f",bb) at screen 0.5,0.25 font "Times New Roman,28"

#set label 2 sprintf("{/Times-Italic a}{/Symbol a} = %0.2f",abar0) at screen 0.5,0.35 font "Times New Roman,28"

set key at 8,-50
set title sprintf("b = %0.2f",bb) font "Times New Roman,20"
plot [-(N-2):N-2][0:10][-N:N] betaf(t,bb,0.1),t lw 3 title '{/Times-Italic a}{/Symbol a}=0.1', \
betaf(t,bb,0.25),t lw 3 title '{/Times-Italic a}{/Symbol a}=0.25', \
betaf(t,bb,0.5),t lw 3 title '{/Times-Italic a}{/Symbol a}=0.5', \
betaf(t,bb,0.75),t lw 3 title '{/Times-Italic a}{/Symbol a}=0.75', \
betaf(t,bb,0.9),t lw 3 title '{/Times-Italic a}{/Symbol a}=0.9', \
betaf(t,bb,1),t lw 3 title '{/Times-Italic a}{/Symbol a}=1', \
100*t/N,0 lw 3



