reset
unset key
set ylabel "Energy(keV)"
set title "Mass Parabola for A = 140 at 285.0 K"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{140}Sb ^{['0+']}" 1,"^{140}Te ^{['0+']}" 2,"^{140}I ^{['0+']}" 3,"^{140}Xe ^{['0+']}" 4,"^{140}Cs ^{['0+']}" 5,"^{140}Ba ^{['0+']}" 6,"^{140}La ^{['0+']}" 7,"^{140}Ce ^{['0+']}" 8,"^{140}Pr ^{['0+']}" 9,"^{140}Nd ^{['0+']}" 10,"^{140}Pm ^{['0+']}" 11,"^{140}Sm ^{['0+']}" 12,"^{140}Eu ^{['0+']}" 13,"^{140}Gd ^{['0+']}" 14,"^{140}Tb ^{['0+']}" 15,"^{140}Dy ^{['0+']}" 16,"^{140}Ho ^{['0+']}" 17)
set xrange [0:18]
plot "140Sb_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "140Sb_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Sb_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Te_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "140Te_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Te_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140I_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "140I_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140I_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Xe_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "140Xe_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Xe_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Cs_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "140Cs_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Cs_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Ba_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "140Ba_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Ba_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140La_Fil.dat" using (7):2:3 with labels left point offset 0.2,0
replot "140La_Fil.dat" using (7-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140La_Fil.dat" using (7-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Ce_Fil.dat" using (8):2:3 with labels left point offset 0.2,0
replot "140Ce_Fil.dat" using (8-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Ce_Fil.dat" using (8-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Pr_Fil.dat" using (9):2:3 with labels left point offset 0.2,0
replot "140Pr_Fil.dat" using (9-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Pr_Fil.dat" using (9-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Nd_Fil.dat" using (10):2:3 with labels left point offset 0.2,0
replot "140Nd_Fil.dat" using (10-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Nd_Fil.dat" using (10-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Pm_Fil.dat" using (11):2:3 with labels left point offset 0.2,0
replot "140Pm_Fil.dat" using (11-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Pm_Fil.dat" using (11-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Sm_Fil.dat" using (12):2:3 with labels left point offset 0.2,0
replot "140Sm_Fil.dat" using (12-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Sm_Fil.dat" using (12-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Eu_Fil.dat" using (13):2:3 with labels left point offset 0.2,0
replot "140Eu_Fil.dat" using (13-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Eu_Fil.dat" using (13-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Gd_Fil.dat" using (14):2:3 with labels left point offset 0.2,0
replot "140Gd_Fil.dat" using (14-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Gd_Fil.dat" using (14-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Tb_Fil.dat" using (15):2:3 with labels left point offset 0.2,0
replot "140Tb_Fil.dat" using (15-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Tb_Fil.dat" using (15-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Dy_Fil.dat" using (16):2:3 with labels left point offset 0.2,0
replot "140Dy_Fil.dat" using (16-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Dy_Fil.dat" using (16-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "140Ho_Fil.dat" using (17):2:3 with labels left point offset 0.2,0
replot "140Ho_Fil.dat" using (17-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "140Ho_Fil.dat" using (17-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 64
set output 'Large_Parabola_140_285K.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 8
set output 'Parabola_140_285K.gif'
replot
set term x11