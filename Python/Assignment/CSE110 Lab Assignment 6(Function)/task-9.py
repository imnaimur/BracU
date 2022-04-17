import math
def area_circumference_generator(r):
    Pi=math.pi
    area=Pi*(r**2)
    circumference=2*Pi*r
    return area,circumference
rad=int(input("Enter Radius: "))
b=area_circumference_generator(rad)
print(b)
area,cir=b
print(f"Area of the circle is {area} and circumference is {cir}")