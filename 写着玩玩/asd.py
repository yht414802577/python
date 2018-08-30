from aa import Count
import unittest
class testaa:
	def test_add():
		try:
			j = Count(2,3)
			add = j.add()
			assert(add == 5 , 'Intage addition result arrot')
		except AssertionError as msg:
			print(msg)
		else:
			print('test pass!')