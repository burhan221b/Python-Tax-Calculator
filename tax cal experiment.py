#tax calculator

from tkinter import *

class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Tax Calculator: Set fields to 0")
    ####before tax
        self.beforetaxlabel = Label(window, text = "Before Tax: ", font = "Helvectica 12")
        self.orgbtlVar = StringVar()
        self.orgbtlVar.set("0")
        btlEntry = Entry(window, textvariable = self.orgbtlVar, font = "Helvectica 12")
        self.beforetaxlabel.grid(row = 1, column = 1)
        btlEntry.grid(row = 1, column = 2, columnspan = 2)
    ####tax rate
        self.taxratelabel = Label(window, text = "Tax Rate in %: ", font = "Helvectica 12")
        self.orgtrVar = StringVar()
        self.orgtrVar.set("0")
        trEntry = Entry(window, textvariable = self.orgtrVar, font = "Helvectica 12")
        self.taxratelabel.grid(row = 2, column = 1)
        trEntry.grid(row = 2, column = 2, columnspan = 2)

####Subtax Price
        self.subtaxlabel = Label(window, text = "Addition: ", font = "Helvectica 12")
        self.orgsubtaxVar = StringVar()
        self.orgsubtaxVar.set("0")
        subtaxEntry = Entry(window, textvariable = self.orgsubtaxVar, font = "Helvectica 12")
        self.subtaxlabel.grid(row = 3, column = 1)
        subtaxEntry.grid(row = 3, column = 2, columnspan = 2)
        
    ####Final Price
        self.finalpricelabel = Label(window, text = "Final Price: ", font = "Helvectica 12")
        self.orgfpVar = StringVar()
        self.orgfpVar.set("0")
        fpEntry = Entry(window, textvariable = self.orgfpVar, font = "Helvectica 12")
        self.finalpricelabel.grid(row = 4, column = 1)
        fpEntry.grid(row = 4, column = 2, columnspan = 2)
    ####Calculate button
        button = Button(window, text = "Calculate", command = self.calculate, font = "Helvectica 12 bold") #the command is when the button is click, call this metod
        button.grid(row = 5, column = 2)
        #resultsbtVar = StringVar()
        #resultsbtVar.set("0.00")


        window.mainloop()

    def calculate(self):
        ####before tax
        orgbtStr = self.orgbtlVar.get()
        orgbt = float(orgbtStr)
        ####percentage
        orgtrStr = self.orgtrVar.get()
        orgtr = float(orgtrStr)

        ####subtax
        orgsubtaxStr = self.orgsubtaxVar.get()
        orgsubtax = float(orgsubtaxStr)
        
        #### final price
        orgfpStr = self.orgfpVar.get()
        orgfp = float(orgfpStr)

        self.beforetaxlabel["fg"] = "black"
        self.taxratelabel["fg"] = "black"
        self.subtaxlabel["fg"] = "black"
        self.finalpricelabel["fg"] = "black"

        if orgbt == 0:
            orgbt = orgfp / (1 + (orgtr / 100))
            self.beforetaxlabel["fg"] = "green"
        elif orgtr == 0:
            orgtr = (orgfp - orgbt) / orgbt 
            self.taxratelabel["fg"] = "purple"
        elif orgfp == 0:
            orgfp = orgbt + (orgbt * (orgtr / 100))
            self.finalpricelabel["fg"] = "red"

        if orgsubtax == 0:
            orgsubtax = orgfp - orgbt
            self.subtaxlabel["fg"] = "orange"
        
        self.orgbtlVar.set(format(orgbt, ".2f"))
        self.orgtrVar.set(format(orgtr, ".2f"))
        self.orgsubtaxVar.set(format(orgsubtax, ".2f"))
        self.orgfpVar.set(format(orgfp, ".2f"))


Calculator()
