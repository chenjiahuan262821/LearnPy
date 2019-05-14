# Python100 - Day9

## 面向对象编程进阶

### 1. @property装饰器

> 虽然不建议将属性设置为私有，但是如果直接将属性暴露给外界也存在问题的，比如没有办法检查赋给属性的值是否有效。

建议将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，并且使用@property包装器来包装getter（访问器）和setter（修改器）方法。

	class Person(object):
	
		def __init__(self, name, age, gender):
			self._name = name     # 属性命名以单下划线开头，通过这种方式来暗示属性是受保护的
			self._age = age       # 这个例子里，属性name和age是受保护的，不可随意改动
			self.gender = gender  # 属性gender是不受保护的，直接暴露出去，可以随便改

		# 访问器 - getter方法，只需 对象.name 就可以返回name的值，只有@property，所以：只读-不允许修改
		@property
		def name(self):
			return self._name

		# 访问器 - getter方法，只需 对象.age 就可以返回age的值，如果没有下面的@age.setter那也是只读
		@property
		def age(self):
			return self._age

		# 修改器 - setter方法，可以通过 对象.age = ... 命令去对age属性进行修改，所以：读写都可以
		# 通常可以与if函数结合，检查赋值是否有效
		@age.setter
		def age(self, age):
			if (age >= 0) & (age <= 130):
				self._age = age
			else:
				self._age = 'NaN'

		def play(self):
			if self._age <= 16:
				print('%s正在玩飞行棋.' %self._name)
			else:
				print('%s正在玩斗地主.' %self._name)

	def main():
    	person = Person('王大锤', 12, 1)

    	print(person._name)   # 返回：王大锤
    	print(person.name)	# 返回：王大锤，和上面一样，说明通过@property转化后不加下划线也可以访问
    	#person.name = '王泥马'  #AttributeError: can't set attribute，说明name这个对象是只读的
    
    	#上面name不能更改是因为命名的时候带有下划线，对比一下gender（没有下划线）
    	person.gender = 0 # 尝试去修改
    	print(person.gender)  #返回：0，说明不带下划线的gender可以随便被人改动

    	#下面我们来看一下可以读写操作的age
    	print(person.age)  #返回：12，说明通过@property转化后不加下划线也可以访问

    	person.age = 22	# 能够修改是因为@age.setter
    	print(person.age) #返回：22，说明通过@age.setter可以修改属性

    	person.age = 999	# 修改
    	print(person.age)  #返回：NaN，说明通过@age.setter检查了参数

		person.grade = 90  #随随便便给他加个属性
    	print(person.grade)   #返回：90，还真加上了嘿

	if __name__ == '__main__':
    	main()

### 2. __slots__限定

比如上面的grade，访问者随随便便就可以给对象加了一个属性，这样就不方便管理了。通过在类中定义__slots__变量，使得对象只能绑定某些属性。需要注意__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

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

### 3. 静态方法和类方法

此前在类中定义的方法都是对象方法（都是给对象发消息），但是写在类中的方法并不需要都是对象方法。

> 例如，定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。

可以通过静态方法（@staticmethod）、类方法（@classmethod）去给类绑定方法。注意类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象。

	from math import sqrt

	class Triangle(object):
	
		def __init__(self, a, b, c):
			self._a = a
			self._b = b
			self._c = c

		@staticmethod		#静态方法，说明接下来的这个方法是绑定在类上的
		def is_valid_static(a, b, c):
			return a + b > c and b + c > a and a + c > b #有效的话会返回True

		@classmethod		#类方法，第一个参数约定名为cls，代表当前类相关的信息
		def is_valid_class(cls, a, b, c):
			return a + b > c and b + c > a and a + c > b

		def perimeter(self):
			return self._a + self._b + self._c 
		def area(self):
			half = self.perimeter() / 2
			return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

	def main():
		a, b, c = 6, 10, 6
	
		if Triangle.is_valid_static(a, b, c):   #静态方法是在给类发消息的时候调用的
			t = Triangle(a, b, c)
			print(t.perimeter())
		else:
			print('无法构成三角形')
	
		if Triangle.is_valid_class(a, b, c):   #类方法是在给类发消息的时候调用的
			t = Triangle(a, b, c)
			print(t.area())
		else:
			print('无法构成三角形')

		#静态方法、类方法，都是绑定在类上的，但是对象也可以访问
		print(t.is_valid_static(5,3,4)) 
		print(t.is_valid_class(5,3,4)) 

	if __name__ == '__main__':
		main()

#### 4. 类之间的关系


+ is-a关系也叫继承或泛化，比如学生和人的关系。
+ has-a关系为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
+ use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。

**继承**

在已有类的基础上创建新类，其中一种做法是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力。

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
			self._grade = grade			  #Student类新增属性grade

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

**多态**

通过abc模块的ABCMeta元类和abstractmethod包装器，将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，当我们在main函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

	from abc import ABCMeta, abstractmethod

	class Pet(object, metaclass=ABCMeta):

		def __init__(self, nickname):
			self._nickname = nickname

		@abstractmethod
		def make_voice(self):
			pass


	class Dog(Pet):
		def make_voice(self):
			print('%s: 汪汪汪...' % self._nickname)

	class Cat(Pet):
		def make_voice(self):
			print('%s: 喵...喵...' % self._nickname)


	def main():
		pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
		for pet in pets:
			pet.make_voice()

	if __name__ == '__main__':
    	main()

	'''
	返回的结果：
	旺财: 汪汪汪...
	凯蒂: 喵...喵...
	大黄: 汪汪汪...
	'''