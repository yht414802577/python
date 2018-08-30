# encoding: utf-8
"""
@version:??
@author:df
"""

from multiprocessing import Process,Array
import time
def func(m,n):
    for var in range(n):
        m[var] = var
        print(m[:])

def main():
    m = Array('i',7)
    p = Process(target=func,name='func1',args=(m,5))
    p.start()
    time.sleep(1)
    for i in m:
        print(i)
    p.join()

if __name__ == '__main__':
    main()