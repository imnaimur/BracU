def addition(*var):
    print(var)
    sum1 = 0
    for i in var:
        sum1 += i
    print(sum1)


#  Arbitrary Arguments store value in a variable as tuple
addition(1, 2, 3, 4, 5)
