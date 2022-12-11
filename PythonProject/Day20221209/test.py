import my_utils.str_util            # 使用两种不同的导包形式
from my_utils import file_util      # 使用两种不同的导包形式，这种形式可以不用写包名

print(my_utils.str_util.str_reverse("我喜欢邱丽婷！"))
print(my_utils.str_util.substr("我喜欢邱丽婷！", 4, 6))


# my_utils.file_util.print_file_info("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221209/test.txt")
file_util.print_file_info("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221209/test.txt")
'''即from导入时可以省略部分前缀'''
from my_utils.file_util import append_to_file
append_to_file("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221209/test.txt", "我喜欢邱丽婷0\n")
file_util.print_file_info("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221209/test.txt")
