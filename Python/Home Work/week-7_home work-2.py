string=input("Enter dictonary: ")
string=string.strip("{")
string=string.strip("}")
string=string.split(",")
dict1={}
for i in range(string):
    key=input("Enter Key: ")
    value=input("Enter value: ")
    dict1.update({key:value})
key=[]
value=[]
ind=0
for i,j in dict1.items():
    key+=[i]
    value+=[j]
maxkey=key[0]
minkey=key[0]
maxval=value[0]
minval=value[0]
for i in key:
    if i>maxkey:
        maxkey=i
    if i<minkey:
           minkey=i
for j in value:
    if j>maxval:
        maxval=j
    if j<minval:
        minval=j
print(maxkey,minkey,maxval,minval)