def foo_moo(num):
    if num%6==0:
        print("FooMoo")
    elif num%3==0:
        print("Moo")
    elif num%2==0:
        print("Foo")
    else:
        print("Boo")
number=int(input("Enter a number: "))
foo_moo(number)