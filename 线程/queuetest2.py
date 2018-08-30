# encoding: utf-8
"""
@version:??
@author:df
"""

import _thread,queue,time

numconsumers = 2
numproducers = 4
nummessages = 4
safeprint = _thread.allocate_lock()
dataqQueue = queue.Queue()
def produce(idnum, dataqQueue):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqQueue.put('[producer id=%d,count=%d]'%(idnum, msgnum))

def consumer(idnum, dataqQueue):
    while True:
        time.sleep(0.1)
        try:
            data = dataqQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
    for i in range(numconsumers):
        _thread.start_new_thread(consumer, (i, dataqQueue))
    for i in range(numproducers):
        _thread.start_new_thread(produce, (i, dataqQueue))
    time.sleep(((numproducers - 1) * nummessages) + 1)
    print('Main thread exit.')