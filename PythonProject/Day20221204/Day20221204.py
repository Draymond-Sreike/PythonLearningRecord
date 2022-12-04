org_data = open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221204/QQ202212041708_OCR/result.txt", 'r', encoding = "UTF-8")
bar_data = open("D:/大学/PythonLearning/PythonLearningRecord/PythonProject/Day20221204/QQ202212041708_OCR/result.txt.bar", 'w', encoding = "UTF-8")

for data_line in org_data:
    # print(data_line)

    if data_line.count("测试") == 1:
        # print(data_line)
        continue

    bar_data.write(data_line)

org_data.close()
bar_data.close()