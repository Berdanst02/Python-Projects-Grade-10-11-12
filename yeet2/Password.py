password = "secret"

while True:
    guess = input("Enter password>>>")
    if guess==password:
        break
    else: 
        print("Invalid Password, try again")
print("Access Granted")

while True:
    try:
        num=int(input("Enter number from 1 to 10>>>"))
    except:
        print("That was not a number")
        continue    
    
    if num > 0 and num <= 10:
        break
    else:
        print("Invalid, try again")
        
print("Thank You")