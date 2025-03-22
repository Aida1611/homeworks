# def main(name, age):
#     return f'Привет, меня зовут {name}, мне {age}'
#
# print(main(12, 'Aман'))
# print(main (age=12, name="Аман"))
#
#
# def main(name, age='не указан'):
#     return f'Привет, меня зовут {name}, мне {age}'
#
# print(main (name="Аман"))
#
#
# '''
# main(name='Аман')-именованный
# main('Аман')-позиционный
# def main(name 'Аман')-дефолтное значение, не объязательный аргумент
# '''
#
# def custom_sum(*args):
#     return sum(args)
# print(custom_sum (2, 4, 6, 8, 9))


# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# ##Пример использования
# print_info(name="Aнна", age=25, city="Москва")
# print_info(width= 20, height=20)


def create_profile(*hobbies, **info):
    print(f'хобби : {hobbies}')
    for key, value in info.items():
        print(f'{key}: {value}')

create_profile("футбол", "теннис", name="Аман", age=25, city= 'Бишкек')








