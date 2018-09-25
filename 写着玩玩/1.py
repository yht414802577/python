mylist = [1,2,3,4,5,6]
for var in mylist: #for循环会绑定你放到这里的数据原型
#一般删除操作不会影响这个原型
	print(var)
	#mylist = mylist[1:] #吧这个值从开头取出来
	#del mylist[0]
	#mylist = mylist.remove(var)
	#mylist = mylist.pop(0)
	mylist.append(var) #放到屁股后面
		#这个列表会越来越大 
	print(mylist)
#1次次的从这个列表取值
	#for循环 怎么能实现死循环?
	#for循环的执行次数是根据 数据的长度
	#for循环经常被称作有限循环

while True:
	#死循环
	break