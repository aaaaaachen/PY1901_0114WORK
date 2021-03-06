
#在子类中是不能继承私有属性和方法的，
#但是私有属性和方法可以在同一个类中被调用
class Person(object):
	def __init__(self,name):
		self.__name = name
		self._age = 12

	def greet(self):
		print('hello,my name is %s' % self.__name)

	def __run(self):
		print('base class is running')


	#但是私有属性和方法可以在同一个类中被调用
	def running(self):
		self.__run()

class Student(Person):

	def greet(self):
		# print('hell, my name is %s' % self.__name)
		print('hello my age is %d' % self._age)
		self.__run()

# p1 = Person('zhiliao')
# p1.greet()
# p1.running()
s1 = Student('zhiliao')
s1.__run()
# s1.greet()

# 本节课的重点：子类不能继承父类的私有属性