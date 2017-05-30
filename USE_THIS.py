from tkinter import *
root = Tk()
root.title("Electroweak Interactions Group -- Systematic Study Program")
import os

#Initial class with the original framework. Is called upon starting the program and is used to call other functions.
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        title = Frame(self)
        buttons = Frame(self)
        title.pack(side = TOP)
        buttons.pack(side = BOTTOM)

        buttonsLabel = Label(buttons, text = "Select which program you would like to use")
        buttonsLabel.grid(row = 0)


        evalDataButton = Button(buttons,text = "Evaluated Nuclear Structure Data", command = self.evalFunc)
        evalDataButton.grid(row = 1, column = 0)

        massDataButton = Button(buttons, text = "Hayden's Code; WHAT DOES IT DO?", command = self.massFunc)
        massDataButton.grid(row = 2, column = 0)

        betaDataButton = Button(buttons, text = "Evaluated Beta Decay Data", command = self.betaFunc)
        betaDataButton.grid(row = 3, column = 0)

        self.pictureSpot = Canvas(title,width = 640, height = 180)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo = PhotoImage(file = "eilogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo, anchor = "nw")

    def evalFunc(self):
        root.destroy()
        os.system('python3 THIS_WORKS.py "one"')

    def massFunc(self):
        root.destroy()
        os.system("python3 Mass_GUI.py")

    def betaFunc(self):
        root.destroy()
        os.system('python3 THIS_WORKS.py "two"')

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()


app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()
