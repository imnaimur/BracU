S=int(input("Enter a number: "))
if S<100:
    L=3000-(125*S**2)
    print(L)
else:
    L=12000/(4+(S**2/14900))
    print(L)