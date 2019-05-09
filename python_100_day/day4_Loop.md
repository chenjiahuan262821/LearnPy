# Python100 - Day4

## 循环结构

Python中两种循环结构，一种是for-in循环，一种是while循环。

如果明确的知道循环执行的次数或者是要对一个容器进行迭代，那么使用for循环；如果要构造不知道具体循环次数的循环结构，那么使用while循环。

### 1.for-in与其常用搭配range

range可用于产生序列，默认从0开始。range(101)可以产生一个0到100的整数序列；range(1, 100)可以产生一个1到99的整数序列；range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

	实现1~100之间的偶数求和

	方法1: for-in循环
	
	sum = 0 #初始化
	for i in range(2, 101, 2):
		sum += i
	print(sum)

	方法2：reduce函数

	sum = 0
	from functools import reduce #Python3使用reduce函数要先import了
	def total(a,b):
		return a+b
	sum = reduce(total, range(2,101,2)) # reduce(函数,list,起始值默认为0）
	print(sum)


P.S. 如果数据量很大的话，循环起来的时间也是蛮久的，在python里如果能不用循环就不用循环了吧~

循环结构是可以嵌套的，比如输出九九乘法口诀表：
	
	for i in range(1, 10):
		for j in range(1，i+1):
			print('%d * %d = %d' % (i, j, i*j), end='\t') #让它不换行，使得每一行的i是相同的
		print() #print是默认换行的，让它换行，换新的i

### 2.while循环

while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循环结束。可以使用break和continue干预循环，break可以终止它所在的那个循环，continue可以用来放弃本次循环后续的代码直接让循环进入下一轮。


	“猜数字”的小游戏

	设定1：计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字，猜了7次以上是笨猪猪
	
	import random 
	answer = random.randint(1,100)
	counter = 0
	while True: #这表示会一直循环下去，直到遇到break
		counter += 1
		number = int(input('请输入数字：'))
		if number < answer:
			print('你猜的数字偏小了，大一点')
		elif number > answer:
			print('你猜的数字偏大了，小一点')
		else:
			print('恭喜你，猜对了！')
			break
	print('你总共猜了%d次' % counter)
	if counter > 7:
		print('OMG，猜了这么多次呢，笨猪猪')


	设定2：计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，猜了7次后停止游戏，笨猪猪不能继续猜了

	import random 
	answer = random.randint(1,100)
	counter = 0
	while counter < 7:
		residual = 7-counter
		print('今天有7次输入机会，剩%d次' % residual）
		number = int(input('请输入数字:'))
		if number < answer:
			print('你猜的数字偏小了')
		elif number > answer:
			print('你猜的数字偏大了')
		else:
			print('恭喜你，猜对了！')
			break
		counter += 1
	print('今天你总共猜了%d次' % counter)
	if counter == 7:
		print('笨猪猪，你今天的输入机会用完啦')

### 小练习：

输入两个正整数，计算最大公约数和最小公倍数。

	x = int(input('x = '))
	y = int(input('y = '))
	if x > y:
	    x, y = y, x
	for factor in range(x, 0, -1):
	    if x % factor == 0 and y % factor == 0:
	        print('%d和%d的最大公约数是%d' % (x, y, factor))
	        print('%d和%d的最小公倍数是%d' % (x, y, x * y //factor))  #这个//是商取整数部份的意思
        	break