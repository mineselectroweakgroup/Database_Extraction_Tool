# CENDET - Complete Evaluated Nuclear Database Extraction Tool
## Version 0.6.1

### Referencing CENDET
CENDET Extraction Program, Ver. 0.6.1, *Colorado School of Mines*, 2017

### Outline of Program
The end goal of the **Complete Evaluated Nuclear Database Extraction Tool** (CENDET) project is to create a cohesive and intuitive set of GUIs which can be used to effectively sort through large databases for nuclear structural data and atomic binding data. This will allow for an easy, systematic study of excited nuclear states, atomic mass data, and beta decay transitions.

The primary source for data are the **Evaluated Nuclear Structure Database Files (ENSDF)** provided by the National Nuclear Data Center at Brookhaven National Laboratory. Fron ENSDF, CENET extracts data from the adopted Level, Gamma, and Beta/EC records. Ionization data is provided by the **National Institute of Standards and Technology** (NIST) and atomic mass data is provided by the **Atomic Mass Data Center** (AMDC).

CENDET has 3 programs: 
1. Produce plots of nuclear states requested by the user.
2. Produce plots of nuclear states with beta decay data.
3. Produce a mass parabola for a given A value.

For each program, generated plots and data files are written to the `Output/gnuPlot` directory.

### How to get CENDET:
There are two ways to get CENDET. You can click on the download link on the GitHub page, or you can download the program with Git. If you do not have Git installed, open your Linux terminal and run `sudo apt-get install git`. With Git installed, run `git clone https://github.com/ElectroweakGroup/Database_Extraction_Tool` to download the program files to your system.

CENDET has the following dependencies:

* Python 3.5.2 or newer
* gnuplot
* Okular (optional: only needed for viewing graphs fullscreen from within CENDET)

To install these packages, run the following commands in your terminal.
```
sudo apt-get install python3
sudo apt-get install gnuplot
sudo apt-get install okular
```
### How to run CENDET:
1. Run `StartupGUI.py` (`python3 StartupGUI.py` in your terminal).
2. Click on the desired function. 
3. Input appropriate values and select desired options before hitting the appropriate submit button.
4. Requested plots will appear in the GUI when it reopens, and actual data can be found in the `Outputs/gnuPlot` directory.



### How CENDET operates:
There are several scripts which interact with each other to produce the plots and outputs requested. When the user runs the `StartupGUI.py` program, a GUI opens asking which subscript the user wishes to run. All three options operate in the same manner, but with different requested inputs and different default values.

Upon selection of a subscript, CENDET will calls `Main.py` with a specific option, which sends this option to `IsotopeDataExporting.py`. This script calls one of three GUIs, `GUI.py`, `Beta_GUI.py`, or `Parabola_GUI.py`, which will ask for input specific to the function desired. The `IsotopeDataExporting.py` file then uses the `dataClass.py` file to sort through the ENSDF data files and compiles the data into a usable form.

Depending on the options provided by the user, the `Main.py` file may then call `mass_data.py`, which searches through `mass16.txt` and gets atomic mass data with uncertainty, adding it to the dataset.

Upon completing the dataset, `Main.py` file calls `IsotopeDataExporting.py` again to create plot files that gnuplot uses to display the data. CENDET then deletes all empty data files and plots the data in gnuplot with the line thickness being the uncertainty of the state.

Finally, the `Main.py` kills CENDET before calling it again fresh with terminal commands.



### Plotting Symbols Legend:

\*		Extrapolated mass

\*\*		Deduced nuclear state energy

[ ]		Non-numerical uncertainty

X		Ground state with missing energy

(0+)X	Ground state of 0+, excited states with missing energy

## Version Tracking:

Version history can be found in the Change Log, [here.](http://github.com/ElectroweakGroup/Database_Extraction_Tool/blob/master/Changelog.txt)

### Contact Info:
Comments, questions, or other feedback? Reach us at electroweakgroup@gmail.com
