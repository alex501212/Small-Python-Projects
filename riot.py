from riotwatcher import RiotWatcher, ApiError
watcher = RiotWatcher('*****') # API key would be here

i = 0
while i == 0:
    region_input = input("Select your region: ")
    if region_input == "1":
        my_region = "br1"
        i += 1
    elif region_input == "2":
        my_region = "eun1"
        i += 1
    elif region_input == "3":
        my_region = "euw1"
        i += 1
    elif region_input == "4":
        my_region = "jp"
        i += 1
    elif region_input == "5":
        my_region = "la1"
        i += 1
    elif region_input == "6":
        my_region = "la2"
        i += 1
    elif region_input == "7":
        my_region = "na1"
        i += 1
    elif region_input == "8":
        my_region = "oc1"
        i += 1
    elif region_input == "9":
        my_region = "tr1"
        i += 1
    elif region_input == "10":
        my_region = "ru"
        i += 1
    else:
        print("Invalid Input.")

user = input("Enter your summoner name: ")

me = watcher.summoner.by_name(my_region, user)

name = me.get("name")
level = me.get("summonerLevel")

print("\nLevel:", level, "\nName:", name)
