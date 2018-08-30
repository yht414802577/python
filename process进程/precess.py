# encoding: utf-8
"""
@version:??
@author:df
"""


from multiprocessing import Process,current_process
import time

def work_1():
    for i in range(5):
        print('进程11111')
        time.sleep(5)

def work_2():
    for i in range(1000000000):
        print('进程222222')
        time.sleep(5)

def work_3():
    for i in range(5):
        print('aaaaaaaaaa')
        time.sleep(5)

def main():
    p1 = Process(target=work_1, name='1')
    p2 = Process(target=work_2, name='2')
    p3 = Process(target=work_3, name='3')
    p2.daemon


    p_list = [p1, p2, p3]
    for p in p_list:
        p.start()

        print('子进程', current_process().name, current_process().pid)

    print('主进程', current_process().name, current_process().pid)

if __name__ == '__main__':
    main()
