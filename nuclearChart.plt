reset
unset key
set xlabel "Number of Neutrons (N)"
set ylabel "Number of Protons (Z)"
set palette rgb -21,-22,-23
set datafile sep ','
set size 1,1
set pointsize 3
set xtics 10
set ytics 10
set grid
set xrange [-1:180]
set term png size 5000,4500 font "/home/matmarti/Database_Extraction_Tool/Helvetica.ttf" 50
set output "nuclearChart.png"
plot "IsotopeList.txt" using ($3-$2):2:4 with points palette pointtype 5
