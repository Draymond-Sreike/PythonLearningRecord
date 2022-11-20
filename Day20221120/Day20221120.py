num = 100 # 全局变量

def func1():
    global num  # 说明num是全局变量（而且是前面已经定义的全局变量）
    num = 200   # 将全局变量修改为200,此时会修改上面的全局变量num
    # global num = 200 # 不能这样同时声明num为全局变量又赋值
    print(num)  # 输出200

func1()
print(num)  # 输出200