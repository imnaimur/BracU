time=int(input("Enter an hour: "))
if 0<=time<=23:
    if 4<=time<=6:
        print("Breakfast")
    elif 12<=time<=13:
        print("Lunch")
    elif 16<=time<=17:
        print("Snacks")
    elif 19<=time<=20:
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Wrong Time")