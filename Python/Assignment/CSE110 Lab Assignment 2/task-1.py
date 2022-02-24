
# a) 24, 18, 12, 6, 0, -6
# b) -10, -5, 0, 5, 10, 15, 20
# c) 18, 27, 36, 45, 54, 63
# d) 18, -27, 36, -45, 54, -63

#a
# for counter in range(24,-7,-6):
#     if counter ==-6:
#         print(counter,end="")
#     else:
#         print(counter, end=",")


#b
# for counter in range(20,-6,-5):
#     if counter ==-5:
#         print(counter,end="")
#     else:
#         print(counter, end=",")

#c
# for counter in range(63,17,-9):
#     if counter ==18:
#         print(counter)
#     else:
#         print(counter,end=",")

# d
for count in range(54,-19,-18):
    if count<0:
        for count in range(-27,-64,-18):
            if count==-63:
                print(count)
            else:
                print(count,end=",")
    else :
        print(count,end=",")