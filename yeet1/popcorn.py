import os
age=int(input("Enter your age, must be between 1 and 99>>>"))

if age > 0 and age < 18:
    price=8
    group="Child"
elif age >=18 and age <=99:
    price=12
    group="Adult"
else:
    print("Not a valid age, exiting program")
    os._exit(0)
    
print("Ticket Price is $%.2f"%(price))
print("your group is %s"%(group))











popcorn=input("Type 'y' if you want popcorn>>>")

if popcorn=="y" or popcorn=="Y":
    print("Popcorn added to price")
    price += 5
    
    butter = input("type 'y' again if you want to add butter for extra $1>>")
    if butter=="y" or butter=="Y":
        print("Butter Added")
        price +=1
    else:
        print("Butter declined")
else:
    print("Popcorn declined")
withtax = price * 1.13
print("Final Price is $%.2f with tax"%(withtax))