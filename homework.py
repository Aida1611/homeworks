##1-Task
from calendar import month
def season (month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Другое"
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
print(season(12))


###1

def season (month):
    if month in (1, 2, 12):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Другое"
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
print(season(12))

##2-Task
from datetime import date
def is_date (day, month, year):
   return date (year, month, day)

print(is_date(29,2, 2020))
print(is_date(29,2, 2025))
print(is_date(30,2, 2021))
print(is_date(31,4, 2023))
print(is_date(15,8, 2023))



def func(a,b, c): # a,b, c-параметр
    pass
func(2, 4, 5)
