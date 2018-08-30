# encoding: utf-8
"""
@version:??
@author:df
"""

import threading,queue,time


numconsumers = 2
numproducers = 4
nummessages = 4
safeprint = threading._allocate_lock()
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
        thread = threading.Thread(target=consumer,args=(i, dataqQueue))
        thread.daemon = True
        thread.start()

    waitfor = []

    for i in range(numproducers):
        thread = threading.Thread(target=produce,args=(i, dataqQueue))
        waitfor.append(thread)
        thread.start()

    for thread in waitfor:
        thread.join()

    print('Main thread exit.')