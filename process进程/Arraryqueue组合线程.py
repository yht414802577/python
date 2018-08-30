# encoding: utf-8
"""
@version:??
@author:df
"""
from multiprocessing import Process,current_process,Array

def work_A():

def work_B():

def work_C():

def work_D():

def main():
    human = Array('i',5)
    p_1 = Process(target=work_A,name='name1',args=(human,))
    p_2 = Process(target=work_B,name='work2',args=(human,))
    p_3 = Process(target=work_C,name='name3',args=(human,))
    p_4 = Process(target=work_D,name='work4',args=(human,))

    p_1.start()
    p_2.start()
    p_3.start()
    p_4.start()

    p_1.join()
    p_2.join()
    p_3.join()
    p_4.join()

if __name__ == '__main__':
    main()