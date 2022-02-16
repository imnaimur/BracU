distance=int(input("Enter distances: "))
time=int(input("Enter meters: "))
v=(distance*3600)/(time*1000)
if v<60:
    print(v,end=" ")
    print("Km/h")
    print("Too slow. Needs more changes.")
elif 60<=v<=90:
    print(v,end=" ")
    print("Km/h")
    print("Velocity is okay. The car is ready!")
else :
    print(v,end=" ")
    print("Km/h")
    print("Too fast. Only a few changes should suffice.")