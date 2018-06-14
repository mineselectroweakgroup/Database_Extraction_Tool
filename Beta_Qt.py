#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QDialog, QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QFrame)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5 import QtCore

import os

""" Check how tabs work when selecting buttons """
class BetaDecay(QDialog):

    def __init__(self, gif):
        super().__init__()

        self.initUI(gif)

        self.chemSymVar = ""
        self.A = ""
        self.energyVar = ""
        self.tempVar = ""
        self.betaVar = ""
      

    def initUI(self, gif):

        plotGif = gif or 'Output/gnuPlot/nuclearChart.gif'
        pixmap = QPixmap(plotGif)
        label = QLabel(self)
        label.setPixmap(pixmap)

       
        #Input Dialogs
        self.mass = QLineEdit(self)
        self.mass.setText("Mass #")
        self.mass.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        self.element = QLineEdit(self)
        self.element.setText("Element")
        self.element.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        self.temp = QLineEdit(self)
        self.temp.setText("Temp (K)")
        self.temp.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        self.energy = QLineEdit(self)
        self.energy.setText("Energy (keV)") 
        self.energy.setStyleSheet("border: 1px solid #2B4570; border-radius:5px; width: 25px; height: 25px; margin: 0px 25px 0px 25px;")

        # Combo box
        self.beta = QComboBox(self)
        self.beta.addItem("B+")
        self.beta.addItem("B-")
#        self.beta.setStyleSheet("color:#2B4570; border: 1px solid #2B4570; border-radius:5px;")

        # Buttons defined below
    
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
        botGrid.addWidget(self.element, 0, 3)
        botGrid.addWidget(self.temp, 0, 5)
        botGrid.addWidget(self.energy, 0, 7)
        botGrid.addWidget(self.beta, 0, 9)
        botGrid.addWidget(submit, 0, 11)
#        botGrid.setSpacing(20)    

        grid.addLayout(topGrid, 0, 0)
        grid.addWidget(line, 1, 0, 1, 6)
        grid.addWidget(label, 2, 0)
        grid.addWidget(line2, 3, 0, 1, 6)
        grid.addLayout(botGrid, 4, 0)

        self.setGeometry(300, 300, 500, 420) #x coord, y coord, width, height
        self.setWindowTitle('Beta Decay Evaluation')
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
        self.A = self.element.text()
        self.energyVar = self.energy.text()
        self.betaVar = self.beta.currentText()
        self.tempVar = self.temp.text()
        self.accept()
 
    def mainClicked(self):
        #TODO: Fix bug when closing main window
#        self.chemSymVar = "Zn"
#        self.A = 10
#        self.spinVar = "0+"
#        self.exitcount = 1
        self.close()
        os.system("python3 StartupQt.py")
       


#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

def getbetaoutputs(gif):
    """
    Method called by IsotopeDataExporting to launch the plotting 
    window and pass inputs
    """
#    app = QApplication(sys.argv)
    ex = BetaDecay(gif)
    ex.exec_()
#    sys.exit(app.exec_())
    #app.exec_()

    a=ex.chemSymVar.upper()
    b=ex.A
    J=""
    E=ex.energyVar
    B=ex.betaVar
    temp=ex.tempVar
    if temp == "" or temp == "Temp (K)":
        temp = 0
    temp=float(temp)

    if a.isdigit() and b.isalpha():
        Z = b
        A = a
    else:
        Z = a
        A = b

    if E == "" or E == "Energy (keV)":
        E = 50000

    ##These if statements kill the program if the user leaves a section blank
    if Z == "" or A == "" or Z == "Mass #" or A == "Element":
        print("Please enter a valid element and mass number.")
        sys.exit()

    return (Z, A, J, E, B, temp)
