import datetime
currentYear = datetime.datetime.now()
currentYear = int(currentYear.year)

name = input("Enter your name: ")

age = int(input("Enter your age: "))

yearWhen100 = currentYear - age + 100

print("\n", name, " on the year of ", yearWhen100, " you will be 100 years old.", sep="")
