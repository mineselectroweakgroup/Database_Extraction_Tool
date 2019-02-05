reset
unset key
set ylabel "Energy(keV)"
set title "Mass Parabola for A = 10 at 0.0 K"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{10}He ^{['0+']}" 1,"^{10}Li ^{['0+']}" 2,"^{10}Be ^{['0+']}" 3,"^{10}B ^{['0+']}" 4,"^{10}C ^{['0+']}" 5,"^{10}N ^{['0+']}" 6)
set xrange [0:7]
plot "10He_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "10He_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10He_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "10Li_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "10Li_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10Li_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "10Be_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "10Be_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10Be_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "10B_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "10B_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10B_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "10C_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "10C_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10C_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "10N_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "10N_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "10N_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 80
set output 'Large_Parabola_10_0K.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 12
set output 'Parabola_10_0K.gif'
replot
set term x11