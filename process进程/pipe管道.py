# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Process, current_process, Pipe

import pickle


def work_1(a):
    msg = '11111111111'
    a.send(pickle.dumps(msg))

    ret = pickle.loads(a.recv())
    print('333', ret)

def work_2(b):

    rece = pickle.loads(b.recv())

    print('22', rece)
    msg = '4444444'
    b.send(pickle.dumps(msg))


def main():
    work1, work2 = Pipe()

    p1 = Process(target=work_1, name='1', args=(work1,))
    p2 = Process(target=work_2, name='2', args=(work2,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()