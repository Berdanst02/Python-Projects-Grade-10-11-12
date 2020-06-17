money = 20000
for years in range(1,19):
    money = money * 1.06
    print("year of Birthday: %d and you have %.2f now"%(years, money))

print("Money is %.2f"%(money))