##list_comprehension-
# n = int(input("5 ке болунгон сандар: "))
# res = []
# for i in range (1, n + 1):
#     if i % 5 == 0:
#         res.append(i)
# print(*res)                           #*-cписоктун ичине чыгарбайт
#
#
# n = int(input("5 ке болунгон сандар: "))
# res = []                              ##[] результатты списоктун ичине чыгарат
# for i in range (1, n + 1):
#     if i % 5 == 0:
#         res.append(i)
# print(res)


# n = int(input("5 ке болунгон сандар: "))
# # res = []
# # for i in range (1, n + 1):
# #     if i % 5 == 0:
# #         res.append(i)
# # print(*res)
# res = [i for i in range (1, n + 1)]
# print(*res)



# n = int(input("5 ке болунгон сандар: "))
# # res = []
# # for i in range (1, n + 1):
# #     if i % 5 == 0:
# #         res.append(i)
# # print(*res)
# res = [i ** 2 for i in range (1, n + 1)]    ##сандардын      #i ** 2 -append деп тушунсо болот
# print(res)


# n = int(input("5 ке болунгон сандар: "))
# # res = []
# # for i in range (1, n + 1):
# #     if i % 5 == 0:
# #         res.append(i)
# # print(*res)
# res = [f'{i} ** 2 = {i ** 2}' for i in range (1, n + 1)]    ##сандардын      #i ** 2 -append деп тушунсо болот
# print(res)

# n = int(input("Табица: "))
# # res = []
# # for i in range (1, 11):
# #     if i * 1 == 0:
# #         res.append(i)
# # print(*res)
# res = [f'{n} * {i} = {i * n}' for i in range (1, 11)]
# print(res)


# n = int(input("Табица: "))
# res = []
# for i in range (1, 11):
#     if i * 1 == 0:
#         res.append(i)
# print(*res)
# res = [f'{n} * {i} = {i * n}' for i in range (1, 11) if n < 10]
# print(res)


# res = [i for i in range (1, int (input()) +1) if i % 2 == 0]     #жуп сандарга болунгон свндвр
# print(res)

# res = [i for i in range (1, int (input()) +1) if i % 3 == 0 and i % 5 ==0]   ##3 ко жана 5 ке болнугон сандар
# print(res)










