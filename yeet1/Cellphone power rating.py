#cell phone power rating
power = float(input("Type the power consumption for your cellphone in one day in watts>>>"))

if power < 0.03:
    print("Your Rating for power consumption is 5 stars! since the amount of power you used is %.2f watts"%(power))

elif power >=0.03 and power <=0.15:
    print("Your Rating for power consumption is 4 stars! since the amount of power you used is %.2f watts" % (power))

elif power > 0.15 and power <=0.25:
    print("Your Rating for power consumption is 3 stars! since the amount of power you used is %.2f watts" % (power))
elif power > 0.25 and power <= 0.35:
    print("Your Rating for power consumption is 2 stars! since the amount of power you used is %.2f watts" % (power))
elif power > 0.35 and power <= 0.5:
    print("Your Rating for power consumption is 1 star since the amount of power you used is %.2f watts" % (power))
elif power > 0.5 and power < 1:
    print("YOU RECIEVE NO STARS!")
else:
    print("Invalid Number try again")
