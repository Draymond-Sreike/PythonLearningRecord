# t1 = ("hello")
# print(f"t1的类型是{type(t1)},t1的内容是{t1}")
#
# t2 = ("hello", )
# print(f"t2的类型是{type(t2)},t2的内容是{t2}")

# t1 = ('周杰伦', 11, ["football", "music"])
# print(t1.index(11))
# print(t1[0])
# t1[2].remove("football")
# print(t1)
# t1[2].insert(0, "coding")
# print(t1)

# t1 = "我是 周杰伦"
# print(t1.index("周杰伦"))

# string = "itheima and itcast"
# newString = string.replace("it", "程序")
# print(newString)
# print(string)

# string = "itheima and itcast"
# newString = string.split()
# print(newString)

string = "itheima itcast boxuegu"
it_count = string.count("it")
print(it_count)
new_String = string.replace(" ", "|")
print(new_String)
string_List = new_String.split("|")
print(string_List)