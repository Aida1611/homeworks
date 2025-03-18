##try-except-  1 try га except обязательно жазыш керек
# try:
#     a = 5
#     b = 0
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Санды нолго болгонго болбойт")
#
# try:
#     a = int (input())
#     b = int (input())
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Санды нолго болгонго болбойт")     ##-каждую ошибку нужно  прописать отдельно
# except ValueError:
#     print("Тексти санга болгонго болбойт")
# except Exception:
#     print("Кандайдыр бир ката бар")
#
#
# try:
#     a = int (input())
#     b = int (input())
#     c = a/b
#     print(c)
# except (ZeroDivisionError,ValueError):    ###-мындай жазганга болбойт
#     print("Санды нолго болгонго болбойт")

#
# def is_date(day, month, year):
#     from datetime import date
#     try:
#         return date(year, month, day)
#     except ValueError:
#         return "Календарда мындай дата жок!"
# print(is_date(18, 3, 2025))
# print(is_date(29, 2, 2025))
# print(is_date(29, 2, 2100))


numbers = [1, 2, 3, 4, 5]
def get_element ():
    try:
        index = int(input("Введите индекс: "))
        return numbers [index]
    except IndexError:
        return "Мындай элемент менен индекс жок"
    except Exception:
        return "Кандайдыр бир ката бар"
print(get_element())













