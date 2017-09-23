# Database_Extraction_Tool
## Version 0.6.0

### Outline of Program
The end goal of the project is to create a cohesive and intuitive set of GUIs which can be used to effectively sort through large databases for nuclear structural data and atomic binding data. This will allow for an easy, systematic study of excited nuclear states, atomic mass data, and beta decay transitions.

This program has 3 functions: 
1. Produce plots of nuclear states requested by the user.
2. Produce plots of nuclear states with beta decay data.
3. Produce a mass parabola for a given A value.

### How to get this program:
1. Download the program from the GitHub page (`git clone https://github.com/ElectroweakGroup/Database_Extraction_Tool`)
2. Install any missing dependencies. This program requires:
    * Python 3.5.2 or newer
    * gnuplot

### How to run this program:
1. Run `StartupGUI.py` (`python3 StartupGUI.py`)
2. Click on the desired function. 
3. Input appropriate values and select desired options before hitting the appropriate submit button.
4. Requested plots will appear in the GUI when it reopens, and actual data can be found in the `Outputs/gnuPlot` directory.



### How this program operates:
There are several scripts which interact with each other to produce the plots and outputs requested. When the user runs the `StartupGUI.py` program, a GUI opens asking which subscript the user wishes to run. All three options operate in the same manner, but with different requested inputs and different default values.

Upon selection of a subscript, the program will calls `Main.py` with a specific option, which sends this option to `IsotopeDataExporting.py`. This script calls one of three GUIs, `GUI.py`, `Beta_GUI.py`, or `Parabola_GUI.py`, which will ask for input specific to the function desired. The `IsotopeDataExporting.py` file then uses the `dataClass.py` file to sort through the ENSDF data files and compiles the data into a usable form.

Depending on the options provided by the user, the `Main.py` file may call `mass_data.py`, which searches through `mass16.txt` and gets atomic mass data with uncertainty, adding it to the dataset.

Upon completing the dataset, `Main.py` file calls `IsotopeDataExporting.py` again to create plot files that gnuplot uses to display the data. The program then deletes all empty data files and plots the data in gnuplot with the line thickness being the uncertainty of the state.

Finally, the `Main.py` kills the program before calling it again fresh with terminal commands.



### Plotting Symbols Legend:

\*		Extrapolated mass

\*\*		Deduced nuclear state energy

[ ]		Non-numerical uncertainty

X		Ground state with missing energy

(0+)X	Ground state of 0+, excited states with missing energy

## Version Tracking:

Version history can be found in the Change Log, [here.](http://github.com/ElectroweakGroup/Database_Extraction_Tool/blob/master/Changelog.txt)
