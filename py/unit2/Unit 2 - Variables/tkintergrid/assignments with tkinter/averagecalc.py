from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Average Calculator")
app['bg'] = "#666666"

## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.rowconfigure(5,pad=10)
app.rowconfigure(6,pad=10)
app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=30)

## DEFS (One for each button) ##

def calc():
    mark1 = float(mark1entry.get())
    mark2 = float(mark2entry.get())
    mark3 = float(mark3entry.get())
    mark4 = float(mark4entry.get())

    answer = (mark1+mark2+mark3+mark4) / 4


    if answer < 50:

        averageLabel['text'] = "Your Average is %.2f, you have failed"%(answer)
    elif answer > 50:

        averageLabel['text'] = "Your Average is %.2f, you have passed"%(answer)
def clear():
    mark1entry.delete(0,END)
    mark2entry.delete(0,END)
    mark3entry.delete(0,END)
    mark4entry.delete(0,END)
    averageLabel['text'] = ""
    mark1entry.focus()



## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
averagebutton = Button(text="Calculate the Average",command=calc)
mark1Label = Label(text="Enter 1st Mark")
mark2Label = Label(text="Enter 2nd Mark")
mark3Label = Label(text="Enter 3rd Mark")
mark4Label = Label(text="Enter 4th Mark")
averageLabel = Label(text="")
averageLabel.config(bg='black',fg="#666666", width=40,font=("Arial", 8))
report = PhotoImage(file="capture.gif")
picLabel = Label(image=report)
clearbutton =  Button(text="Clear",command=clear)

mark1entry = Entry(width=10)
mark2entry = Entry(width=10)
mark3entry = Entry(width=10)
mark4entry = Entry(width=10)

## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
averagebutton.grid(row=5, column=1)
mark1Label.grid(row=1, column=1)  
mark2Label.grid(row=2, column=1) 
mark3Label.grid(row=3, column=1)
mark4Label.grid(row=4, column=1)
averageLabel.grid(row=6, column=1,columnspan=3)

picLabel.grid(row=1, column=3,rowspan=5)
clearbutton.grid(row=5, column=2) 

mark1entry.grid(row=1, column=2)
mark2entry.grid(row=2, column=2)
mark3entry.grid(row=3, column=2)
mark4entry.grid(row=4, column=2)

#.grid(row= , column= )
