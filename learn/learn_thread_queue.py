# *-* coding: utf-8 -*

import threading
import time
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            # time.sleep(1)
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def test_fn():
    print(f'开始 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} \n')

def test_queue_pool():
    # 创建长度为5的队列
    queue = Queue(2)
    for i in range(queue.maxsize):
        task = CustomThread(queue)
        task.setDaemon(True)
        task.start()

    for i in range(20):
        queue.put(test_fn)

    queue.join()

if __name__ == '__main__':
    test_queue_pool()
