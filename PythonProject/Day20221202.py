txt_file = open("C:/Users/win10/Desktop/快捷操作.txt", "r", encoding="UTF-8")
# print(type(txt_file))
print(f"{txt_file.read(5)}")
print(f"{txt_file.readlines()}")