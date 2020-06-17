from tkinter import *
from tkinter import messagebox
import winsound
## SETUP ##
app = Tk()
app.title("Call Of Duty Zombies Franchise - Trivia")
app.geometry('710x500')
app['bg'] = '#5e3636'
app.iconbitmap('pics for trivia/call-of-duty-zombies-png-4.ico')

## GRID PADDING ##
app.rowconfigure(1,pad=10)
app.rowconfigure(2,pad=10)
app.rowconfigure(3,pad=10)
app.rowconfigure(4,pad=10)
app.rowconfigure(5,pad=10)
app.rowconfigure(6,pad=10)
app.columnconfigure(1,pad=20)
app.columnconfigure(2,pad=10)
app.columnconfigure(3,pad=10)


## DEFS (One for each button) ##
def go():
    global item, right, wrong
    answer = choice.get()
    if answer==questions[item][5]:
        result = "Correct Answer!"
        right +=1
        rightlabel['text'] = "Correct Answers: %d" %(right)
    else:
        rightloc = int(questions[item][5])
        result = "Wrong - the answer is:" + questions[item][rightloc]
        wrong +=1
        wronglabel['text']= "Wrong Answers: %d" %(wrong)
    if (item < 17):
        result += ">>> Click for the next question"
    else:
        result += ">>> Game Over. Click to Leave"
        
    nextbutton['text'] = result
    nextbutton.grid()
    setOptions(DISABLED)
    
def setOptions(state):
    choiceA['state'] = state
    choiceB['state'] = state
    choiceC['state'] = state
    choiceD['state'] = state




