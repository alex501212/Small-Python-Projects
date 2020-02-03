orgPrice = float(input("Welcome to Alex's Discount Calculator\n Enter the Item's Original Price: £"))

saleAmount = float(input("Enter Sale Percentage: ")) / 100

salePrice = format(orgPrice - (orgPrice * saleAmount), ".2f")
print("£", salePrice, " is the sale price.", sep="")
