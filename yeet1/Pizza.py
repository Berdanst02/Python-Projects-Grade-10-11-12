from tkinter import *
from tkinter import messagebox

## SETUP ##
app = Tk()
app.title("Pizza Program")
app.geometry = "800x800"
app['bg'] = "#fc6603"

## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.rowconfigure(5,pad=10)
app.rowconfigure(6,pad=10)
app.rowconfigure(7,pad=10)
app.rowconfigure(8,pad=10)
app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=10)
app.columnconfigure(4,pad=10)


## DEFS (One for each button) ##
def order():
    toppings = 0
    size = rbvar.get()
    if size=="?":
        messagebox.showinfo("Error", "Must Choose a side")
        return
    elif size=="sm":
        price=8
    elif size=="md":
        price=10
    elif size=="lg":
        price=12
    else:
        price=14
        
    #toppings
    toppings = 0
    toplist.delete(0, END)
    if cb1var.get()==1:
        toppings +=1
        toplist.insert(END,"Pepperoni")
    if cb2var.get() == 1:
        toppings += 1
        toplist.insert(END,"Cheese")
    if cb3var.get() == 1:
        toppings += 1
        toplist.insert(END, "Onions")
    if cb4var.get() == 1:
        toppings += 1
        toplist.insert(END, "BBQ")
    total = price + toppings
    price2['text'] = "$%.2f" % (price)
    total2['text'] =  "$%.2f" % (total)

def reset():
    cb1var.set(0)
    cb2var.set(0)
    cb3var.set(0)
    cb4var.set(0)
    rbvar.set("?")
    toplist.delete(0,END)
    price2['text'] = "?"
    total2['text'] = "?"
    
## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
topLabel= Label(text="Choose Toppings", bg='black', fg='yellow', width=50)
sizeLabel= Label(text="Choose size", bg='black', fg='yellow',width=50)
price1 = Label(text="Price of the Pizza")
price2 = Label(text="?")
ordered= Label(text="Toppings ordered")
total1 = Label(text="total price")
total2 = Label(text="?")

orderbutton = Button(text="Order", command=order) 
resetButton = Button(text="Reset", command=reset)

toplist = Listbox(height=6)

cb1var = IntVar()
cb2var = IntVar()
cb3var = IntVar()
cb4var = IntVar()

cb1 = Checkbutton(text="Pepperoni", variable = cb1var)
cb2 = Checkbutton(text="Cheese", variable = cb2var)
cb3 = Checkbutton(text="Onions", variable = cb3var)
cb4 = Checkbutton(text="BBQ", variable = cb4var)

rbvar = StringVar()
rbvar.set("?")
rb1 = Radiobutton(text="Small" , variable=rbvar, value="sm")
rb2 = Radiobutton(text="Medium" , variable=rbvar, value="md")
rb3 = Radiobutton(text="Large" , variable=rbvar, value="lg")
rb4 = Radiobutton(text="x-Large" , variable=rbvar, value="xlg")


## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##

#.grid(row= , column= )
#row1
topLabel.grid(row=1 , column=1,columnspan=4 )
#row2
cb1.grid(row=2, column=1 )
cb2.grid(row=2 , column=2 )
cb3.grid(row=2 , column=3 )
cb4.grid(row=2 , column=4 )
#row3
sizeLabel.grid(row=3 , column=1,columnspan=4)
rb1.grid(row=4 , column=1 )
rb2.grid(row=4 , column=2)
rb3.grid(row=4 , column=3 )
rb4.grid(row=4 , column=4 )
#row5
orderbutton.grid(row=5 , column=1,columnspan=2 )
resetButton.grid(row=5 , column=3,columnspan=2 )
#row6
price1.grid(row=6 , column=2 )
price2.grid(row=6 , column=3 )
#row7
ordered.grid(row=7 , column=2 )
toplist.grid(row=7 , column=3 )
total1.grid(row=8 , column= 2)
total2.grid(row=8 , column= 3 )

