total = 0 
for hole in range (1,10,1):
    while True:
        try:
            shot = int(input("Enter a score for hole %d>>>  "%(hole)))
        except:
            print("Error must be a number")
            continue
        if shot < 1:
            print("Must be a positive number")
        elif shot > 10:
            shot = 10
            print("Shot is capped at 10")
            total += shot 
        else:
            total +=shot
            break
    total += shot
    
print("Your final score is %d"%(total))