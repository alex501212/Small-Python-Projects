months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
i = 0
rainfall = [0] * 12

while i != 12:
    try:
        print("Enter rainfall for ", months[i], ":", end="", sep="")
        rainfall[i] = int(input())
        i += 1
    except:
        print("--------------------------\n",
              "Enter a correct data type."
              "\n--------------------------", sep="")
total_rain = sum(rainfall)
print("\nTotal rainfall for the year:", total_rain)

average_rain = sum(rainfall) / len(rainfall)
print("Average monthly rainfall:", average_rain)

min_max_rain = sorted(rainfall)
min_rain = min_max_rain[0]
max_rain = min_max_rain[-1]
print("Maximum monthly rainfall:", min_rain)
print("Minimum monthly rainfall:", max_rain)
