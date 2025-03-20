# import random
# import datetime
#
# while True:
#     a = random.randint (0, 100)
#     print(a)
#
# from random import randint #Импорт коркретных объектов из модуля
# x =randint (0, 10)
#
# import datetime as dt
# now = dt.datetime.now()   #Импорт всего мождуля с псевдонимом
#
# from random import  * #импорт всех объектов из модуля
# randint(0, 4)


##random-cлучайные числа, другие
# import  model
# model.custom_sub(10, 5)


import model
from model import custom_sub

print(model.season(1))

a = model.custom_sum(10, 5)
print(model.custom_sub(a, 10))


language_code = input("Выберите язык:").strip().lower()
print(model.greet(language_code))

print(model.add_user('Aida'))
print(model.get_user())
print(model.delete_user('Aida'))
print(model.get_user())


