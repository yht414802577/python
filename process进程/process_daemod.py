# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Process,current_process
import time

def work():
    for i in range(10):
        print('子进程', current_process().name, current_process().pid)
        time.sleep(100)

def work_1():

    print('子进程1', current_process().name, current_process().pid)
    time.sleep(3)
def main():
    print('父进程', current_process().name, current_process().pid)
    p1 = Process(target=work, name='1')
    p2 = Process(target=work_1, name='2')
    p1.daemon = True
    p1.start()
    p2.start()
    time.sleep(2)



if __name__ == '__main__':
    main()
