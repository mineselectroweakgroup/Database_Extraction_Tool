import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget, QMessageBox
from PyQt5. QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    #app = QApplication(sys.argv)
    #win = QWidget()
    button1 = QPushButton(win)
    button1.setText("Show Dialog")
    button1.move(50,50)
    button1.clicked.connect(showDialog)
    win.setWindowTitle("clicked")
    win.show()
    sys.exit(app.exec_())

def showDialog():
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Information)
    msgbox.setText("Message box pop up window")
    msgbox.setWindowTitle("Example")
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgbox.buttonClicked.connect(msgButtonClick)

    returnValue = msgbox.exec()
    if returnValue == QMessageBox.Ok:
        print('ok')

def msgButtonClick(i):
    print('ye',i.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    window()
