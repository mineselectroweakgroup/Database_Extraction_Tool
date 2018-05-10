#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QDialog, QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QFrame)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5 import QtCore
import os

from StartupQt import main

" Check how tabs work when selecting buttons """
class NucEval(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.chemSymVar = ""
        self.lowBoundIsoVar = "" 
        self.upBoundIsoVar = ""

        self.spinVar = ""
        self.upBoundEnergyVar = ""

        self.exitcount = 0
      

    def initUI(self):

        pixmap = QPixmap('Output/gnuPlot/nuclearChart.gif')
        label = QLabel(self)
        label.setPixmap(pixmap)

        # Input Dialogs defined below

        self.mass = QLineEdit(self)
        self.mass.setText("Mass #")
        self.mass.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 20px 0px 20px;")

        self.loA = QLineEdit(self)
        self.loA.setText("Low A")
        self.loA.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 20px 0px 20px;")

        self.hiA = QLineEdit(self)
        self.hiA.setText("High A")
        self.hiA.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 20px 0px 20px;")

        self.energy = QLineEdit(self)
        self.energy.setText("Energy (keV)") 
        self.energy.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 10px 20px 10px 20px;")


        self.spin = QLineEdit(self)
        self.spin.setText("Spin")
        self.spin.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 10px 20px 10px 20px;")


        # Button defined below 

        submit = QPushButton("Submit", self)
        submit.clicked.connect(self.submitClicked)
        submit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin: 0px 25px 0px 25px; padding: 0px 15px 0px 15px;")
        submit.installEventFilter(self) 


        full = QPushButton("Full", self)
        full.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")      
        full.installEventFilter(self)      


        main = QPushButton("Main", self)
        main.clicked.connect(self.mainClicked)
        main.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")                
        main.installEventFilter(self)      


        exit = QPushButton("Exit", self)
        exit.clicked.connect(QApplication.instance().quit)
        exit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin-left: 25px; margin-right: 25px;")                
        exit.installEventFilter(self)      

       
        # GRID LAYOUT 

        grid = QGridLayout()
        self.setLayout(grid)

        topGrid = QGridLayout()

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setLineWidth(2)

        line2 = QFrame()
        line2.setFrameStyle(QFrame.HLine)
        line2.setLineWidth(2)

        topGrid.addWidget(full, 0, 4)
        topGrid.addWidget(main, 0, 5)
        topGrid.addWidget(exit, 0, 6)
        topGrid.setSpacing(40)

        botGrid = QGridLayout()
        botGrid.addWidget(self.mass, 0, 1)
        botGrid.addWidget(self.loA, 0, 2)
        botGrid.addWidget(self.hiA, 0, 3)
        botGrid.addWidget(self.energy, 0, 4)
        botGrid.addWidget(self.spin, 0, 5)
        botGrid.addWidget(submit, 0, 6)
        botGrid.setColumnMinimumWidth(80, 0)    

        grid.addLayout(topGrid, 0, 0)
        grid.addWidget(line, 1, 0, 1, 6)
        grid.addWidget(label, 2, 0)
        grid.addWidget(line2, 3, 0, 1, 6)
        grid.addLayout(botGrid, 4, 0)

        self.setGeometry(300, 300, 500, 420) #x coord, y coord, width, height
        self.setWindowTitle('Evaluated Nuclear Structure Data')
        self.setStyleSheet("background-color: white")

        #self.exec_()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            object.setStyleSheet("background-color:#1E555C; color:#EBEEF2; border:1px solid #1E555C; border-radius:5px; height:25px; margin: 0px 25px 0px 25px;padding: 0px 15px 0px 15px;")
            return True;
        if event.type() == QtCore.QEvent.HoverLeave:
            object.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px; margin: 0px 25px 0px 25px;padding: 0px 15px 0px 15px;")
        return False;


    def submitClicked(self):
        """Send user input to nuclear structure sorting function"""
        #from IsotopeDataExporting import datExp
        self.chemSymVar = self.mass.text()
        self.lowBoundIsoVar = self.loA.text()
        self.upBoundIsoVar = self.hiA.text()
        self.spinVar = self.spin.text()
        self.upBoundEnergyVar = self.energy.text()
        self.accept()

    def mainClicked(self):
        # 
        self.checmSymVar = "Zn"
        self.A = 10
        self.spinVar = "0+"
        self.exitCount = 1
        self.close()
        os.system("python3 StartupQt.py")
        #main()
        #print("main")


app = QApplication(sys.argv)
ex = NucEval()
ex.exec_()
#sys.exit(app.exec_())
app.exec_()

#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

class guioutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    Z=ex.chemSymVar
    try:
        Z=Z.upper()
    except:
        pass
    isoLow=ex.lowBoundIsoVar
    J=ex.spinVar
    isoUp=ex.upBoundIsoVar
    E=ex.upBoundEnergyVar
    exitcount=ex.exitcount

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if exitcount == 1:
        sys.exit()
    if Z == '' or Z == 'Mass #':
        print("Enter valid mass value.")
        sys.exit()
    if isoLow == '' or isoLow == "Low A":
        isoLow = 1
    if isoUp == '' or isoUp == "High A":
        isoUp = 299
    if E == '' or E == "Energy (keV)":
        E = 9999999
    mass = "NO"

