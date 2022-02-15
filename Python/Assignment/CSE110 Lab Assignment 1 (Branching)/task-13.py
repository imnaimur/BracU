marks=int(input("Enter your marks: "))
if 0<=marks<=100:
    if 90<=marks<=100:
        print("A")
    elif 80<=marks<=89:
        print("B")
    elif 70<=marks<=79:
        print("C")
    elif 60<=marks<=69:
        print("D")
    elif 50<=marks<=59:
        print("E")
    else:
        print("F")