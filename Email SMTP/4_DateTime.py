import datetime as dt

now=dt.datetime.now()
print(now)

year=now.year
print(year)

if year==2020:
    print("Wear a mask")

day_of_the_week=now.weekday()
print(day_of_the_week)

date_of_birth=dt.datetime(year=2003,month=12,day=9)
print(date_of_birth)

