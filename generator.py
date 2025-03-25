"""
[выражение for элемент in  список if  условие]
выражение -что делать  с каждым элементов
for  элемент in  список-перебор элементов по отдельности
if  условие -(необязательно) условие, фильтр для элементов
"""

# numbers = [x for x in range(5)]
# print(numbers)
#
# numbers = [x+2 for x in range(5)]
# print(numbers)
#
even_numbers=[x for x in range(10) if x %2 ==0]
print(even_numbers)
#
# words = ['apple', 'orange', 'cherry']
# short_words = [word.upper() for word in words]
# print(short_words)
#
# numbers = tuple(x for x in range(100))
# print(numbers)

even_numbers=[x for x in range(10) if x % 2 == 1]
print(even_numbers)

words = ["cat", "elephant", "dog", "giraffe"]
lengths = [len(word) for word in words]
print(lengths)

words = ["cat", "elephant", "dog", "giraffe"]
a = [x for x in words if len(x) % 2 == 0]
print(a)


