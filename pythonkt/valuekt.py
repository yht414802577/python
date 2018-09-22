from multiprocessing import Value,Process,current_process
def work(v):
    print('zijingcheng ', current_process().name, current_process().pid, v.Value)
    v.Value = 123
    print('aaaaaaa',current_process().name,current_process().pid,v.Value)

def work_1(v):
    print('~~~~~~~~~~~~~~~',current_process().name,current_process().pid,v.Value)
    v.Value = 456
    print('_______________',current_process().name,current_process().pid,v.Value)

def main():
    v = Value('i', 0)
    p_a = Process(target=work,name='A',args=(v,))

    p_b = Process(target=work_1,name='B',args=(v,))


    p_a.start()
    p_b.start()

    p_a.join()
    p_b.join()


if __name__ == '__main__':
    main()

