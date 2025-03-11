##ternary-operator
# a = 20
# if a % 2 == 0:
#     print("Жуп")
# else:
#     print("Так")
#
# print("Jup" if a % 2 == 0 else "Tak")
#
# print("Jup" if int (input()) % 2 == 0 else "Tak")

# print(
#     ["Jup" if i % 2 == 0 else "Tak"
#      for i in range (int(input()) + 1)]
# )

print(
    ["Jup" if i % 2 == 0 else "Tak"
     for i in range (1, int(input()) + 1)]     ##так сандан башталат 1 коюлду
)

print(4 ** 0.5)      ##4ту тамырдан чыгарат