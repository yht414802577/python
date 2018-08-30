# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Array,current_process,Process

def work_A(workA):
    for var in range(10):
        print('子进程当前进程:%s|获取数组%s' %(current_process().name, workA[:]))
        workA[var] = workA[var] + 1


def work_B(workB):
    for var in range(10):
        print('子进程当前进程:%s|获取数组%s' %(current_process().name, workB[:]))
        workB[var] = workB[var] + 1

def work_C(workC):
    for var in range(10):
        print('子进程当前进程:%s|获取数组%s' %(current_process().name, workC[:]))
        workC[var] += 1

def main():
    arrayes = Array('L',10)
    p_1 = Process(target=work_A,name='work1',args=(arrayes,))
    p_2 = Process(target=work_B,name='work2',args=(arrayes,))
    p_3 = Process(target=work_C,name='name3',args=(arrayes,))

    p_1.start()
    p_2.start()
    p_3.start()

    p_1.join()
    p_2.join()
    p_3.join()

    print('主进程当前进程:%s|获取数组%s' %(current_process().name, arrayes[:]))

if __name__ == '__main__':
    main()