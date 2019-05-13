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

	if __name__ == '__main__':
    	main()

