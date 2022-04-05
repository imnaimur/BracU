string=input("Enter Dictonary: ")
string=string.strip("{")
string=string.strip("}")
string=string.replace(",",":")
string=string.split(":")
count=1
key=string[::2]
value=string[1::2]
sum=0
count=0
for i in value:
    sum+=int(i)
    count+=1
avg=sum/count
print("Average is ",avg)