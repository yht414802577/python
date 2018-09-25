from itertools import cycle
#itertools Python标准库 专门用来创建迭代器的
import time 
mylist =  [1,2,3] #var中的数据 取决于 来源的有序对象
	#mylist:  列表 线性的方向
var = cycle(mylist) #无法动态改变的
print(dir(var))
for v in var:
	time.sleep(0.5)
	print(v)
mystr = 'abcdefg' #C语言 常量指针 无法修改
#序列类型会帮你多创建一些空间

chr mystr[7] = "abcdefg" 
#hash表
#红黑二叉树(链表) 遍历检索非常快 游戏 精灵

#双向链表 
	#门禁系统 队列 双向链表 在任意节点位置都可以 insert pop 
	#栈 先进后出 头部可以写入，头部可以弹出，屁股啥都不能看

#Python 模块 函数 学会调用就行了