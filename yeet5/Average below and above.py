import random as r

marks = []
aboveaverage = []
belowaverage = []

average = 0

####

for x in range(0,30):
    marks.append(r.randint(20,100))
    average += marks[x]

#

average = average / len(marks)

print("The Average of the marks is %.2f"%(average))

for m in marks:
    if m >= average:
        aboveaverage.append(m)
    else:
        belowaverage.append(m)

aboveaverage.sort()
belowaverage.sort()
print("There are %d marks over %d"%(len(aboveaverage),average))

for aa in aboveaverage:
    print(aa, end = " ,  ")
    
    
print("\n=======================================================================================")

print("There are %d marks under %d"%(len(belowaverage),average))
for ba in belowaverage:
    print(ba, end = " ,  ")