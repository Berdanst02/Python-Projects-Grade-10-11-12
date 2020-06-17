#Candy Giver
#how much does each kid get
candy = int(input("Enter the amount of candies you have>>>"))

students = int(input("Enter the amount of stude+nts you have>> "))
#proccess
candygiventostudents =(candy/students)

remainder = candy % students
#Output
print("Each kid will get %d amount of candies and you will have remainder of %d of candies"%(candygiventostudents, remainder))
