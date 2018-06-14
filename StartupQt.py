#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QDialog, QMainWindow)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5 import QtCore

from Main import startup

import UpdateTool

class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()    

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        #Input Dialogs
        
        test = QLabel("Comprehensive Evaluated Nuclear\nDatabase Extraction Toolkit", self)      
        test.setAlignment(QtCore.Qt.AlignCenter) 
        test.setStyleSheet("color: #2B4570; border: 2px solid #2B4570; border-radius: 5px; font-size:20px") 
        
        prompt = QLabel("\n\n\n\nChoose an option below:", self)
        prompt.setStyleSheet("color: #2B4570; font-size:16px;")
        prompt.setAlignment(QtCore.Qt.AlignBottom)
        
        selection = QComboBox(self)
        selection.addItem("Evaluated Nuclear Structure Data")
        selection.addItem("Environmental Decay Rate Changes")
        selection.addItem("Mass Parabola")
        selection.setStyleSheet("background-color:#2B4570; color:#F5EFFF; border: 0px solid black; border-radius:5px; padding: 3px;")

        submit = QPushButton("Open")
        submit.clicked.connect(lambda: self.submitClicked(selection))
        submit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px;")               
        submit.installEventFilter(self)
 
        exit = QPushButton("Exit", self)
        exit.clicked.connect(QApplication.quit)
#        exit.clicked.connect(self.exitClicked)
        exit.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px;")                
        exit.installEventFilter(self)     

        update = QPushButton("Update", self)
        update.clicked.connect(UpdateTool.main)
        update.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px;")                
        update.installEventFilter(self)     

 
        grid.addWidget(test, 0, 0) 
        grid.addWidget(prompt, 1, 0)
        grid.addWidget(selection, 3, 0)    

        innerGrid = QGridLayout()
        innerGrid.addWidget(submit, 0, 0)
        innerGrid.addWidget(update, 0, 1)
        innerGrid.addWidget(exit, 0, 2)

        grid.addLayout(innerGrid, 4, 0)

            
     
        self.setGeometry(300, 300, 380, 220) #x coord, y coord, width, height
        self.setWindowTitle('CENDET')
        self.setFixedSize(self.size())
        self.setStyleSheet("background-color:white")


    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            object.setStyleSheet("background-color:#1E555C; color:#EBEEF2; border:1px solid #1E555C; border-radius:5px; height:25px;")
            return True;
        if event.type() == QtCore.QEvent.HoverLeave:
            object.setStyleSheet("background-color:#EBEEF2; border: 1px solid #2B4570; border-radius:5px; color: #2B4570; height:25px;")
        return False;

    def submitClicked(self, combo):
        index = combo.findText(combo.currentText(), QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)
        option = ["one", "two", "three"]
        self.close()
        startup(option[index])
        
#        self.exit()

    def updateClicked(self):
        main

    def exitClicked(self):
        #Input default variables
        print("close")
        sys.exit()
        return 0;       

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
#    app.exec_()

if __name__ == '__main__':
    main()

    
