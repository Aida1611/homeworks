summ = 0
# бул цикл чексиз цикл
while True:
    number = int (input("Введите одно число: "))
    if number == 0:
        break    # бул циклдин ишин токтотот
    summ += number
    print(f"Общая сумма = {summ}")

