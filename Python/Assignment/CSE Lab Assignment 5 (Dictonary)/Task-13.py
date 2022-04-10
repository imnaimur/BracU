list1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dict1={}
val1=[]
val2=[]
val3=[]
for i in list1:
    for j in i:
        if j=='a':
            val1.append(i[1])
        elif j=='b':
            val2.append(i[1])
        elif j=='c':
           val3.append(i[1])
    dict1.update({'a':val1})
    dict1.update({'b':val2})
    dict1.update({'c':val3})
print(dict1)