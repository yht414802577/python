import _thread as thread , time
stdoutmutex = thread.allocate_lock()
numthread = 5
exitmutexes = [thread.allocate_lock() for i in range(10)]
def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1)
        with mutex:
            print('[%s] => %s' %(myId, i))
    exitmutexes[myId].acquire()

for i in range(numthread):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))
while not all(mutex.locked() for mutex in exitmutexes):
    time.sleep(0.25)

print('Main thread exiting')
