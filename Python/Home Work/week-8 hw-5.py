def unique_dictonary(string):
    string1=[]
    dict1={}
    for i in string:
        count=0
        if i not in string1:
            string1.append(i)
    for j in string1:
        count=0
        for i in string:
            if i==j:
                count+=1
        dict1.update({j:count})
    sortedbyval={k:v for k,v in sorted(dict1.items(),key=lambda v:v[1])}

    print(sortedbyval) 

string=input("Enter a space separated string: ")
string=string.split(" ")
unique_dictonary(string)