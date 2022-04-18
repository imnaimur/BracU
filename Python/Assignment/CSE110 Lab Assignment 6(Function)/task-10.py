def make_square(var1, var2):
    dict1 = {}
    var = var2-var1+1
    for i in range(var):
        value = var1**2
        key = var1
        dict1.update({key: value})
        var1 += 1
    print(dict1)


num = input("Enter a tuple: ")
num = num.strip("()")
num = num.split(",")
num = tuple(num)
starting, ending = num
make_square(int(starting), int(ending))
