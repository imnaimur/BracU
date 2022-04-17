# def show_palindrome(var):
#     for i in range(var):
#         print(i+1,end="")
#     for i in range(var):
#         sum1=var-1-i
#         if sum1>0:
#             print(var-1-i,end="")
# show_palindrome(5)
def show_palindrome(var):
    string=''
    string2=''
    for i in range(var):
        string+=str(i+1)
        val=var-i-1
        if val>0:
            string2+=str(var-i-1)
    print(string,end="")
    print(string2)
number=int(input("Enter a number: "))
show_palindrome(number)