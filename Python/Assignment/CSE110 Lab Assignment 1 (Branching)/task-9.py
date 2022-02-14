#Write the Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds. The number of seconds is taken as input from the user.
#sec1 and sec2 variable represetns the seconds
#hr and min repesents hour and minute respectively
sec1=int(input("Enter the number of seconds: "))
hr=sec1//3600
min=(sec1%3600)//60
sec2=((sec1%3600)%60)
print(f"Hours: {hr} Minutes: {min} Seconds: {sec2}")