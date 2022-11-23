# my_list = [31, 31, 21, 25, 21, 23, 22, 20]
# my_list.append(31)
# print(my_list)
# my_list.extend([29, 33, 30])
# print(my_list)
# print(my_list.pop(0))
# print(my_list.pop(len(my_list)-1))
# print(my_list.index(31))

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"原列表{num_list}")
# index = 0
# even_list = []
#
# while index < len(num_list):
#     if num_list[index] % 2 == 0:
#         even_list.append(num_list.pop(index))
#     index += 1
#
# print(f"经修改后的原列表：\t\t\t{num_list}")
# print(f"从原列表中取出的偶数列表：\t{even_list}")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原列表{num_list}")
even_list = []

for element in num_list:
    if element % 2 == 0:
        even_list.append(element)

print(f"经修改后的原列表：\t\t\t{num_list}")
print(f"从原列表中取出的偶数列表：\t{even_list}")