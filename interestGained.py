initialAmount = float(input("Enter the amount of the fund to be deposited: £"))
interestRate = float(input("Enter the interest rate: ")) /100
noOfYears = float(input("Enter the number of years: "))

interest = initialAmount * interestRate * noOfYears
totalFunds = interest + initialAmount * noOfYears

print("\nInterest gained: £", format(interest, ",.2f"), "\nTotal funds that will be available: £", format(totalFunds, ",.2f"), sep="")
