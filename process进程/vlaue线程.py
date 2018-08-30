# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Process,Value,current_process

def work1(v):
    print('111111111', current_process().name, current_process().pid, v.value)
    v.value = 123
    print('2222222222', current_process().name, current_process().pid, v.value)

def work2(v):
    print('111111111', current_process().name, current_process().pid, v.value)
    v.value = 45678
    print('2222222222', current_process().name, current_process().pid, v.value)

def main():
    v = Value('i',0)
    p1 = Process(target=work1,name='name1',args=(v,))
    p2 = Process(target=work2,name='name2',args=(v,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('主进程', current_process().name, current_process().pid, v.value)

if __name__ == '__main__':
    main()