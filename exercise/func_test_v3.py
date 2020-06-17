import time


# 装饰器
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("cast time:", end - start)
    return wrapper

@timer
def sleep():
    time.sleep(5)


sleep()