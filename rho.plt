set style data linespoints

plot 'build/0.dat' using 1:2, \
     'build/dt.dat' using 1:2, \
     'build/1.dat' using 1:2
