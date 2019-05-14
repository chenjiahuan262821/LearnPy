class Person(object):

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age
	
class Student(Person):		#从Person那里继承
	
	def __init__(self, name, age, grade):
		super().__init__(name, age)   #从Person那里继承对象的name和age属性
		self._grade = grade

	@property
	def grade(self):
		return self._grade
	
	def course(self, course):
		print('%s的%s课程获得%d分' % (self._name, course, self._grade))

class Teacher(Person):

	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title

	@property
	def title(self):
		return self._title
	
	def lesson(self, course):
		print('%s%s主讲课程%s' % (self._name, self._title, course))

def main():
	stu = Student('王一', 22, 90)
	stu.course('程序设计')
	t = Teacher('老王', 39, '教授')
	t.lesson('交易策略')

if __name__ == '__main__':
	main()