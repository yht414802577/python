# encoding: utf-8
"""
@version:??
@author:df
"""


from multiprocessing import Queue,current_process,Process


def work_1(q):
    ret = q.get()
    print('``````````',current_process().name, current_process().pid, ret)


def work_2(q):
    ret = q.put('1')
    print('222222222222', current_process().name, current_process().pid, ret)

def main():
    q = Queue()
    q_1 = Process(target=work_1,name='1',args=(q,))
    q_2 = Process(target=work_2,name='2',args=(q,))

    q_1.start()
    q_2.start()
    q_1.join()
    q_2.join()


if __name__ == '__main__':
    main()
