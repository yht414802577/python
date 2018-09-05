# encoding: utf-8
"""
@version:??
@author:df
"""

import os
from multiprocessing import Process
from threading import Thread

def action(arg1, arg2):
    print(arg1, arg2)

if __name__ == '__main__':
    Thread(target=(lambda: action(2,4))).start()
    p = Process(target=action,args=('spam', 'eggs'))
    p.daemon = True
    p.start()