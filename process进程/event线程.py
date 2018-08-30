# encoding: utf-8
"""
@version:??
@author:df
"""


from multiprocessing import Process,current_process,Event
import time

def work_1(event_1):
    while True:
        event_1.wait()
        print('子进程11111前进', current_process().name, current_process().pid)
        time.sleep(1)
def work_2(event_2):
    while True:
        event_2.wait()
        print('子进程2222前进', current_process().name, current_process().pid)
        time.sleep(2)
def main():
    e = Event()
    ee = Event()
    p1 = Process(target=work_1,name='work1',args=(e,))
    p2 = Process(target=work_2,name='work2',args=(ee,))

    p1.start()
    p2.start()
    while True:
        print('立即执行')
        e.set()
        ee.set()
        time.sleep(10)
        print('立即结束')
        e.clear()
        ee.clear()
        time.sleep(10)

if __name__ == '__main__':
    main()