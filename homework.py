#1-Задача
name = input("Атыныз ким: ")
age = int (input("Жашыныз канчада: "))
print(f"Салам {name}, Сен {age} жаштасын")

#2-Задача
a = int(input("Кайсы сан: "))
b = int(input("Кайсы сан: "))
print(f"Cандар {a} жана {b} суммасы {a + b}")

#3-Задача
numbers = input().split(",")

while True:
    number = int(input("Число для списка: "))
    if str (number) in numbers:
        print(f"Cан {i} табылды")
        break
    else:
        print(f"Cay {number} табылган жок: ")
#
# # #4-Задача
n= [7, 9, 13, 18, 21]
for num in n:
    if num % 2 == 0:
        print(f"Биринчи жуп сан {num}")
        break

#5-Задача
while True:
    num = int (input("Сыр созду киргизиниз: "))
    if num  == 1234:
        print(f"Кирууго уруксат берилди")
        break
