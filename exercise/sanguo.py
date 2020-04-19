import re


def find_item(name):
    with open("sanguo.txt", encoding="gb18030") as f:
        data = f.read().replace("\n", "")
        name_num = re.findall(name, data)
        print("name:%s appear num:%s" %(name, len(name_num)))
    return len(name_num)


# 读取人物名称
name_dict = {}


def find_name():
    with open("sanguo_name.txt") as f:
        for line in f:
            names = line.split("|")
            for n in names:
                name_num = find_item(n)
                name_dict[n] = name_num
    print(name_dict)


if __name__ == '__main__':
    find_name()