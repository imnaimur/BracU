def ascii_char_ascii(string):
    list1=[]
    list2=[]
    for i in string:
        if i not in list1:
            list1.append(i)
            j=ord(i)
            list2.append(str(j)+i+str(j))
    print(list2)
string1=input("Enter a string: ")
ascii_char_ascii(string1)