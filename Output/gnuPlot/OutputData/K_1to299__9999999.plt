reset
unset key
set ylabel "Energy(keV)"
set title "Excited States of ^{1}K to ^{299}K with  Spins up to 9999999 keV"
set datafile sep ';'
set pointsize 0.0001
set label "* Extrapolated Mass" at graph 0.01, graph 0.97 left
set xtics right rotate by 45 ("^{33}K ^{}" 1,"^{34}K ^{}" 2,"^{35}K ^{}" 3,"^{36}K ^{}" 4,"^{37}K ^{}" 5,"^{38}K ^{}" 6,"^{39}K ^{}" 7,"^{40}K ^{}" 8,"^{41}K ^{}" 9,"^{42}K ^{}" 10,"^{43}K ^{}" 11,"^{44}K ^{}" 12,"^{45}K ^{}" 13,"^{46}K ^{}" 14,"^{47}K ^{}" 15,"^{48}K ^{}" 16,"^{49}K ^{}" 17,"^{50}K ^{}" 18,"^{51}K ^{}" 19,"^{52}K ^{}" 20,"^{53}K ^{}" 21,"^{54}K ^{}" 22,"^{55}K ^{}" 23,"^{56}K ^{}" 24)
set xrange [0:25]
plot "33K_Fil.dat" using (1):2:3 with labels left point offset 0.2,0
replot "33K_Fil.dat" using (1-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "33K_Fil.dat" using (1-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "34K_Fil.dat" using (2):2:3 with labels left point offset 0.2,0
replot "34K_Fil.dat" using (2-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "34K_Fil.dat" using (2-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "35K_Fil.dat" using (3):2:3 with labels left point offset 0.2,0
replot "35K_Fil.dat" using (3-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "35K_Fil.dat" using (3-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "36K_Fil.dat" using (4):2:3 with labels left point offset 0.2,0
replot "36K_Fil.dat" using (4-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "36K_Fil.dat" using (4-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "37K_Fil.dat" using (5):2:3 with labels left point offset 0.2,0
replot "37K_Fil.dat" using (5-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "37K_Fil.dat" using (5-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "38K_Fil.dat" using (6):2:3 with labels left point offset 0.2,0
replot "38K_Fil.dat" using (6-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "38K_Fil.dat" using (6-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "39K_Fil.dat" using (7):2:3 with labels left point offset 0.2,0
replot "39K_Fil.dat" using (7-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "39K_Fil.dat" using (7-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "40K_Fil.dat" using (8):2:3 with labels left point offset 0.2,0
replot "40K_Fil.dat" using (8-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "40K_Fil.dat" using (8-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "41K_Fil.dat" using (9):2:3 with labels left point offset 0.2,0
replot "41K_Fil.dat" using (9-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "41K_Fil.dat" using (9-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "42K_Fil.dat" using (10):2:3 with labels left point offset 0.2,0
replot "42K_Fil.dat" using (10-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "42K_Fil.dat" using (10-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "43K_Fil.dat" using (11):2:3 with labels left point offset 0.2,0
replot "43K_Fil.dat" using (11-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "43K_Fil.dat" using (11-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "44K_Fil.dat" using (12):2:3 with labels left point offset 0.2,0
replot "44K_Fil.dat" using (12-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "44K_Fil.dat" using (12-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "45K_Fil.dat" using (13):2:3 with labels left point offset 0.2,0
replot "45K_Fil.dat" using (13-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "45K_Fil.dat" using (13-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "46K_Fil.dat" using (14):2:3 with labels left point offset 0.2,0
replot "46K_Fil.dat" using (14-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "46K_Fil.dat" using (14-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "47K_Fil.dat" using (15):2:3 with labels left point offset 0.2,0
replot "47K_Fil.dat" using (15-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "47K_Fil.dat" using (15-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "48K_Fil.dat" using (16):2:3 with labels left point offset 0.2,0
replot "48K_Fil.dat" using (16-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "48K_Fil.dat" using (16-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "49K_Fil.dat" using (17):2:3 with labels left point offset 0.2,0
replot "49K_Fil.dat" using (17-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "49K_Fil.dat" using (17-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "50K_Fil.dat" using (18):2:3 with labels left point offset 0.2,0
replot "50K_Fil.dat" using (18-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "50K_Fil.dat" using (18-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "51K_Fil.dat" using (19):2:3 with labels left point offset 0.2,0
replot "51K_Fil.dat" using (19-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "51K_Fil.dat" using (19-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "52K_Fil.dat" using (20):2:3 with labels left point offset 0.2,0
replot "52K_Fil.dat" using (20-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "52K_Fil.dat" using (20-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "53K_Fil.dat" using (21):2:3 with labels left point offset 0.2,0
replot "53K_Fil.dat" using (21-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "53K_Fil.dat" using (21-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "54K_Fil.dat" using (22):2:3 with labels left point offset 0.2,0
replot "54K_Fil.dat" using (22-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "54K_Fil.dat" using (22-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "55K_Fil.dat" using (23):2:3 with labels left point offset 0.2,0
replot "55K_Fil.dat" using (23-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "55K_Fil.dat" using (23-0.75):2:(0.75):(0) with vectors nohead linecolor -1
replot "56K_Fil.dat" using (24):2:3 with labels left point offset 0.2,0
replot "56K_Fil.dat" using (24-0.375):2:(0.375):4 with boxxyerrorbars linecolor rgb 'black' fillstyle solid
replot "56K_Fil.dat" using (24-0.75):2:(0.75):(0) with vectors nohead linecolor -1
set term png size 5600,4000
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 95"
set term png enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 56
set output 'Large_K_1to299__9999999.png'
replot
set term gif size 840,600
set title font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf, 15"
set term gif enhanced font "/home/yanina/Documents/Spring 2018/PHGN 482/CENDET/Helvetica.ttf" 7
set output 'K_1to299__9999999.gif'
replot
set term x11