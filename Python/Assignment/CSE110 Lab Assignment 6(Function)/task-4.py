def case_check(string):
    upper=0
    lower=0
    for i in string:
        if 65<=ord(i)<=90:
           upper+=1
        if 97<=ord(i)<=122:
            lower+=1
    print("No. of Uppercase characters: ",upper)
    print("No. of Lowercase characters: ",lower)
string1=input("Enter String: ")
case_check(string1)