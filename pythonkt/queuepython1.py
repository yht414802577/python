from multiprocessing import Process, current_process 
import time

def dunc():

    print('zijingcheng',current_process().name, current_process().pid)

def work():
    print('fuzijincheng ', current_process().name, current_process().pid)

def main():
    p1 = Process(target=dunc, name='hhh')
    p2 = Process(target=work, name='aaaa')
    p3 = Process(target=dunc,name='1111')
    p_list = [p1, p2, p3]
    for p in p_list:
        p.start()

    print('jincheng', current_process().name, current_process().pid)
if __name__ == '__main__':
    main()

