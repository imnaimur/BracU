string="{4:'CSE110',9:'CSE111',6:'CSE421',1:'CSE420'}"
# for i in list1:
#     for j in i:
#         if j==":" :
#             key=i[0]
#             value=i[2::]
#             print(key,":",value)
key=[]
value=[]
ind=0
# for i,j in dict1.items():
#     key+=[i]
#     value+=[j]
# string=input("Enter dictonary: ")
string=string.strip("{")
string=string.strip("}")
string=string.replace(",",":")
string=string.split(":")
key=string[::2]
value=string[1::2]
dict1={}
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