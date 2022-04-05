element=int(input("Enter element Number: "))
dict1={}
for i in range(element):
    key=input("Enter Key: ")
    value=input("Enter value: ")
    dict1.update({key:value})
print(dict1)
string=input("Enter dictonary: ")
string=string.strip("{")
string=string.strip("")
string=string.split(",")
dict1={}
key=''
value=''
for i in string:
    for j in i:
        if j==":":
            key=i[0]
            value=i[2::]
            dict1.update({key:value})
print(dict1)