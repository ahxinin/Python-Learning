file = open("name.txt", "w")
file.write("张三")
file.close()

file2 = open("name.txt", "r")
print(file2.readline())