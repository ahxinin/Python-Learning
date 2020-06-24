import threading
import time
from threading import currentThread

def my_thread(arg):
    print(currentThread().getName(), "start")
    print("arg:  %s" % arg)
    time.sleep(2)
    print(currentThread().getName(), 'end')


for i in range(1, 11, 2):
    # my_thread(i)
    t = threading.Thread(target=my_thread, args={i})
    t.start()