import datetime
from datetime import date

my_time = datetime.time(2, 20)
print(my_time.minute)

today = datetime.date.today()
print(today)
print(today.ctime())

whole_date = datetime.datetime(2020, 12, 20, 13, 30, 1)
print(whole_date)
whole_date = whole_date.replace(year=2021)
print(whole_date)

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

difference = date1 - date2
print(difference)

datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)
difference2 = datetime1 - datetime2
print(difference2)