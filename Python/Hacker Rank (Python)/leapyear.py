year = int(input())
leapyear=False
if( year%4==0 and year%100!=0) or (year%4==0 and year%400==0):
    leapyear=True
print(leapyear)