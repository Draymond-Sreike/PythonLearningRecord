def print_file_info(file_name):
    '''
    功能：将文件路径的文件内容全部输出至控制台
    :param file_name: 输入文件路径
    :return: None
    '''
    f = None
    try:
        # 非可能出现异常的的代码也写在try里
        f = open(file_name, 'r', encoding="UTF-8")
        print("文件内容如下：")
        print(f.read())
    except Exception as e:
        print(f"print_file_info函数打开文件时出现异常，异常原因是：{e}")
    finally:
        if f:   # 只有文件正常打开才会执行关闭，否则如果文件打开出现异常则f仍为None，不能执行f.close()，否则会异常
            f.close()

def append_to_file(file_name, data):
    '''
    功能：在指定文件路径的文件中追加数据
    :param file_name: 输入文件路径
    :param data: 要追加到文件的数据
    :return: None
    '''
    f = open(file_name, 'a', encoding="UTF-8")
    f.write(data)
    print("数据写入成功！")
    f.close()
    print("文件关闭成功！")

if __name__ == '__main__':
    # print_file_info("C:/Users/win10/Desktop/快捷操作.txt")
    append_to_file("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221209/test.txt", "我喜欢邱丽婷！\n")