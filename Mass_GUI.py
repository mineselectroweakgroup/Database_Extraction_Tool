from tkinter import *
root = Tk()
root.title("Electroweak Interactions Group -- Systematic Study Program")
import os
import searching_function as sf

#GUI used for Hayden's code.
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.create_widgets()
        self.grid()

        self.qLowVar = StringVar()
        self.qHighVar = StringVar()

        self.aLowVar = StringVar()
        self.aHighVar = StringVar()

    def create_widgets(self):
        title = Frame(self)
        decay = Frame(self)
        out = Frame(self)
        title.pack(side = TOP)
        decay.pack(side = BOTTOM)
        out.pack(side = BOTTOM)

        decayLabel = Label(decay, text = "Decay Information")
        decayLabel.grid(row = 0, column = 0, sticky = W)

        qLowLabel = Label(decay, text = "Q Low")
        qLowLabel.grid(row = 1, column = 0, sticky = W)
        qHighLabel = Label(decay, text = "Q High")
        qHighLabel.grid(row = 1, column = 1, sticky = W)

        aLowLabel = Label(decay, text = "A Low")
        aLowLabel.grid(row = 3, column = 0, sticky = W)
        aHighLabel = Label(decay, text = "A High")
        aHighLabel.grid(row = 3, column = 1, sticky = W)

        self.qLowEntry = Entry(decay)
        self.qLowEntry.grid(row = 2, column = 0, sticky = W)
        self.qHighEntry = Entry(decay)
        self.qHighEntry.grid(row = 2, column = 1, sticky = W)
        
        self.aLowEntry = Entry(decay)
        self.aLowEntry.grid(row = 4, column = 0, sticky = W)
        self.aHighEntry = Entry(decay)
        self.aHighEntry.grid(row = 4, column = 1, sticky = W)

        decaySubmit = Button(decay, text = "Submit", command = self.sendDecayData)
        decaySubmit.grid(row = 5, column = 0, sticky = W)

        newChoiceSubmit = Button(decay, text = "Program Selection", command = self.newChoiceButton)
        newChoiceSubmit.grid(row = 5, column = 1)

        self.outText = Text(out)
        self.outText.grid(row = 0, column = 1, sticky = W+E+N+S)
        outScroll = Scrollbar(out)
        outScroll.grid(row = 0, column = 1, sticky = E+S+N)
        outScroll.config(command=self.outText.yview)
        self.outText.config(yscrollcommand=outScroll.set)





        self.pictureSpot = Canvas(title,width = 620, height = 100)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo2 = PhotoImage(file = "eilonglogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo2, anchor = "nw")

    def sendDecayData(self):
        """Send user input to decay data sorting function"""
        self.outText.delete(0.0,END)
        self.qLowVar = self.qLowEntry.get()
        self.qHighVar = self.qHighEntry.get()
        self.aLowVar = self.aLowEntry.get()
        self.aHighVar = self.aHighEntry.get()

        self.outText.insert(0.0, sf.acquire(self.qLowVar,self.qHighVar,self.aLowVar,self.aHighVar,Theory = False,Sym = False))

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()

    def newChoiceButton(self):
        self.chemSymVar = "Zn"
        self.A = 10
        self.spinVar = "0+"
        self.exitcount = 1
        root.destroy()
        os.system("python3 USE_THIS.py")
        sys.exit()



app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()
