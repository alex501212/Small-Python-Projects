currentTime = int(input("Enter current time (in hours): "))
waitTime = int(input("Enter the number of hours you want to wait: "))

alarm = currentTime + waitTime
outPut = alarm % 12

print("The alarm will go off at:", outPut)
