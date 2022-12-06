# def fun1():
#     print("fun1 开始执行")
#     num = 1 / 0 # 异常发生位置
#     print("fun1 执行结束")
#
# def fun2():                 # 异常传递的第一个环节
#     print("fun2 开始执行")
#     try:
#         fun1()
#     except Exception as e:
#         print(f"fun2() 捕获到了异常！异常为：{fun1()}")
#     print("fun2 执行结束")
#
# def main():                 # 异常传递的第二个环节
#     print("main 开始执行")
#     try:
#         fun2()
#     except Exception as e:
#         print(f"main 捕获到了异常！异常为：{e}")
#     print("main 执行结束")
#
# # main()
# def func1():
#     print("func1开始执行")
#     try:
#         num = 1 / 0
#     except Exception as e:
#         print(f"出现异常啦！异常的类型是：{1 / 0}")
#     print("func1执行结束")
#
# func1()

from time import *
sleep(3)

