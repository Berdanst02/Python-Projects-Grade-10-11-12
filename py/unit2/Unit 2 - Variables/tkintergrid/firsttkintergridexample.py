from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Title Goes Here")
app['bg'] = "#36c0d9"

## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)

## DEFS (One for each button) ##
def submit():
    name = nameEntry.get()

    age = int(ageEntry.get())

    age+=10

    answerLabel['text']=("%s, in 10 years you will be %d years old"%(name, age))

def clear():
    nameEntry.delete(0,END)
    ageEntry.delete(0,END)
    answerLabel['text'] = ""
    name.Entry.focus()
## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
submitButton = Button(text="Submit",width=10,command=submit)
clearButton = Button(text="Clear",width=10,command=clear)
nameLabel = Label(text="Enter Name")
ageLabel = Label(text="Enter Age")
nameEntry = Entry(width=20)
ageEntry = Entry(width=20)
answerLabel = Label(text="")


## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##

#.grid(row= , column= )
submitButton.grid(row=3, column=1)
clearButton.grid(row=3, column=2)
nameLabel.grid(row=1 , column= 1)
ageLabel.grid(row=2 , column=1 )
nameEntry.grid(row=1 , column=2 )
ageEntry.grid(row=2 , column=2 )
answerLabel.grid(row=4 , column=1, columnspan=2)
