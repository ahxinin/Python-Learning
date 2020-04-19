file = open("name.txt", "w")
file.write("张三")
file.close()

file2 = open("name.txt", "r")
print(file2.readline())

file3 = open("sanguo.txt", encoding="gb18030")
print(file3.readlines())