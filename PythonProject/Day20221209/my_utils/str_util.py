def str_reverse(ori_str):
    '''
    功能：将输入的字符串ori_str实现反转后，return返回字符串
    :param ori_str:待反转的字符串
    :return:反转后的字符串
    '''
    # str_tmpList = []
    # i = -1
    # while((-1 - i) < len(ori_str)):
    #     str_tmpList.append(ori_str[i])
    #     i -= 1
    # result_str = str(str_tmpList)
    # print(result_str)
    return ori_str[::-1]

def substr(ori_str, cut_start, cut_end):
    '''
    功能：对字符串进行指定片段的切取
    :param ori_str: 待切取的原字符串
    :param cut_start: 切取字符串的起始位置（第一个字符的位置为1）
    :param cut_end: 切取字符串的起始位置（最后一个字符的位置数值上等于字符串的长度）
    :return:
    '''
    return ori_str[cut_start-1 : cut_end+1 : 1] # 步长1也可以省略不写


if __name__ == '__main__':          # 输入main后直接回车可以快捷形成该语句
    test_str = "Hello World!"
    print(str_reverse(test_str))
    print(substr(test_str, 1, 12))