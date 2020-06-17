
km = float(input("Enter the amount of km you will travel to get the amount money will pay including 15% tip and taxi fare of $3.50>>>"))


moneycostkm = km * 0.50
taxifare = 3.50

total = (moneycostkm + taxifare)

tip = total * 0.15

totalwiththetip = total * 1.15

print("Total: %.2f"%(total))
print("Tip: %.2f"%(tip))
print("Total with the tip: %.2f"%(totalwiththetip))
