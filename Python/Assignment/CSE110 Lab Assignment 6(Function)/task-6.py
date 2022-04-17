def year_month_day(var):
    year=var//365
    month=(var%365)//30
    days=(var%365)%30
    print(year,"years",month,"months and",days,"days")
day=int(input("Enter Days: "))
year_month_day(day)