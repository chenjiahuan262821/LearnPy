class Person(object):

	__slots__ = ('_name', '_age', '_gender') #限定Person对象只能绑定_name, _age和_gender这三个属性

	def __init__(self, name, age, gender):
		self._name = name     # 属性命名以单下划线开头，通过这种方式来暗示属性是受保护的
		self._age = age       # 这个例子里，属性name和age是受保护的，不可随意改动
		self._gender = gender  # 属性gender是不受保护的，直接暴露出去，可以随便改

	# 访问器 - getter方法，只读-不允许修改
	@property
	def name(self):
		return self._name

	# 访问器 - getter方法，只读
	@property
	def age(self):
		return self._age

def main():
    person = Person('王大锤', 12, 1)

    person.grade = 90  #想随便加个属性，报错: 'Person' object has no attribute 'grade'   

if __name__ == '__main__':
    main()