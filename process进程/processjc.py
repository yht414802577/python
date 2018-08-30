# encoding: utf-8
"""
@version:??
@author:df
"""



import os , time
from multiprocessing import Process,current_process

res = os.fork()
if res == 0:
    time.sleep(5)

else:

    time.sleep(10)
