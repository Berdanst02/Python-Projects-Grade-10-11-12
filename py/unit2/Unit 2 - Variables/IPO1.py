#speed converter
#converts km/h to m/h
#3 step IPO METHOD

#1 --> input = ASK FOR INFO

kmh = float(input("Enter your speed in km/hr >>>"))

#2 > processing = does the calculation needed for the answer
miles = kmh * 0.62131

#step 3 > Output = print the answer to the screen

print("%.2f km - %.2f miles"%(kmh,miles))


