yearNow = int(input("Enter the Current Year: "))

if (yearNow % 100 == 0) and (yearNow % 400 == 0):
    print("It is currently a leap year.")
elif (yearNow % 100 != 0) and (yearNow % 4 == 0):
    print("It is currently a leap year.")
else:
    print("It is currently not a leap year.")
