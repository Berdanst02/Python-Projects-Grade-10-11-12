from tkinter import *
import random as r

## SETUP ##
app = Tk()
app.title("Magic 8 BALL")
app['bg'] = 'white'

## GRID PADDING ##
app.rowconfigure(1,pad=20)


## DEFS (One for each button) ##
def getFortune():
    fortunes=[]
    fortunes.append("It is certain.")
    fortunes.append("It is decidedly so.")
    fortunes.append("Without a doubt.")
    fortunes.append("Yes – definitely.")
    fortunes.append("You may rely on it.")
    fortunes.append("As I see it, yes.")
    fortunes.append("Most likely.")
    fortunes.append("Outlook good.")
    fortunes.append("Yes.")
    fortunes.append("Signs point to yes.")
    fortunes.append("Reply hazy, try again.")
    fortunes.append("Ask again later.")
    fortunes.append("Better not tell you now.")
    fortunes.append("Cannot predict now.")
    fortunes.append("Concentrate and ask again.")
    fortunes.append("Don't count on it")
    fortunes.append("I don't know")
    fortunes.append("My sources say no")
    fortunes.append("Outlook not so good.")
    fortunes.append("Yeah.. No")
    fortuneLabel['text']= r.choice(fortunes)

## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
ball = PhotoImage(file ="magic8ball.gif")
ballButton = Button(image=ball,bg='red',command=getFortune)
fortuneLabel = Label(text="Ask a yes/no question")
fortuneLabel.config(bg='orange',fg='white',font=("Impact",24),width=30,height=3)
#grid thingy
ballButton.grid(row=1,column=1)
fortuneLabel.grid(row=2,column=1)



#statement to help the program run in pycharm
app.mainloop()