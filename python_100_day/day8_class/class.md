# Python100 - Day8 

## 面向对象编程基础

今天的主题听上去就十分抽象~

>关键词：对象（object）、类（class）、封装（encapsulation）、继承（inheritance)、多态（polymorphism）

### 1.类和对象

+ 类是对象的蓝图和模板，而对象是类的实例。
+ 一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类。
+ 把一大堆拥有共同特征的对象，包括静态特征（属性）和动态特征（行为）都抽取出来堆在一起，就可以定义出一个叫做“类”的东西。

### 2. 定义类class

在python中以class为关键字定义类，在类中通过之前学习过的函数，将对象的动态特征描述出来。

+ 首先，通过__init__这个特殊方法去将对象初始化，并绑定属性（这里是name、age和gender）。注：在最开始将属性绑定以后，在之后描述行为的时候也可以调用。
+ 在这之后，通过定义函数，去描述对象的行为（这里是study、love、dating）。
+ self代表着一个对象，在定义属性与描述动作的时候就要在括号里第一个参数的为位置填self。
+ 定义好一个类之后，可以通过：类的名称(属性)，来创建对象。
+ 调用属性或者相应动作的时候，self.property、self.function()。

定义类Student：

	class Student(object):
	
		def __init__(self, name, age, gender):
			self.name = name
			self.age = age
			self.gender = gender
	
		def study(self, course_name):
			print('%s正在学习%s' % (self.name, course_name))

		def love(self):
			if self.age >= 18:
				print('%s已经是大人了，谈恋爱是开启一项长期投资' % self.name)
			else:
				print('%s还是个小孩，谈恋爱会遭到家长限制' % self.name)

		def dating(self):
			if self.gender == '男':
				print('%s约会出门前只需1分钟梳头穿鞋，跟着女朋友吃就对了' % self.name)
			else:
				print('%s约会出门前需要两小时化妆更衣，负责吃就对了' % self.name)

创建对象：

	def main():
		
		stu1 = Student('小亮', 22, '男')
		stu1.study('php')
		stu1.love()
		stu1.dating()
		stu1.age
		print(stu1.age)
	
		stu2 = Student('小欢', 16, '女' )
		stu2.study('python')
		stu2.love()
		stu2.dating()
		print(stu2.age)
	
	if __name__ == '__main__':
		main()

### 3. 访问可见性

在Python中，属性和方法的访问权限只有两种，也就是公开的(public)和私有的(private)。命名时可以用两个下划线(__)作为开头将属性或方法设置为私有。

	class Test:

    	def __init__(self, foo):
    	    self.__foo = foo   #__foo属性是私有的
	
    	def __bar(self):    #__bar方法是私有的
    	    print(self.__foo)
    	    print('__bar')

	def main1():
    	test = Test('hello')
    	# AttributeError: 'Test' object has no attribute '__bar'
    	test.__bar()
    	# AttributeError: 'Test' object has no attribute '__foo'
    	print(test.__foo)

	if __name__ == "__main__":
    	main1()

尽管设置了私有，但是还是可以通过下划线加类的名称访问到。

	def main2():
    test = Test('hello')
    test._Test__bar()   #插入了：_Test
    print(test._Test__foo)   #插入了：_Test


	if __name__ == "__main__":
    	main2()
P.S. 没什么特殊的情况下还是不要设置私有了......