def nextquestion():
    global item
    item +=1
    if item ==17:
        qLabel.grid_remove()
        imgLabel.grid_remove()
        choiceA.grid_remove()
        choiceB.grid_remove()
        choiceC.grid_remove()
        choiceD.grid_remove()
        gameoverimglabel.grid()
        winsound.PlaySound('pics for trivia/Game Over Sound Effects High Quality.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
        app.geometry('710x500')
        messagebox.showinfo("The End", "This is the end of Trivia, you may close this window")
    
    imgLabel['image'] = images[item]
    choiceA['text'] = questions[item][1]
    choiceB['text'] = questions[item][2]
    choiceC['text'] = questions[item][3]
    choiceD['text'] = questions[item][4]
    qLabel['text'] = questions[item][0]
    choice.set("?")
    nextbutton.grid_remove()
    setOptions(NORMAL)
#home menu start function
def start():
    mainbutton.grid_remove()
    qLabel.grid()
    imgLabel.grid()
    choiceA.grid()
    choiceB.grid()
    choiceC.grid()
    choiceD.grid()
    rightlabel.grid()
    wronglabel.grid()
    nextquestion()
    pressstarttoplaybutton.grid_remove()
    winsound.PlaySound('pics for trivia/videoplayback (5).wav', winsound.SND_FILENAME| winsound.SND_ASYNC)
    app.geometry('750x525')
#Home, Main SCREEN

homeImage = PhotoImage(file="pics for trivia/MAIN.GIF")
mainbutton = Button(image=homeImage, command =start)

pressstarttoplay = PhotoImage(file="pics for trivia/generatedtext.gif"),
pressstarttoplaybutton = Button(image=pressstarttoplay, command = start)
pressstarttoplaybutton.config(bg='#5e3636')
#########

## MAKE WIDGETS -> ex: Button, Label, Entry, Listbox, RadiotButton, Checkbutton ##
nextbutton = Button(text="Next Question", command = nextquestion)
nextbutton.config(font=("Times", 14, "bold italic"), bg='black', fg='yellow', width=50)
gameoverimg = PhotoImage(file='pics for trivia/gameover.GIF')
gameoverimglabel = Label(image = gameoverimg)
rightlabel = Label(text="Correct Answers: 0", font=("Times", 24),bg='green',width=20)
wronglabel = Label(text="Wrong Answers: 0", font=("Times", 24),bg='red',width=20)

image1 = PhotoImage(file = 'pics for trivia/5.gif')
image2 = PhotoImage(file = 'pics for trivia/4.gif')
image3 = PhotoImage(file = 'pics for trivia/2.gif')
image4 = PhotoImage(file = 'pics for trivia/3.gif')
image5 = PhotoImage(file = 'pics for trivia/Capture.gif')
#list of images
images = [PhotoImage(file = 'pics for trivia/5.gif'),
PhotoImage(file = 'pics for trivia/4.gif'),
PhotoImage(file = 'pics for trivia/2.gif'),
PhotoImage(file = 'pics for trivia/3.gif'),
PhotoImage(file = 'pics for trivia/Capture.gif'),
PhotoImage(file = 'pics for trivia/6.gif'),
PhotoImage(file = 'pics for trivia/7.gif'),
PhotoImage(file = 'pics for trivia/8.gif'),
PhotoImage(file = 'pics for trivia/9.gif'),
PhotoImage(file = 'pics for trivia/10.gif'),
PhotoImage(file = 'pics for trivia/11.gif'),
PhotoImage(file = 'pics for trivia/12.gif'),
PhotoImage(file = 'pics for trivia/13.gif'),
PhotoImage(file = 'pics for trivia/14.gif'),
PhotoImage(file = 'pics for trivia/15.gif'),
PhotoImage(file = 'pics for trivia/16.gif'),
PhotoImage(file = 'pics for trivia/17.gif'),
PhotoImage(file = 'pics for trivia/18.gif'),

          
          

          
    
    
    
]


#list of questions
questions = [["How many Elemental Staffs Are There in Origins?", "4", "3", "1", "6","1"],
             ["Who Died in Blood Of The Dead?","Nikolai","Richtofen","Takeo","Maxis","2"],
             ["Who studied Element 115", "Richtofen", "Samantha", "The Warden", "Nobody","1"],
             ["Which  game that featured the first playable zombies gamemode?", "World at War", "Black Ops 3", "Black Ops 4", "Advanced Warfare","1"],
             ["The main element of zombies that causes them to move?", "Agarthian Device", "The Curse", "Element 115", "Illuminati","3"],
             ["Who is Maxis's daughter?", "Misty", "Samantha", "Emily", "Richtofen","2"],
             ["Who wants the Ultimate Power?", "Ultimis Richtofen", "Primis Richtofen", "Primis Nikolai", "Ultimis Nikolai","1"],
             ["What device allows you to travel in the multiverse?", "Summoning Key", "Agarthian Device", "N/A", "Beast Mode","1"],
             ["What is the only perk that does not require you to turn on the power?", "PHD", "Quick Revive", "Deadshot", "Speed Cola","2"],
             ["Which map featured a bus system?", "Origins", "Nacht Der Untoten", "Tranzit", "Ascension", "3"],
             ["Which of the maps did not feature the primis crew?", "Gorod Krovi", "Der Eisandrache", "Mob of the dead", "Revelations", "3"],
             ["Name of the first map in the series", "Nacht Der Untoten", "The Giant", "Tag der Toten", "Call of the dead","1"],
             ["Finish the Quote, You must Ascend from...", "Us", "Shadow", "the sky", "Darkness", "4"],
             ["What is this Creature?","Margwa","Shadowman","Hellhound","Lagoon","1"],
             ["What is this creature?","Margwa","Shadowman","Hellhound","Lagoon","3"],
             ["Which perk caused you to create an explosion when diving to prone?", "JuggerNog", "PHD FLOPPER", "Widow's Wine", "Deadshot","2"],
             ["Which one of the guns is not a wonder weapon?","Wunderwaffle","Apothican Servant","M14","Ray Gun", "3"],
             ["Which one of these characters is obsessed with Vodka?","Nikolai","Takeo","Dempsey","Richtofen"]
             
             ]



item =-1
right=0
wrong=0


#question and choices
choice = StringVar()
choice.set("?")
qLabel = Label(text="This is a question", width=50)
qLabel.config(font=("Times", 20),bg='black',width=50, fg='yellow')
imgLabel = Label(image = image1)

#choice a,b,c,d

choiceA = Radiobutton(text = "Choice A", value = "1", variable = choice, command = go, font = ("Comic Sans MS", 20),bg='#5e3636')
choiceB = Radiobutton(text = "Choice B", value = "2", variable = choice, command = go, font = ("Comic Sans MS", 20),bg='#5e3636')
choiceC = Radiobutton(text = "Choice C", value = "3", variable = choice, command = go, font = ("Comic Sans MS", 20),bg='#5e3636')
choiceD = Radiobutton(text = "Choice D", value = "4", variable = choice, command = go, font = ("Comic Sans MS", 20),bg='#5e3636')




## PUT WIDGETS ON GRID -> ex:  thing.grid(row=1, column=1) ##
qLabel.grid(row=1 , column= 1,columnspan=3)
rightlabel.grid(row=2 , column=2,sticky=W )
wronglabel.grid(row=2 , column=3,sticky=W )
imgLabel.grid(row=3 , column=1,columnspan=3)
choiceA.grid(row=4 , column=2 ,sticky=W)
choiceB.grid(row=4 , column=3 ,sticky=W)
choiceC.grid(row=5 , column=2 ,sticky=W)
choiceD.grid(row=5 , column=3 ,sticky=W)
mainbutton.grid(row=1,column=1,columnspan=3,rowspan=6)
nextbutton.grid(row=6,column=1,columnspan=3)
nextbutton.grid_remove()
pressstarttoplaybutton.grid(row=10,column=1)
gameoverimglabel.grid(row=7,column=1,columnspan=4)
gameoverimglabel.grid_remove()

#removing the main game in the start menu
qLabel.grid_remove()
imgLabel.grid_remove()
choiceA.grid_remove()
choiceB.grid_remove()
choiceC.grid_remove()
choiceD.grid_remove()
rightlabel.grid_remove()
wronglabel.grid_remove()

#mainloop that helps the program stay on in pycharm
mainloop()

