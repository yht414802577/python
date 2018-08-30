#coding=utf-8
from ss import Person
class Manager(Person):
	def  giveRives(self,percent,bonus=0.1):
		self.pay *= (1.0+percent+bonus)
		

if __name__ == '__main__':
	tom = Manager('Tom Doe',42,3000,'software')
	print(tom.lastname())
	print(tom.pay)
	tom.giveRives(.10)
	print(tom.pay)