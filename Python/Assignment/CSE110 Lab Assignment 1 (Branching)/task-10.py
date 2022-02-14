working_hour=int(input("Enter the hours worked: "))

if working_hour<0:
    print("Hour cannot be negative")
elif working_hour<=40:
    print(working_hour*200)
elif working_hour>40 and working_hour<168:
    print((working_hour-40)*300+8000)
else:
    print("Impossible to work more than 168 hours weekly")