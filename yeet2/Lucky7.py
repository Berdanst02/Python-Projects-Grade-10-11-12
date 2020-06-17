import random as r 
tries = 0 

while True:
    number = r.randint(1,100)
    tries +=1
    print("Try %d: >>> %d"%(tries, number))
    if number==7:
        break
        
print("================================")
print("It took %d tries to get 7"%(tries))