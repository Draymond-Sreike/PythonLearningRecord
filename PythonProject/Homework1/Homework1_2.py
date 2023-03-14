'''
    题目：自编货币转换程序
    作者：21级电子信息工程信2班 梁深南
    学号：202134310214
'''
while True:
    print("本程序可提供的转换的币种有：人民币(¥/￥)、美元($/＄)、欧元(€)")
    CurrencyStr = input("请输入带币种符号的金额>:")
    CurrencySign = CurrencyStr[-1]                                                # 获取用户输入的金额字符串的最后一位，即币种符号

    while CurrencySign not in ['¥', '￥', '$', '＄', '€']:                        # 若用户输入有误，则循环直至输入正确为止
        CurrencyStr = input("您的输入有误!请重新输入带币种符号的金额>:")
        CurrencySign = CurrencyStr[-1]

    # print(CurrencyStr[-1]) # 测试
    if CurrencySign in ['¥', '￥']:                                              # 若用户输入的是人民币
        CurrencyValue_F = eval(CurrencyStr[0:-1])                                # 获取人民币数值
        print(f"您输入的是人民币：{CurrencyValue_F}¥")

        ExchangeCurrencyStr = input("您想要兑换的币种是？[人民币(¥/￥)、美元($/＄)、欧元(€)]输入币种符号>:")
        ExchangeCurrencySign = ExchangeCurrencyStr[-1]
        while ExchangeCurrencyStr not in ['¥', '￥', '$', '＄', '€']:             # 若用户输入有误，则循环直至输入正确为止
            ExchangeCurrencyStr = input("您的输入有误!请重新输入带币种符号的金额>:")
            ExchangeCurrencySign = ExchangeCurrencyStr[-1]

        if ExchangeCurrencySign in ['¥', '￥']:                  # 若用户要兑换人民币
            print(f"人民币：{CurrencyValue_F}¥，兑换为人民币后的币值为：{CurrencyValue_F}¥")
        elif ExchangeCurrencySign in ['$','＄']:                 # 若用户要兑换美元
            print("您要兑换的是美元，截至2023年3月13日：1¥ = 0.15$")
            print(f"人民币：{CurrencyValue_F}¥，兑换为美元后的币值为：{CurrencyValue_F * 0.15}$")
        else:                                                    # 若用户要兑换欧元
            print("您要兑换的是欧元，截至2023年3月13日：1¥ = 0.14€")
            print(f"人民币：{CurrencyValue_F}¥，兑换为欧元后的币值为：{CurrencyValue_F * 0.14}€")

    elif CurrencySign in ['$', '＄']:                                           # 若用户输入的是美元
        CurrencyValue_F = eval(CurrencyStr[0:-1])                               # 获取美元数值
        print(f"您输入的是美元：{CurrencyValue_F}$")

        ExchangeCurrencyStr = input("您想要兑换的币种是？[人民币(¥/￥)、美元($/＄)、欧元(€)]输入币种符号>:")
        ExchangeCurrencySign = ExchangeCurrencyStr[-1]
        while ExchangeCurrencyStr not in ['¥', '￥', '$', '＄', '€']:             # 若用户输入有误，则循环直至输入正确为止
            ExchangeCurrencyStr = input("您的输入有误!请重新输入带币种符号的金额>:")
            ExchangeCurrencySign = ExchangeCurrencyStr[-1]

        if ExchangeCurrencySign in ['¥', '￥']:                  # 若用户要兑换人民币
            print("您要兑换的是人民币，截至2023年3月13日：1$ = 6.84¥")
            print(f"美元：{CurrencyValue_F}$，兑换为人民币后的币值为：{CurrencyValue_F * 6.84}¥")
        elif ExchangeCurrencySign in ['$','＄']:                 # 若用户要兑换美元
            print(f"美元：{CurrencyValue_F}$，兑换为美元后的币值为：{CurrencyValue_F}$")
        else:                                                   # 若用户要兑换欧元
            print("您要兑换的是欧元，截至2023年3月13日：1$ = 0.93€")
            print(f"美元：{CurrencyValue_F}$，兑换为欧元后的币值为：{CurrencyValue_F * 0.93}€")

    else:                                                                       # 若用户输入的是欧元
        CurrencyValue_F = eval(CurrencyStr[0:-1])                               # 获取欧元数值
        print(f"您输入的是欧元：{CurrencyValue_F}€")

        ExchangeCurrencyStr = input("您想要兑换的币种是？[人民币(¥/￥)、美元($/＄)、欧元(€)]输入币种符号>:")
        ExchangeCurrencySign = ExchangeCurrencyStr[-1]
        while ExchangeCurrencyStr not in ['¥', '￥', '$', '＄', '€']:            # 若用户输入有误，则循环直至输入正确为止
            ExchangeCurrencyStr = input("您的输入有误!请重新输入带币种符号的金额>:")
            ExchangeCurrencySign = ExchangeCurrencyStr[-1]

        if ExchangeCurrencySign == '€':                         # 若用户要兑换欧元
            print(f"欧元：{CurrencyValue_F}€，兑换为欧元后的币值为：{CurrencyValue_F}€")
        elif ExchangeCurrencySign in ['$','＄']:                # 若用户要兑换美元
            print("您要兑换的是美元，截至2023年3月13日：1€ = 1.07$")
            print(f"欧元：{CurrencyValue_F}€，兑换为美元后的币值为：{CurrencyValue_F * 1.07}$")
        else:                                                   # 若用户要兑换人民币
            print("您要兑换的是人民币，截至2023年3月13日：1€ = 7.33¥")
            print(f"欧元：{CurrencyValue_F}¥，兑换为欧元后的币值为：{CurrencyValue_F * 7.33}¥")

    Continue_Flag = input("本次货币转换结束，请问是否需要继续进行货币转换？(Y/N)>:")    # 判断用户是否需要继续进行货币转换
    while Continue_Flag not in ['Y', 'N']:                                      # 用户输入错误时提示用户，并规范用户输入直至正确为止
        Continue_Flag = input("您的输入有误!请重新输入(Y/N)>:")

    if Continue_Flag == "Y":    # 若用户需要继续进行货币转换则重新执行上述温度转换代码
        continue
    else:                       # 若用户不需要继续进行货币转换则退出循环，结束程序
        break