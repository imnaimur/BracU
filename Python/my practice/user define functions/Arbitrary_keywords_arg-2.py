# Arbitrary Keyword Arguments(**kwargs) store value in var as key value syntax as dictonary
# and its automatically convert valiable name into key and make it string if its a string.
def inform(**var):
    print(var)
    for i in var:
        print(var[i])
inform(name="naimur",id=22101075,age=22,address="Mohakhali")