string=input("Enter Dictonary: ")
string=string.strip("{")
string=string.strip("}")
string=string.replace(",",":")
string=string.split(":")
value=string[1::2]
key=string[::2]
maxk=key[0]
maxv=value[0]
for i in value:
    if int(i)>int(maxv):
        maxv=i
name=key[value.index(maxv)]
print(f"The highest selling book genre is {name} and the number of books sold are {maxv}.")