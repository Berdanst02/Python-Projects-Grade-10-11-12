from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Wage Calculator")
app['bg'] = '#5ea832'

## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=10)
app.columnconfigure(4,pad=10)


## DEFS (One for each button) ##
def calcwage():
    hour = float(hourentry.get())
    wage = float(wageentry.get())
    
    answer = hour * wage
    overpay = (hour - 40) * 2 + answer 
    
    answerLabel['text'] = "Your wage per week is %.2f"%(answer)


    if hour > 40:

        answerLabel['text'] = "your wage per week is %.2f because you overworked"%(overpay)

def clear():
    hourentry.delete(0,END)
    wageentry.delete(0,END)
    answerLabel['text'] = ""
    hourentry.focus()
## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
hoursLabel = Label(text="Enter Hours Worked per week")
wageLabel = Label(text="Enter Wage per Hour")
answerLabel = Label(text="")
answerLabel.config(bg='#5ea832')
calcbutton = Button(text="Calculate Pay",width=20,command=calcwage)
clearButton = Button(text="Clear",width=20,command=clear)
wage = PhotoImage(file="wage1.gif")
picLabel = Label(image=wage)

hourentry = Entry(width=10)
wageentry = Entry(width=10)

## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
hoursLabel.grid(row=1, column=1)
wageLabel.grid(row=2, column=1)
answerLabel.grid(row=4, column=1, columnspan=2)
calcbutton.grid(row=3, column=1)
clearButton.grid(row=3, column=2)
picLabel.grid(row=1, column=3, rowspan=4)
hourentry.grid(row=1, column=2)
wageentry.grid(row=2, column=2)
#.grid(row= , column= )
