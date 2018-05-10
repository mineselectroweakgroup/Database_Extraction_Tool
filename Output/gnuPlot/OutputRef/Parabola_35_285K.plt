reset
unset key
set ylabel "Energy(keV)"
set title "Mass Parabola for A = 35 at 285.0 K"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{35}Na ^{['0+']}" 1,"^{35}Mg ^{['0+']}" 2,"^{35}Al ^{['0+']}" 3,"^{35}Si ^{['0+']}" 4,"^{35}P ^{['0+']}" 5,"^{35}S ^{['0+']}" 6,"^{35}Cl ^{['0+']}" 7,"^{35}Ar ^{['0+']}" 8,"^{35}K ^{['0+']}" 9,"^{35}Ca ^{['0+']}" 10)
set xrange [0:11]
plot "35Na_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "35Na_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Na_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Mg_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "35Mg_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Mg_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Al_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "35Al_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Al_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Si_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "35Si_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Si_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35P_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "35P_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35P_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35S_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "35S_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35S_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Cl_Fil.dat" using (7):2:3 with labels left point offset 0.2,0
replot "35Cl_Fil.dat" using (7-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Cl_Fil.dat" using (7-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Ar_Fil.dat" using (8):2:3 with labels left point offset 0.2,0
replot "35Ar_Fil.dat" using (8-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Ar_Fil.dat" using (8-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35K_Fil.dat" using (9):2:3 with labels left point offset 0.2,0
replot "35K_Fil.dat" using (9-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35K_Fil.dat" using (9-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35Ca_Fil.dat" using (10):2:3 with labels left point offset 0.2,0
replot "35Ca_Fil.dat" using (10-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35Ca_Fil.dat" using (10-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 70
set output 'Large_Parabola_35_285K.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 10
set output 'Parabola_35_285K.gif'
replot
set term x11