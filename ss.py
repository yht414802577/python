#coding=utf-8

class Person:
	def __init__(self,name,age,pay=0,job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def  lastname(self):
		return self.name.split()[-1]
	def giveRives(self,percent):
		self.pay *= (1.0 + percent)

	
		
		

if __name__ == '__main__':
	bob = Person('Bob Smith',42,3000,'software')
	sue = Person('Sue Jones',53,30000,'hardware')
	print(bob.name,sue.name)
	print(bob.lastname())
	print(sue.pay)
	sue.giveRives(.10)
	print(sue.pay)