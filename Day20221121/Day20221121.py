my_list = ['梁深南', 19, True]  # 列表元素的类型可以不唯一
print(my_list)
print(type(my_list))

# 列表中的元素可以是列表，即可嵌套
my_list1 = [['梁深南', 19, True],"明天有课"]
print(my_list1)
print(type(my_list1))
my_list2 = [my_list1, "明天真的有课！！！"]
print(my_list2)
print(type(my_list2))