# Python100 - Day6

## 函数和模块


### 1.定义函数

在Python中使用def关键字来定义函数，在函数名后面的圆括号中可以放置传递给函数的参数（可以在最开始定义的时候设置变量的默认值）。函数的参数就相当于是自变量，而函数执行完成后可以通过return关键字来返回一个值，这相当于因变量。

	def add(a =0, b=0, c=0):
		return a+b+c
	
	print(add())
	print(add(1,2))
	print(add(1,2,3)) #需要按照设定的顺序进行传递
	print(add(a=10, c=30, b=20)) #传递参数可以不按照设定的顺序进行传递

倘若具体传递多少个参数由调用者决定，那么在不确定参数个数的时候，可以使用可变参数（*args）。

	# 在参数名前面的*表示args是一个可变参数
	# 即在调用add函数时可以传入0个或多个参数
	def add_new(*args):
	    tot = 0
	    for val in args:
	        tot += val
	    return tot
	print(add_new(1,2,3,4,5,6,7,8))


### 2.同名函数的管理

	def foo():
 	   print('hello, world!')
	def foo():
 	   print('goodbye, world!')
	foo() #返回goodbye,world，也就是说会覆盖掉第一个函数

**解决办法：**可以通过模块对同名函数进行管理，也就是把它们分别保存到不同的.py文件中，之后使用的时候import指定的模块来调用函数。

比如，把第一个foo()保存在模块module1.py，把第二个foo()保存在模块module2.py。
	
	import module1 as m1
	import module2 as m2
	m1.foo()
	m2.foo()

在导入某一模块的函数时，倘若该模块除了定义的函数之外还存在可以执行代码，但是我们不希望在导入的时候执行呀。

**解决办法：**将这些执行代码放在特殊的if条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”。

	def bar():
		pass
	if __name__ == '__main__':
    	print('call bar()')

	# __name__是Python中一个隐含的变量它代表了模块的名字
	# 只有被Python解释器直接执行的模块的名字才是__main__
	# 所以Import module的时候不满足条件，不会执行







