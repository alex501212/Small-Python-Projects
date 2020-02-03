item_count = int(input("How many items do you want to enter? "))

while item_count < 3:
    print("---------------\n"
          "Invalid amount."
          "\n---------------")
    item_count = int(input("How many items do you want to enter? "))

items = []
while item_count != 0:
    user_input = input("Enter name of item: ")
    items.append(user_input)
    item_count -= 1
#items = ["car", "boat", "train", "plane", "rocket", "tram", "yacht"]

length = len(items) - 1
i = 0
while length != 0:
    print(items[i], ", ", sep="", end="")
    i += 1
    length -= 1
print("and", items[-1], end="")
