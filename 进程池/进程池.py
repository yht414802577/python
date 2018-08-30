# encoding: utf-8
"""
@version:??
@author:df
"""


from multiprocessing import Pool


def work_1():
    for i in range(200000000):
        pass
    print('1111111111')

def work_2():
    for i in range(200000):
        pass
    print('22222222222222')

def work_3():
    for i in range(400000):
        pass
    print('333333333333333')

def main():
    p = Pool(3)
    for i in range(4):
        p.apply_async(func=work_1)

    for i in range(5):
        p.apply(func=work_2)

    for i in range(6):
        p.apply_async(func=work_3)


    p.close()
    p.join()

if __name__ == '__main__':
    main()