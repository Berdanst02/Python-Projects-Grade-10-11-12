goal = 320000
pop = 160000
year = 2020
while True:
    year+=10
    pop = pop * 1.06
    print("year: %d >>> population = %d"%(year, pop))
    if pop >= goal:
        break
print("============================")
print("Barrie's population will double by the year %d"%(year))