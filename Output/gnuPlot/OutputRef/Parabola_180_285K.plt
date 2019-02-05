reset
unset key
set ylabel "Energy(keV)"
set title "Mass Parabola for A = 180 at 285.0 K"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{180}Tm ^{['0+']}" 1,"^{180}Yb ^{['0+']}" 2,"^{180}Lu ^{['0+']}" 3,"^{180}Hf ^{['0+']}" 4,"^{180}Ta ^{['0+']}" 5,"^{180}W ^{['0+']}" 6,"^{180}Re ^{['0+']}" 7,"^{180}Os ^{['0+']}" 8,"^{180}Ir ^{['0+']}" 9,"^{180}Pt ^{['0+']}" 10,"^{180}Au ^{['0+']}" 11,"^{180}Hg ^{['0+']}" 12,"^{180}Tl ^{['0+']}" 13,"^{180}Pb ^{['0+']}" 14)
set xrange [0:15]
plot "180Tm_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "180Tm_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Tm_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Yb_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "180Yb_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Yb_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Lu_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "180Lu_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Lu_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Hf_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "180Hf_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Hf_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Ta_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "180Ta_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Ta_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180W_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "180W_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180W_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Re_Fil.dat" using (7):2:3 with labels left point offset 0.2,0
replot "180Re_Fil.dat" using (7-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Re_Fil.dat" using (7-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Os_Fil.dat" using (8):2:3 with labels left point offset 0.2,0
replot "180Os_Fil.dat" using (8-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Os_Fil.dat" using (8-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Ir_Fil.dat" using (9):2:3 with labels left point offset 0.2,0
replot "180Ir_Fil.dat" using (9-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Ir_Fil.dat" using (9-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Pt_Fil.dat" using (10):2:3 with labels left point offset 0.2,0
replot "180Pt_Fil.dat" using (10-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Pt_Fil.dat" using (10-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Au_Fil.dat" using (11):2:3 with labels left point offset 0.2,0
replot "180Au_Fil.dat" using (11-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Au_Fil.dat" using (11-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Hg_Fil.dat" using (12):2:3 with labels left point offset 0.2,0
replot "180Hg_Fil.dat" using (12-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Hg_Fil.dat" using (12-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Tl_Fil.dat" using (13):2:3 with labels left point offset 0.2,0
replot "180Tl_Fil.dat" using (13-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Tl_Fil.dat" using (13-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "180Pb_Fil.dat" using (14):2:3 with labels left point offset 0.2,0
replot "180Pb_Fil.dat" using (14-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "180Pb_Fil.dat" using (14-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 70
set output 'Large_Parabola_180_285K.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 10
set output 'Parabola_180_285K.gif'
replot
set term x11