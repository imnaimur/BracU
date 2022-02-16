cgpa=float(input("Enter CGPA: "))
credit=int(input("Enter credit: "))
if cgpa>=3.8 and credit>=30:
    if  3.80<=cgpa<=3.89:
        print("The student is eligible for a waiver of 25 percent")
    elif 3.90<=cgpa<=3.94:
        print("The student is eligible for a waiver of 50 percent")
    elif 3.95<=cgpa<=3.99:
        print("The student is eligible for a waiver of 75 percent")
    else:
        print("The student is eligible for a waiver of 100 percent")
else:
    print("The students is not eligible for a waiver ")