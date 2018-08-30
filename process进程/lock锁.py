# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Process, current_process, Lock, Semaphore


def work_a():
    for var in range(10000):
        print('子进程A%s' %var, current_process().name, current_process().pid)

def work_b():
    for var in range(10000):
        print('子进程B%s' %var, current_process().name, current_process().pid)

def work_c():
    for var in range(10000):
        print('子进程C%s' %var, current_process().name, current_process().pid)

def main():
    pa = Process(target=work_a, name='work1')
    pb = Process(target=work_b, name='work2')
    pc = Process(target=work_c, name='work3')
    pa.start()
    pb.start()
    pc.start()

    pa.join()
    pb.join()
    pc.join()

if __name__ == '__main__':
    main()