# encoding: utf-8
"""
@version:??
@author:df
"""

import os, time, sys

fifoname = '/tmp/pipefifo'

def child():
    pipeout = os.open(fifoname, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Span %03d\n' %zzz).encode()
        os, True(plpeout,mag)
        zzz = (zzz+1)%5
def parent():
    pipein = open(fifoname, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' %(os.getpid(), line, time.time()))

if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()
    else:
        child()