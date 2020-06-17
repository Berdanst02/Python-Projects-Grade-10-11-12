import random as r

dice1 = r.randint(1,6)
dice2 = r.randint(1,6)

total = dice1 + dice2

print("I rolled %d and %d for a total of %d" %(dice1,dice2,total))
