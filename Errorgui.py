import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Error Notification'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 60
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        errorprompt = QLabel("Input Error: Would you like to try again?", self)
        #errorprompt.setAlignment(QtCore.Qt.Center)
        
        button1 = QPushButton('Exit', self)
        button1.setToolTip('Exit the program')
        button1.move(167,30)
        button1.clicked.connect(self.on_clicked)

        button2 = QPushButton('Yes',self)
        button2.setToolTip('Return to main selection')
        button2.move(67,30)
        button2.clicked.connect(self.on_clicked)

        self.show()

    def on_clicked(self):
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

