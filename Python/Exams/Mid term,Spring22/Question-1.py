string=input("Enter a string: ")
ind=0
dig=0
vow=0
con=0
for x in string:
    val=ord(string[ind])
    if 48<=val<=57:
        dig+=1
    elif val==97 or val==101 or val==105 or val==111 or val==117:
        vow+=1
    elif val==32:
        pass
    else:
        con+=1
    ind+=1
print("digit",dig)
print("vowel",vow)
print("cons",con)

