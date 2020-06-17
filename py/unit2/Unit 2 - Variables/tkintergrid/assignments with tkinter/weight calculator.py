from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Weight converter")
app['bg'] = "#eb4334"
      
## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)

app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=10)
app.columnconfigure(4,pad=10)

#option menu widget









## DEFS (One for each button) ##
def calc():
    lbs = float(lbentry.get())
    
    answer = lbs * 0.453592
    
    answerLabel['text'] = "Your weight in kgs is %.2f"%(answer)

def clear():

 lbentry.delete(0,END)
 answerLabel['text'] = ""


## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
convertbutton = Button(text="Convert Lb to Kg",width=20,command=calc)
weightLabel = Label(text="Enter your weight in lbs",width=20)
clearbutton = Button(text="Clear",width=20,command=clear)
answerLabel = Label(text="")
answerLabel.config(bg='#eb4334', fg='#2b2322',font=("Arial", 17))
lbentry = Entry(width=10)

weightpic = PhotoImage(file="weight1.gif")
weight = Label(image=weightpic)


## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
convertbutton.grid(row=2, column=1)
lbentry.grid(row=1, column=2)
weightLabel.grid(row=1, column=1)
clearbutton.grid(row=2, column=2)
answerLabel.grid(row=3, column=1, columnspan=2)
weight.grid(row=1, column=3,rowspan=3)
#.grid(row= , column= )
