import _thread , time

mutex = _thread.allocate_lock()
def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print('[%s] => %s' %(myId, i))
        mutex.release()
        print('~~~~~~~~~~~~~~~~~~~')
        print(i)

for i in range(5):
    _thread.start_new_thread(counter, (i, 5))
    _thread.start_new_thread(counter, (i, 7))


time.sleep(6)
print('Main thread exiting.')