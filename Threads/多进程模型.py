import time
from multiprocessing import Process
def func_1():
    print('这是第一件事')
    mysum = 0
    for var in range(10000000):
        mysum += var
def func_2():
    print('这是第二件事情')
    mysum = 1
    for var in range(1,1000000):
        mysum = mysum - var
def func_3():
    print('这是第三件事情')
    mysum = 1
    for var in range(10000000):
        pass #过滤一遍
# start = time.time()
# func_1()
# func_2()
# func_3()
# end = time.time()
# print('%.2f' % (end -start))
#1.02
def main():
    p1 = Process(target=func_1)
    p2 = Process(target=func_2)
    p3 = Process(target=func_3)
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print('%.2f' % (end -start))
    #0.23
if __name__ == '__main__':
    main()
#抗洪:
    #同步 #大家排起队来，有序执行
    #异步/并发 #谁能扔谁扔，资源谁抢到算谁的
        #效率高