def special(var,n):
    string1=""
    string2=""
    for j in range(len(var)):
        if j%n==0 and j>0:
             string1+=(var[j])
        else:
            string2+=(var[j])
    print(string2+string1)
string=input("Enter a string: ")
position=int(input("Enter a postion: "))
special(string,position)
# "Python is easy to learn.I love python."