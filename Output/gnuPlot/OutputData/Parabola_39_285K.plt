reset
unset key
set ylabel "Energy(keV)"
set title "Mass Parabola for A = 39 at 285.0 K"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{39}Mg ^{['0+']}" 1,"^{39}Al ^{['0+']}" 2,"^{39}Si ^{['0+']}" 3,"^{39}P ^{['0+']}" 4,"^{39}S ^{['0+']}" 5,"^{39}Cl ^{['0+']}" 6,"^{39}Ar ^{['0+']}" 7,"^{39}K ^{['0+']}" 8,"^{39}Ca ^{['0+']}" 9,"^{39}Sc ^{['0+']}" 10,"^{39}Ti ^{['0+']}" 11)
set xrange [0:12]
plot "39Mg_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "39Mg_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Mg_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Al_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "39Al_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Al_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Si_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "39Si_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Si_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39P_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "39P_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39P_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39S_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "39S_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39S_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Cl_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "39Cl_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Cl_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Ar_Fil.dat" using (7):2:3 with labels left point offset 0.2,0
replot "39Ar_Fil.dat" using (7-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Ar_Fil.dat" using (7-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39K_Fil.dat" using (8):2:3 with labels left point offset 0.2,0
replot "39K_Fil.dat" using (8-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39K_Fil.dat" using (8-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Ca_Fil.dat" using (9):2:3 with labels left point offset 0.2,0
replot "39Ca_Fil.dat" using (9-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Ca_Fil.dat" using (9-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Sc_Fil.dat" using (10):2:3 with labels left point offset 0.2,0
replot "39Sc_Fil.dat" using (10-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Sc_Fil.dat" using (10-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39Ti_Fil.dat" using (11):2:3 with labels left point offset 0.2,0
replot "39Ti_Fil.dat" using (11-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39Ti_Fil.dat" using (11-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 70
set output 'Large_Parabola_39_285K.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 10
set output 'Parabola_39_285K.gif'
replot
set term x11