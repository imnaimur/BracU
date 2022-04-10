string=input("Enter string: ")
string=string.lower()
dict1={}
for i in string:
    if i not in dict1:
        if i==" ":
            continue
        else:
            dict1[i]=1
    else:
        dict1[i]+=1
print(dict1)