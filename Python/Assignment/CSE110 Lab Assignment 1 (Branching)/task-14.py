from math import *
f=int(input("Enter the temperature: "))
c=((f-32)*0.56)
d=floor(c)
#c = clsius temperature
#f = farenheit ||
if (c-d)<0.0005:
    c=d
if c<20 :
    print(c,end=' ')
    print("degrees C")
    print("Winter")
elif 20<=c<=25:
    print(c,end=' ')
    print("degrees C")
    print("Autumn")
elif 25<c<30:
    print(c,end=' ')
    print("degrees C")
    print("Spring")
else :
    print(c,end=' ')
    print("degrees C")
    print("Summer")
