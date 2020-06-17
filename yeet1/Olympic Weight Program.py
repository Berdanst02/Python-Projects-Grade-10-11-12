from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Olympic Weight Program")
app['bg'] = '#fcca03'
app.geometry = "400x400"
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.rowconfigure(5,pad=10)
app.rowconfigure(6,pad=10)
app.columnconfigure(1,pad=20)
app.columnconfigure(2,pad=20)
app.columnconfigure(3,pad=20)

## DEFS (One for each button) ##
def addathlete():
    name = Athletenameentry.get()
    weight = int(Athleteweight.get())
    if weight < 80 or weight >200:
        messagebox.showinfo("Error", "Athlete is disqualified")
    elif weight >= 80 and weight <120:
        lightBox.insert(END, "%s, %.2f kg"%(name, weight))
    elif weight >=121 and weight < 180:
        middlebox.insert(END, "%s, %.2f kg"%(name, weight))
    elif weight >=181 and weight < 240:
        heavybox.insert(END, "%s, %.2f kg"%(name, weight))
    else:
        messagebox.showinfo("Error", "Athlete is disqualified")
     

## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
Athletenameentry = Entry(width=20)
Athletename = Label(text="Enter Athlete's name")
Athletenterweight = Label(text="Enter Weight in KG")
Athleteweight =Entry(width=20)
Addathletebutton = Button(text="Add Athlete", command = addathlete) 
lightweightLabel = Label(text="Light weight")
middleweightLabel = Label(text="Middle Weight")
heavyweightLabel = Label(text="Heavy Weight")
lightBox = Listbox()
middlebox = Listbox()
heavybox = Listbox()



## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
Athletenameentry.grid(row=1,column=2)
Athletename.grid(row=1 , column=1 )
Athleteweight.grid(row=2 , column=2)
Athletenterweight.grid(row=2, column=1)
Addathletebutton.grid(row=3 , column=2)
lightweightLabel.grid(row=4 , column=1 ) 
middleweightLabel.grid(row=4 , column=2 ) 
heavyweightLabel.grid(row=4 , column=3 )
lightBox.grid(row=5 , column=1, rowspan=6 )
middlebox.grid(row=5 , column= 2)
heavybox.grid(row=5 , column=3 , rowspan=6)
#.grid(row= , column= )
