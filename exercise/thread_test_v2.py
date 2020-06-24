import threading
from threading import currentThread


class Mythrad(threading.Thread):
    def run(self):
        print(currentThread().getName(), 'start')
        print('run')
        print(currentThread().getName(), 'end')


t = Mythrad()
t.start()
t.join()

print(currentThread().getName(), 'end')