def test_func(fun, num1, num2):
    result = fun(num1, num2)  # 写到这里才能确定fun是个函数名
    print(f"fun的类型是：{type(fun)}")
    print(f"计算结果：{result}")

def compute1(x, y):
    return x + y

def compute2(x, y):
    return x * y

def compute3(x, y):
    return x - y

test_func((lambda x, y : x + y), 7 ,8)
# test_func(compute1, 1, 2)
# test_func(compute2, 3, 4)
# test_func(compute3, 5 ,6)


# def test_func1(fun1):
#     result = fun1(1, 2)  # 写到这里才能确定fun是个函数名
#     print(f"fun1的类型是：{type(fun1)}")
#     print(f"计算结果：{result}")
#
# test_func1(lambda x, y : x + y, 1, 2)

#result = lambda x = 1, y = 2: x + y




