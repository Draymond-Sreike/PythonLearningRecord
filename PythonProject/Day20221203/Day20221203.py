# test_File = open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221203/test.txt", 'r', encoding = "UTF-8")
# lines_data = test_File.readlines()
# str_itheima_overall_count = 0
#
# for line_data in lines_data:
#     str_itheima_line_cout = line_data.count("itheima")
#     print(f"本行字符串内容是{line_data}，有\"itheima\"共计：{str_itheima_line_cout}个")
#     str_itheima_overall_count += str_itheima_line_cout
# print(f"最后总共有\"itheima\"：{str_itheima_overall_count}个")
#
# test_File.close()

# with open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221203/test.txt", 'r', encoding = "UTF-8") as test_File:
#     lines_data = test_File.readlines()
#     str_itheima_overall_count = 0
#
#     for line_data in lines_data:
#         str_itheima_line_cout = line_data.count("itheima")
#         print(f"本行字符串内容是{line_data}，有\"itheima\"共计：{str_itheima_line_cout}个")
#         str_itheima_overall_count += str_itheima_line_cout
#     print(f"最后总共有\"itheima\"：{str_itheima_overall_count}个")

# with open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221203/test.txt", 'r', encoding = "UTF-8") as test_File:
#     str_itheima_overall_count = 0
#
#     for line_data in test_File:
#         str_itheima_line_cout = line_data.count("itheima")
#         print(f"本行字符串内容是{line_data}，有\"itheima\"共计：{str_itheima_line_cout}个")
#         str_itheima_overall_count += str_itheima_line_cout
#     print(f"最后总共有\"itheima\"：{str_itheima_overall_count}个")

open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221203/test.txt", 'w', encoding = "UTF-8")
