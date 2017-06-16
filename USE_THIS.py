from tkinter import *
root = Tk()
root.title("Electroweak Interactions Group -- Systematic Study Program")
root.configure(background='#21314D')
import os
import time

#Initial class with the original framework. Is called upon starting the program and is used to call other functions.
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.configure(background='#21314D')

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        title = Frame(self)
        #message = Frame(self)
        buttons = Frame(self)
        extraSpace = Frame(self)
        #message.pack(side=TOP)
        title.pack(side = TOP)
        extraSpace.pack(side = BOTTOM)
        buttons.pack(side = BOTTOM)

        buttons.configure(bg="#21314D")

        buttonsLabel = Label(buttons, text = "PLEASE MAKE A PROGRAM SELECTION",font=("Helvetica",16,"bold"),bg='#21314D',fg='#92A2BD')
        buttonsLabel.grid(row = 0)


        evalDataButton = Button(buttons,text = "EVALUATED NUCLEAR STRUCTURE DATA", command = self.evalFunc,font=("Ariel",11,"bold"),width=39,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D")
        evalDataButton.grid(row = 1, column = 0)

        massDataButton = Button(buttons, text = "FUCK YOU HAYDEN, I DISABLED YOUR BUTTON", command = self.massFunc,font=("Ariel",11,"bold"),width=39,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",state=DISABLED)
        massDataButton.grid(row = 2, column = 0)

        betaDataButton = Button(buttons, text = "EVALUATED BETA DECAY DATA", command = self.betaFunc,font=("Ariel",11,"bold"),width=39,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D")
        betaDataButton.grid(row = 3, column = 0)

        massParabolaButton = Button(buttons, text = "MASS PARABOLA", command = self.parabolaFunc,font=("Ariel",11,"bold"),width=39,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D")
        massParabolaButton.grid(row = 4, column = 0)

        nucChartButton = Button(buttons, text = "ENVIRONMENTAL DECAY RATE SENSITIVITIES", command = self.nucChartFunc, font=("Ariel",11,"bold"),width=39,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D")
        nucChartButton.grid(row=5,column=0)

        self.pictureSpot = Canvas(title,width = 640, height = 180)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo = PhotoImage(file = "eilogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo, anchor = "nw")

        space = Label(extraSpace, text = " ", fg = '#21314D', bg = '#21314D')
        space.grid(row=0)

        #welcome = Label(message, text = "Hello, my name is Matthew \n Martin and my goal is to haunt \n your life and eat your brains!", font = ("Helvetica", 40, "bold"), fg="Orange Red")
        #welcome.grid(row = 0)

    def evalFunc(self):
        root.destroy()
        os.system('python3 THIS_WORKS.py "one"')

    def massFunc(self):
        root.destroy()
        os.system("python3 Mass_GUI.py")

    def betaFunc(self):
        root.destroy()
        os.system('python3 THIS_WORKS.py "two"')

    def parabolaFunc(self):
        root.destroy()
        os.system('python3 THIS_WORKS.py "three"')

    def nucChartFunc(self):
        root.destroy()
        os.system('python3 Decay_Chart_GUI.py')

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()

app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()
