hotels = ["Comfortn INN","Daily INN","Home INN","Barrie INN","Niagra INN","Hilton INN","Discord INN","Steam INN","Hotel Monville","Motel Honville"]
pricespernight = [230,20,70,160,54,34,178,120,45,69]

cheap = []
expensive = []
ccounter=1
ecounter=1

for x in range(0,len(pricespernight)):
    if pricespernight[x] <=100:
        cheap.append("%d > Hotel: %s : Price: $%d"%(ccounter, hotels[x], pricespernight[x]))
        ccounter +=1
    else:
        expensive.append("%d > Hotel: %s : Price: $%d" % (ecounter, hotels[x], pricespernight[x]))
        ecounter += 1
        
print("List of Cheap Hotels \/\/\/")
print("====================================================")
for ch in cheap:
    print(ch)

print('\n')
print('\n')
print("List of Expsensive Hotels \/\/\/")
print("====================================================")
for ex in expensive:
    print(ex)

input("type in anything to continue")
exit()


