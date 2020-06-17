import random as r

tries = 1 
answer = r.randint(1,100)

while True:
    print("You are on guess #%d"%(tries))
    try:
        guess = int(input("Enter a guess from 1 to 100>>>"))
    except:
        print("Must be a number")
        continue
    if guess > answer and guess < 101:
        print("Too high guess lower buddy")
        tries +=1
    elif guess < answer and guess > 0:
        print("Too low guess higher buddy")
    elif guess == answer:
        print("You won!")
        break
    else:
        print("Error, guess is invalid")


print("The number was %d and took %d tries."%(answer, tries))

