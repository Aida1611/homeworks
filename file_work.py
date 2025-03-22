# ##Записать файл
# with open ('file.txt', 'w') as file:
#     file.write('Hello, World')
#
# ##Дописать файл -'a'
# with open ('file.txt', 'a') as file:
#     file.write('\nThis is a new line')
#
# ##Прочитать файл -'r'
# with open ('file.txt', 'r') as file:
#     content = file.read()
#     print(content)



##Создать файл--'x'
# with open ('file1.txt', 'x') as file:
#     file.write('This is a new line')

##Запись и чтение--'w+'
# with open ('file.txt', 'w+') as file:
#     file.write('Hello Aida!\nThis is a new line.')
#     file.seek(0) ##Переместить курсор в начало файла
#     content = file.read()
#     print(content)


with open ('numbers.txt', 'w') as file:
    for i in range (5):
        numbers = int (input(('Number: ')))
        file.write(f'{numbers} \n')

numbers = []
with open ('numbers.txt', 'r') as file:
    for line in file:
        numbers.append(int (line.strip()))
    print(sum(numbers))