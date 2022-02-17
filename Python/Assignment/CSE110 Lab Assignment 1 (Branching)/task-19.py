canvas=int(input("Enter the number of canvas: "))
paint=int(input("Enter the number of paint: "))
total=(canvas*120)+(paint*75)
if total<299:
    print("Previous total:",total)
    print("New total after discount:",total)
elif 300<=total<=499:
    print("Previous total:",total)
    print("New total after discount:",total-10)
elif 500<=total<=746:
    print("Previous total:",total)
    print("New total after discount:",total)
elif 750<total<=999:
    print("Previous total:",total)
    print("New total after discount:",total-50)
else:
    print("Previous total:",total)
    print("New total after discount:",total-150)
    