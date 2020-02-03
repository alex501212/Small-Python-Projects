# nails price and p&p price in £0.00 format
nailsPrice = 0.10
postagePrice = 2.00

# number of nails bought and their corresponding discount %
nailsBought1to50 = 0.00
nailsBought51to100 = 0.10
nailsBought100to200 = 0.20
nailsBought200Plus = 0.25

nailsAmount = float(input("How many nails do you want to buy? "))

# calculates the amount of discount to be applied
# calculates the price before postage and packaging
# calculates the total amount including postage and packaging

if (nailsAmount >= 1) and (nailsAmount <= 50):
    print("\n", int(nailsBought1to50*100), "% Discount Applied.", sep="")
    print("Total (excluding P&P): £", format(nailsAmount*nailsPrice*nailsBought1to50, ",.2f"), sep="")
    print("Total (including P&P): £", format(nailsAmount*nailsPrice*nailsBought1to50+postagePrice, ",.2f"), sep="")
elif (nailsAmount >= 51) and (nailsAmount <= 100):
    print("\n", int(nailsBought51to100*100), "% Discount Applied.", sep="")
    print("Total (excluding P&P): £", format(nailsAmount*nailsPrice*nailsBought51to100, ",.2f"), sep="")
    print("Total (including P&P): £", format(nailsAmount*nailsPrice*nailsBought51to100+postagePrice, ",.2f"), sep="")
elif (nailsAmount >= 100) and (nailsAmount <= 200):
    print("\n", int(nailsBought100to200*100), "% Discount Applied.", sep="")
    print("Total (excluding P&P): £", format(nailsAmount*nailsPrice*nailsBought100to200, ",.2f"), sep="")
    print("Total (including P&P): £", format(nailsAmount*nailsPrice*nailsBought100to200+postagePrice, ",.2f"), sep="")
elif nailsAmount >= 200:
    print("\n", int(nailsBought200Plus*100), "% Discount Applied.", sep="")
    print("Total (excluding P&P): £", format(nailsAmount*nailsPrice*nailsBought200Plus, ",.2f"), sep="")
    print("Total (including P&P): £", format(nailsAmount*nailsPrice*nailsBought200Plus+postagePrice, ",.2f"), sep="")
