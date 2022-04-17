def calculate_tax(age,job,salary):

    if age<18 or job=="president" or salary<10000:
        print("0")
    elif 10000<salary<20000:
        sum1=salary*(5/100)
        print((sum1))
    else:
        sum1=salary*(10/100)
        print(sum1)
age=int(input("Enter Age: "))
salary=int(input("Enter Salary: "))
job=input("Enter Job designation: ")
job=job.lower()
calculate_tax(age,job,salary)