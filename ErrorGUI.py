import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

buttonYes = False
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Error Notification'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


       # button1 = QPushButton('Fuckyou', self)
       # button1.clicked.connect(self.fuck)

       # num = 1
       # if num == 0:
        #    print("whiy")
       # else:
          #  print("k")
        
        #QMessgeBox buttonReply:
        #buttonReply.setStandardButtons(QMessageBox::Yes | QMessageBox::No)
        buttonReply = QMessageBox.question(self, 'Error Notification', "Invalid Input. Would you like to try again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            global buttonYes
            buttonYes = True
           # buttonReply.buttonClicked.connect(self.mainClicked)
        else:
            exit()
        self.show()

   # def fuck(self):
       # exit()

   # def mainClicked(self):
    #    self.close()
     #   os.system("python StartupQt.py")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
