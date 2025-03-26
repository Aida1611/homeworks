words = ["cat", "elephant", "dog", "giraffe"]
a = [x for x in words if len(x) % 2 == 0]
print(a)

list_comprehension = ["алма", "анар", "жузум", "алмурут", "хурма"]
filtered_list_comprehension = list(filter(lambda x: x[0] == 'а', list_comprehension))
print(filtered_list_comprehension)


list_comprehension = ["Anna", "Rita", "Calicha", "Aida", "Kudaibergen"]
filtered_list_comprehension = [name for name in list_comprehension if name.lower()[0]=='a']
print(filtered_list_comprehension)