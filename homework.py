import random
# def game():
#     a = random.randint(1, 100)
#     b = 0
#     print(f'')
#
#     while True:
#         d = int(input("Cан танда:     "))
#         b += 1
#
#         if a < d:
#             print ("Cен тандаган сан чон ")
#         elif a > d:
#             print ('Сен тандаган сан кичине')
#         else:
#             print(f'Cен тандаган сан {a} = {d} менен барабар попытка {b}')
#             break
#
# game()


#2 Task
# import random
# def game():
#         a=random.randint(1, 2)
#         b= 1 or 2
#         print("Оюн башталды")
#
#         if a == b:
#             print("Орел")
#         else:
#             print("Решка")
#
# game()

import random
def fruit():
    fruits= ["алма", "банан", "анар", "хурма", "алмурут", "алча", "кулпунай", "арбуз", "коон"]
    a=random.choice(fruits)
    attempt=0
    print ("Созду тап")

    while True:
        d = (input("Cоз танда:     "))
        attempt += 1
        if d == a:
            print(f"Куттуктайм созду, {attempt}- аракеттен кийин таптын")
            break
        else:
            print("Cозду тапкан жоксун")
fruit()












