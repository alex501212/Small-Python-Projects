input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
input3 = int(input("Enter the third number: "))

maxNum = max(input1, input2, input3)
minNum = min(input1, input2, input3)
middleNum = input1 + input2 + input3 - maxNum - minNum

print("\nLargest Value: ", maxNum, "\nMiddle Value: ", middleNum, "\nSmallest Value: ", minNum, sep="")
