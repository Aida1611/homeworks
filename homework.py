##1-Задача
res = [i for i in range (1, 21)]     #1 ден 20 га чейинки жуп сандарга болунгон свндвр
print(res)

##2-Задача
res = [i ** 2 for i in range (1, 11)]     #1 ден 10 го чейинки сандардын вкадраттарынын тизмеси
print(res)

##3-Задача
numbers = [5, 12, 7, 18, 3, 10, 8]
res = [n for n in numbers if n > 7]     #7 ден чон сандарды тандоо
print(res)

##4-Задача
words = ["яблоко", "банан", "вишня"]   ##создорду чон тамгага озгорт
res = [i for i in words]
print(res)

##5-Задача
number= int (input("Сан жазыныз: "))
res = "Он сан" if number > 0 else  "Терс сан"
print(res)

##6-Задача
number= int (input("Сан жазыныз: "))
res = "Жуп сан" if number % 2 == 0 else  "Так сан"
print(res)

##7-Задача
n = [4, -1, 7, -3, 0, 9, -2]
res = [i if i >= 0 else 0 for i in n]
print(res)