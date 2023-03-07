'''
    题目：自编温度转换程序
    作者：21电信2 梁深南
    学号：202134310214
'''
while True:
    # print("欢迎使用本温度转换程序！本程序作者：21电信2 梁深南，请尊重原作，切勿抄袭！")

    TemperatureStr = input("请输入带符号的温度值>:")
    TemperatureSign = TemperatureStr[-1]                            # 获取用户输入的温度字符串的最后一位，即温度符号

    while TemperatureSign not in ['F', 'f', 'C', 'c']:              # 若用户输入有误，则循环直至输入正确为止
        TemperatureStr = input("您的输入有误!请重新输入带符号的温度值>:")
        TemperatureSign = TemperatureStr[-1]
    #    if TemperatureSign in ['F', 'f', 'C', 'c']:
    #        break

    # print(TemperatureStr[-1]) # 测试
    if TemperatureSign in ['F', 'f']:                               # 若用户输入的是华氏度
        TemperatureValue_F = eval(TemperatureStr[0:-1])             # 获取华氏度数值
        print(f"您输入的是华氏度：{TemperatureValue_F}°F")
        TemperatureValue_C = (TemperatureValue_F - 32) / 1.8        # 将华氏度转化为摄氏度
        print("转化为摄氏度：{:.2f}°C".format(TemperatureValue_C))
    else:                                                           # 若用户输入的是摄氏度
        TemperatureValue_C = eval(TemperatureStr[0:-1])             # 获取摄氏度数值
        print(f"您输入的是摄氏度：{TemperatureValue_C}°C")
        TemperatureValue_F = TemperatureValue_C * 1.8 + 32          # 将摄氏度转化为摄氏度
        print("转化为华氏度：{:.2f}°F".format(TemperatureValue_F))

    Continue_Flag = input("本次温度转换结束，请问是否需要继续进行温度转换？(Y/N)>:")    # 判断用户是否需要继续进行温度转换
    while Continue_Flag not in ['Y', 'N']:                                     # 用户输入错误时提示用户，并规范用户输入直至正确为止
        Continue_Flag = input("您的输入有误!请重新输入(Y/N)>:")

    if Continue_Flag == "Y":    # 若用户需要继续进行温度转换则重新执行上述温度转换代码
        continue
    else:                       # 若用户不需要继续进行温度转换则退出循环，结束程序
        break