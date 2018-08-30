# encoding: utf-8
"""
@version:??
@author:df
"""

import os
from multiprocessing import Process, Lock

def whoami(label, lock):
    msg = '%s: name:%s,pid:%s'
    with lock:
        print(msg % (label, __name__, os.getpid()))

if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)

    p = Process(target=whoami, args=('spaured child',lock))
    p.start()
    p.join()

    for i in range(5):
        Process(target=whoami,args=(('run process %s' % i), lock)).start()

    with lock:
        print('Main proccess exit.')