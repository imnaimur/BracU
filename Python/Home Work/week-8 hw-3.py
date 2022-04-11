string1=input("Enter string: ")
list1=[]
for i in string1:
    if i not in list1:
        j=ord(i)
        list1.append(str(j)+i+str(j))
print(list1)