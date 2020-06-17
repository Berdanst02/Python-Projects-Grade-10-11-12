from tkinter import *
from tkinter import messagebox
import random as r 
import time as t 
money=100
## SETUP ##
app = Tk()
app.title("Slot Machine")
#app['bg'] = "#666666"
## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.columnconfigure(1,pad=10)
app.columnconfigure(2,pad=10)

## DEFS (One for each button) ##
def spin():
    buttonspin.grid_remove()
    labelstatus.grid_remove()
    global money
    money -=10
    labelmoney['text'] = "Money $: %d"%(money)
    #loop1 LOOP =======================================
    for times in range(1,30):
        s1 = r.randint(1,7)
        s2 = r.randint(1,7)
        s3 = r.randint(1,7)
        img1['file'] = "pic%d.gif"%(s1)
        img2['file'] = "pic%d.gif" % (s2)
        img3['file'] = "pic%d.gif" % (s3)
        t.sleep(0.05)
        app.update_idletasks()
  #loop2 LOOP =======================================
    for times in range(1,30):
        s2 = r.randint(1,7)
        s3 = r.randint(1,7)
        img2['file'] = "pic%d.gif" % (s2)
        img3['file'] = "pic%d.gif" % (s3)
        t.sleep(0.05)
        app.update_idletasks()
#loop2 LOOP =======================================
    for times in range(1,30):
        s3 = r.randint(1,7)
        img3['file'] = "pic%d.gif" % (s3)
        t.sleep(0.05)
        app.update_idletasks()

#winner
    if s1 ==s2 and s1==s3:
        labelstatus.config(text="3 of a kind! you win $100")
        money +=100
    elif s1==s2 or s1==s3 or s2==s3:
        labelstatus.config(text="2 of a kind! you win $20")
        money += 20
    else:
        labelstatus.config(text="No matches you lost $10")
    
    labelmoney.config(text="You have $" + str(money))
    
    if money > 0:
        buttonspin.grid()
    labelstatus.grid()
    if money <=0:
        labelmoney['text'] = "No more money go home man"
        
    else:
        labelmoney['text'] = "You have $%d"%(money)
        buttonspin.grid()
        
    
    
    buttonspin.grid()
    labelstatus.grid()
    labelmoney['text'] = "Money: $%d"%(money)


## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
buttonspin = Button(text="SPIN", command=spin,width= 10)
labelmoney = Label(text="Money : $100", width=20)
labelstatus = Label(text="Press Spin to start playing...")
img1 = PhotoImage(file="pic1.gif")
img2 = PhotoImage(file="pic1.gif")
img3 = PhotoImage(file="pic1.gif")
slot1 = Label(image=img1)
slot2 = Label(image=img2)
slot3 = Label(image=img3)

## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
buttonspin.grid(row=2, column=1, columnspan=3)
labelmoney.grid(row=4, column=1,columnspan=3)
labelstatus.grid(row=3, column=1,columnspan=3)
slot1.grid(row=1, column=1)
slot2.grid(row=1, column=2)
slot3.grid(row=1, column=3)
#.grid(row= , column= )
