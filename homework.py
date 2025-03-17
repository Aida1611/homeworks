##1-Task
from calendar import month
def season(month):
    if 3 <= month <= 5:
        return "Весна"
    elif 6 < month < 8:
        return "Лето"
    elif 9 < month < 11:
        return "Осень"
    else:
        return "Зима"
print(season(1))
print(season(2))
print(season(3))
print(season(4))
print(season(5))
print(season(6))
print(season(7))
print(season(8))
print(season(9))
print(season(10))
print(season(11))
print(season(13))

##2-Task
from datetime import date
from datetime import datetime, date
from calendar import month
from datetime import date, MAXYEAR, MINYEAR
def date (day, month, year):
    if 1 <= day < 31 and 1 < month < 12 and MINYEAR  < year < MAXYEAR:
        return "True"
    else:
        return "False"

print(date(29,2, 2020))
print(date(30,2, 2021))
print(date(31,4, 2023))
print(date(15,8, 2023))



