reset
unset key
set title `head -1 "IsotopeList.txt"`
set xlabel "Number of Neutrons (N)"
set ylabel "Number of Protons (Z)"
set palette defined (0 'black', 1 'red', 2 'orange', 3 'yellow', 4 'green', 5 'blue')
set nocolorbox
set datafile sep ','
set size 1,1
set pointsize 3
set xtics 10
set ytics 10
set grid
set xrange [-1:180]
set term png size 5000,3000 font "/home/matmarti/Database_Extraction_Tool/Helvetica.ttf" 50
set output "nuclearChart.png"

set arrow 1 from 1.5, graph 0 to 1.5, graph 1 nohead linewidth 2
set arrow 2 from 2.5, graph 0 to 2.5, graph 1 nohead linewidth 2
set arrow 3 from 7.5, graph 0 to 7.5, graph 1 nohead linewidth 2
set arrow 4 from 8.5, graph 0 to 8.5, graph 1 nohead linewidth 2
set arrow 5 from 19.5, graph 0 to 19.5, graph 1 nohead linewidth 2
set arrow 6 from 20.5, graph 0 to 20.5, graph 1 nohead linewidth 2
set arrow 7 from 27.5, graph 0 to 27.5, graph 1 nohead linewidth 2
set arrow 8 from 28.5, graph 0 to 28.5, graph 1 nohead linewidth 2
set arrow 9 from 49.5, graph 0 to 49.5, graph 1 nohead linewidth 2
set arrow 10 from 50.5, graph 0 to 50.5, graph 1 nohead linewidth 2
set arrow 11 from 81.5, graph 0 to 81.5, graph 1 nohead linewidth 2
set arrow 12 from 82.5, graph 0 to 82.5, graph 1 nohead linewidth 2
set arrow 13 from 125.5, graph 0 to 125.5, graph 1 nohead linewidth 2
set arrow 14 from 126.5, graph 0 to 126.5, graph 1 nohead linewidth 2

set arrow 15 from graph 0, first 1.5 to graph 1, first 1.5 nohead linewidth 2
set arrow 16 from graph 0, first 2.5 to graph 1, first 2.5 nohead linewidth 2
set arrow 17 from graph 0, first 7.5 to graph 1, first 7.5 nohead linewidth 2
set arrow 18 from graph 0, first 8.5 to graph 1, first 8.5 nohead linewidth 2
set arrow 19 from graph 0, first 19.5 to graph 1, first 19.5 nohead linewidth 2
set arrow 20 from graph 0, first 20.5 to graph 1, first 20.5 nohead linewidth 2
set arrow 21 from graph 0, first 27.5 to graph 1, first 27.5 nohead linewidth 2
set arrow 22 from graph 0, first 28.5 to graph 1, first 28.5 nohead linewidth 2
set arrow 23 from graph 0, first 49.5 to graph 1, first 49.5 nohead linewidth 2
set arrow 24 from graph 0, first 50.5 to graph 1, first 50.5 nohead linewidth 2
set arrow 25 from graph 0, first 81.5 to graph 1, first 81.5 nohead linewidth 2
set arrow 26 from graph 0, first 82.5 to graph 1, first 82.5 nohead linewidth 2

plot "IsotopeList.txt" using 1:2:3 with points palette pointtype 5
