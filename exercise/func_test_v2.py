# 闭包
def counter(first=0):
    cnt = [first]
    def add():
        cnt[0] += 1
        return cnt[0]
    return add


num = counter(5)
print(num())


# 闭包 V2
# a*x + b = y
def line(a, b):
    def arg_y(x):
        return a*x + b
    return arg_y


l1 = line(3, 5)
print(l1(4))