# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Queue, current_process, Process



def work_1(q_put):
    for var in range(200):
        res = q_put.put(var)
        print('放入',res, current_process().name, current_process().pid, var )


def work_2(q_get):
    back = 0
    while True:
        if back > 100:
            break

        ret = q_get.get(block=False)
        print('进程1111取出', ret, current_process().name, current_process().pid, )

        back = back + 1


def work_3(q_get):
    back = 0
    while True:
        if back > 100:
            break
        try:
            ret = q_get.get(block=False)
            print('进程2222取出', ret, current_process().name, current_process().pid, )
        except:
            back = back + 1
            pass
        else:
            back = back + 1



def work_4(q_get):
    back = 0
    while True:
        if back > 100:
            break
        try:
            ret = q_get.get(block=False)
            print('进程3333取出', ret, current_process().name, current_process().pid, )
        except:
            back = back + 1
            pass
        else:
            print('跳过进程3333取出')
            back = back + 1


def work_5(q_get):
    back = 0
    while True:
        if back > 100:
            break
        try:
            ret = q_get.get_nowait()
            print('进程4444取出', ret, current_process().name, current_process().pid, )
        except:
            back = back + 1
            pass
        else:
            print('跳过进程4444取出')
            back = back + 1


def work_6(q_get):
    back = 0
    while True:
        if back > 100:
            break
        try:
            ret = q_get.get_nowait()
            print('进程5555取出', ret, current_process().name, current_process().pid, )
        except:
            back = back + 1
            pass
        else:
            print('跳过进程5555取出')
            back = back + 1



def main():
    q = Queue(4)

    put_1 = Process(target=work_1,name='put_1',args=(q,))
    get_1 = Process(target=work_2,name='get_1',args=(q,))
    get_2 = Process(target=work_3,name='get_2',args=(q,))
    get_3 = Process(target=work_4, name='get_3', args=(q,))
    get_4 = Process(target=work_5, name='get_4', args=(q,))
    get_5 = Process(target=work_6, name='get_5', args=(q,))
    get_1.daemon

    put_1.start()
    get_1.start()
    get_2.start()
    get_3.start()
    get_4.start()
    get_5.start()

    put_1.join()
    get_1.join()
    get_2.join()
    get_3.join()
    get_4.join()
    get_5.join()




if __name__ == '__main__':
    main()