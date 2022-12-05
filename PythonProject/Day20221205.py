
try:
    print(10)
    print(name)
    print(20)
    1/0
except NameError as e:
    print("出异常啦！")
# except ZeroDivisionError as e:
#     print("出异常啦！")