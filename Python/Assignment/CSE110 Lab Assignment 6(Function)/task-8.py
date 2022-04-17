def show_palindromic_triangle(var):
    string=''
    string2=''
    for i in range(var):
            space_creator="  "*(var-i)
            string+=str(i+1)+" "
            if i>0:
                string2+=" "+str(i)
            print(space_creator,end="")
            print(string,end="")
            print(string2[::-1])
number=int(input("Enter a number: "))
show_palindromic_triangle(number)