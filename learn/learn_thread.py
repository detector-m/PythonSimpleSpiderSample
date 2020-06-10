# *-* coding: utf-8 -*

'''
多线程
Python3 有三个多线程模块 _thread, threading, Queue
_thread没什么人用
'''

import threading
import time

def threading_action_01(para='test_01_thread_01', sleep=3):
    time.sleep(sleep)
    print(f'{para} 开始 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')

def test_threading_01(name, sleep=1, count=10):
    # 创建子线程
    thread_01 = threading.Thread(target=threading_action_01)
    thread_02 = threading.Thread(target=threading_action_01, args=['test_01_thread_02', 2])

    # 启动子线程
    thread_01.start()
    thread_02.start()

    while count:
        time.sleep(sleep)
        print(f'{name} 开始 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        count -= 1
    

'''
创建一个线程子类
'''
class TestThread(threading.Thread):
    def __init__(self, threadId, name, sleep=1):
        threading.Thread.__init__(self)
        self.threadId = threading
        self.name = name
        self.sleep = sleep
    
    def run(self):
        # 线程内容
        print('线程开始：{}'.format(self.name))
        self.threading_action_02(self.name, 2)
        print('线程结束：{}'.format(self.name))

    def threading_action_02(self, para='test_02_thread_01', sleep=1, count=10):
        while count:
            time.sleep(sleep)
            print(f'{para} 开始 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
            count -= 1

def test_threading_02(name, sleep=1, count=10):
    thread_01 = TestThread(1, 'thread_01')
    thread_02 = TestThread(2, 'thread_02', 3)
    thread_01.start()
    thread_02.start()
    
    while count:
        time.sleep(sleep)
        print(f'{name} 开始 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        count -= 1
    
    # 主线程等待子线程执行完毕 ->让子线程加入主线程等待
    thread_01.join()
    thread_02.join()

    print('退出主线程')

if __name__ == '__main__':
    # test_threading_01('test_threading_01')
    test_threading_02('test_threading_02')
