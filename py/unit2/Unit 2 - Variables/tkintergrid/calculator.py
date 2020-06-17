from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Calculator")
app['bg'] = '#753344'

## GRID PADDING ## 
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.rowconfigure(5,pad=10)
app.rowconfigure(6,pad=10)
app.columnconfigure(1,pad=40)
app.columnconfigure(2,pad=40)


## DEFS (One for each button) ##
def add():
    #input
    x = float(xEntry.get()) #read from xentry to store into x
    y = float(yEntry.get())

    #processing
    answer = x + y
    #output
    answerLabel['text'] = "%.2f + %.2f = %.2f"%(x, y, answer)
        
def sub():
    x = float(xEntry.get()) #read from xentry to store into x
    y = float(yEntry.get())
    answer = x - y    
    answerLabel['text'] = "%.2f - %.2f = %.2f"%(x, y, answer)

def multiply():
    x = float(xEntry.get()) #read from xentry to store into x
    y = float(yEntry.get())
    answer = x * y
    answerLabel['text'] = "%.2f x %.2f = %.2f"%(x, y, answer)

def divide():
    x = float(xEntry.get()) #read from xentry to store into x
    y = float(yEntry.get())
    answer = x / y
    answerLabel['text'] = "%.2f / %.2f = %.2f"%(x, y, answer)


def clear():

    xEntry.delete(0,END)
    yEntry.delete(0,END)
    answerLabel['text'] = ""
    xEntry.focus()
## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
addbutton = Button(text="+",width=10,command=add)
subbutton = Button(text="-",width=10,command=sub)
multiplybutton = Button(text="*",width=10,command=multiply)
dividebutton = Button(text="/",width=10,command=divide)
clearbutton = Button(text="Clear",width=20,command=clear)
xLabel = Label(text="Enter x value")
yLabel = Label(text="Enter y value")
answerLabel = Label(text="",bg='#753344')
xEntry = Entry(width=10)
yEntry = Entry(width=10)

#pic

calc = PhotoImage(file="images.png")
picframe = Label(image=calc)
## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##

#.grid(row= , column= )
addbutton.grid(row=3 , column=1 )
subbutton.grid(row=3 , column=2 ) 
multiplybutton.grid(row=4 , column=1 )
dividebutton.grid(row=4 , column=2 ) 
clearbutton.grid(row=6 , column=1,columnspan=2 ) 
xLabel.grid(row=1 , column=1 )
yLabel.grid(row=2 , column=1 )
answerLabel.grid(row=5 , column=1,columnspan=2 )
xEntry.grid(row=1 , column=2 )
yEntry.grid(row=2 , column=2)
picframe.grid(row=1,column=3,rowspan=6)
