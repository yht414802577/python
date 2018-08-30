# encoding: utf-8
"""
@version:??
@author:df
"""


from multiprocessing import Process, current_process, Pipe
import pickle

def work_1(sends):
    for var in range(100):
        rev = sends.send(pickle.dumps(var))
        print('发送 %s 数据', var, current_process().name, current_process().pid, rev)


def work_2(loads1):
    back = 0
    while True:

        if back > 10:
            break
        rev = pickle.loads(loads1.recv())
        print('1111接受  数据', rev, current_process().name, current_process().pid)
        back = back + 1


def main():
    pipe_send,pipe_load = Pipe(4)
    p_send = Process(target=work_1,name='send',args=(pipe_send,))
    p_loads = []
    for var in range(10):
        p_loads.append(Process(target=work_2,name='load%d' % var,args=(pipe_load,)))

    p_send.start()
    for p_load in p_loads:
        p_load.start()

    p_send.join()
    for p_load in p_loads:
        p_load.join()

if __name__ == '__main__':
    main()