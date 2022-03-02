i=1
sum=0
avg=0
qty=int(input("Enter the quantity: "))
minimum=0
maximum=0
for count in range(qty):
    number=int(input("Enter a numnber: "))
    sum+=number
    if number>maximum:
        maximum=number
    if number<minimum:
        minimum=number
avg=sum/qty
print("Maximum",maximum)
print("Minimum",minimum)
print("Average",avg)