# ingredients for 2 large pizzas
flour = 250  # grams
yeast = 3  # grams
salt = 0.25  # teaspoons
sugar = 0.5  # teaspoons
water = 160  # millilitres

pizzaNum = int(input("Enter the amount of pizzas you want make: "))

print("\nRequired ingredients:\n", flour/2*pizzaNum, " grams of flour, ", yeast/2*pizzaNum, " grams of yeast, ",
      salt/2*pizzaNum, " teaspoons of salt, ", sugar/2*pizzaNum, " teaspoons of sugar and ", water/2*pizzaNum,
      " millilitres of water.", sep="")
