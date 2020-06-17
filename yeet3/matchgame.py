from tkinter import *
from tkinter import messagebox
import random as r 
## SETUP ##
app = Tk()
app.title("MatchGame")
app['bg'] = "#fc3503"


## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)


app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=10)

## DEFS (One for each button) ##
def match():
    
    tries=0
    mylist.delete(0,END)
    mynum = int(textnumber.get())
    
    if mynum > 100 or mynum < 1:
       messagebox.showinfo(message="Error, value must be from 1,100...") 
       return
    
#starts the game
    while True:
        
        randomnum = r.randint(1,100)
        tries += 1
        mylist.insert(END, "Try %d: %d" %(tries,mynum))


    
        if mynum == randomnum:
            messagebox.showinfo(message="Good Job!, your number matches! It took you %d amount of tries" % (tries))
            break
            
        
    mylist.see(END)
    labeltries2['text']= "%d"% tries


def clear():
    mylist.delete(0,END)
    textnumber.delete(0,END)
    labeltries2['text'] = "0"


## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
labelrow1 = Label(text="Please Enter a number from 1-100")
labelrow1.config(bg="#fc3503",fg='white')
textnumber = Entry(width=5)

buttonadd = Button(text="Match the number", command=match)
buttonadd.config(bg="#fc3503",fg='white')
mylist = Listbox()
mylist.config(bg="#fc3503",fg='white')
labeltries1 = Label(text="Number of Tries")
labeltries1.config(bg="#fc3503",fg='white')
labeltries2 = Label(text="0")
labeltries2.config(bg="#fc3503",fg='white')
clearbutton = Button(text="Reset", command=clear)
clearbutton.config(bg="#fc3503",fg='white')

## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
labelrow1.grid(row=1, column=1)
textnumber.grid(row=1, column=2)
buttonadd.grid(row=1, column=3)
mylist.grid(row=2, column=2)
labeltries1.grid(row=3, column=1)
labeltries2.grid(row=3, column=2)
clearbutton.grid(row=3, column=3)

#.grid(row= , column= )     
