# 迭代器
num_list = [1, 2 ,3]
it = iter(num_list)
print(next(it))


# 生成器
for i in range(0, 10, 2):
    print(i)


# 自定义生成器
def frange(start, end, step):
    x = start
    while(x < end):
        yield x
        x += step


for i in frange(10, 15, 0.5):
    print(i)


# 过滤函数
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x:x>2, nums))
print(result)

