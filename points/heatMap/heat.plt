#!/usr/local/bin/gnuplot

reset


set grid
set tics font "Times New Roman,18"
set termopt enhanced   
unset key

plot [0:1][-5:105] 'b = 0.8, beta = 10, x = 11, y = 11, z = 100.txt' with image
