print("*Enter miles driven*")

milesDriven = float(input())

print("*Enter gallons of fuel used*")

fuelUsed = float(input())

print(format(milesDriven/fuelUsed, ".2f"), "mpg", sep="")
