names = ['Richtofen','Dempsey','Nikolai','Takeo']
emails = ['rt@gmail.com','dempsey@gmail.com','nikolai@gmail.com','takeo@gmail.com']


def menu():
    print("Characters in the Primis Crew")
    print("*****************************")
    print("%5s %10s %20s"%("Loc","Name","Email"))
    print("%5s %10s %20s"%("---","----","-----"))

    for x in range(0,len(names)):
        print("%5s %10s %20s"%(x,names[x],emails[x]))

    print("--------------------------------")

    print('1 - Add a person')
    print('2 - remove a person')
    print('3 - Modify a person')
    print('4 - Exit')

    print('===================================')

def addperson():
    name=input("Enter a name >>>")
    email=input("Enter email>>>")
    names.append(name)
    emails.append(email)
def removeperson():
    limit=len(names)
    item = input("Enter a number from 0 to %d>>>"%(limit))    
    item=int(item)
    if item >=0 and item <=limit:
    
        names.pop(item)
        emails.pop(item)
        print("Name was removed")
    else:
        print("Invalid Number")
#
def modifyperson():
    limit=len(names)
    item = input("Enter a number from 0 to %d>>>"%(limit))    
    item=int(item)
    
    if item >=0 and item <=limit:
        names[item]=input("Enter a new name>>")
        emails[item]=input("Enter a new email>>")
        
        print("Name was changed")
    else:
        print("Invalid Number")



#


def clear():
    print("==========================")
    input("Press enter to continue")
    for x in range(0,200):
        print("")



#

while True:
    menu()
    choice = int(input("Enter 1 to 4 >>>"))
    if choice==1:
        addperson()
    elif choice==4:
        break
    elif choice==2:
        removeperson()
    elif choice==3:
        modifyperson()

    else:
        print("That isn't working yet")
    clear()
        
