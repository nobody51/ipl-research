#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,18"
set dgrid3d 20,20,20

set termopt enhanced   
unset key

plot 'b = 0.8, beta = 10, x = 11, y = 11, z = 100.txt' with image
