speed = 20 

for seconds in range(10,-1,-1):
    print("at t-%d seconds speed is %.2f"%(seconds, speed))
    speed = speed + 0.10 * speed
print("-------------------------")
print("It hits the ground at %.2f km/hr"%(speed))