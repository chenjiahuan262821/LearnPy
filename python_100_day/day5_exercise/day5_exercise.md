# Python100 - Day5

---
通过这5题小练习，新掌握的技巧：

+ python应该尽量避免循环，在避免了循环的情况下要尽可能减少遍历数据量（e.g.涉及因子的问题应该想到平方根、通过等式关系减少循环）
+ map函数和reduce函数都能提升效率，今天这里只用了map，map函数返回的是可迭代对象，可以用list()的方法显示出来
+ python中通过random这个库产生随机数
+ 丢弃变量：_，如果不关心一个变量，就可以定义改变量的名字为_。for _ in range(20)就是循环20次的意思。
---


## 寻找“水仙花数”
仙花数（Narcissistic number）是指一个3位数，它的每位上的数字的3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

	for i in range(100, 999, 1):
		hund = i // 100
		tens = (i-hund*100) // 10
		unit = (i-hund*100-tens*10)
		number = int(str(hund)+str(tens)+str(unit))
		if hund**3 + tens**3 + unit**3 ==  number:
			print('we find the Narcissistic number:', number) 

返回的结果是：

	we find the Narcissistic number: 153
	we find the Narcissistic number: 370
	we find the Narcissistic number: 371
	we find the Narcissistic number: 407



## 寻找“完美数”
完全数（Perfect number），又称完美数或完备数，它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如，第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。

寻找10000（1万）以内的完美数


方案1：两个循环
	
	import time
	start = time.clock()
	for i in range(1, 10000):
		end = i-1
		sum = 0
		for j in range(1, end):
			if i % j == 0:
				sum += j
		if sum == i:
			print('we find the Perfect number:', i)
	end = time.clock()
	print("执行时间:", (end - start), "秒")  #执行时间: 9.0850145 秒

方案2：用map函数免去一个循环（上面两个循环太慢了）
	
	import time
	start = time.clock()
	def find_perfect(i):
		end = i-1
		sum = 0
		for j in range(1, end):
			if i % j == 0:
				sum += j
		if sum == i:
			print('we find the Perfect number:', i)

	l = map(find_perfect, range(1, 10000))
	list(l)
	end = time.clock()
	print("执行时间:", (end - start), "秒")  #执行时间: 3.7170397 秒


方案3：学习一下优化的代码

	import time
	import math

	start = time.clock()
	for num in range(1, 10000):
    	sum = 0
    	for factor in range(1, int(math.sqrt(num)) + 1):   
        	if num % factor == 0:
            	sum += factor
            	if factor > 1 and num / factor != factor:
            	    sum += num / factor          #这里一小块是精髓，减少了很多数据量
    	if sum == num:
        	print('we find the Perfect number:', num)
	end = time.clock()
	print("执行时间:", (end - start), "秒") #执行时间: 0.09769749999999888 秒


## “百钱百鸡”问题
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

假设公鸡数量是x，母鸡数量是y，小鸡数量是z，三者应该满足如下方程
	
	x + y + z = 100
	5 * x + 3 * y + 1/3 * z = 100
	0 <= x <= 20
	0 <= y <= 33
	0 <= z <= 100


俺的代码：

	for x in range(20):
		for y in range(33):
			for z in range(100):
				if (x + y + z == 100) & (5 * x + 3 * y + 1/3 * z == 100):
					print('公鸡数量为%d，母鸡数量为%d，小鸡数量为%d' % (x, y, z))

返回的结果是：

	公鸡数量为0，母鸡数量为25，小鸡数量为75
	公鸡数量为4，母鸡数量为18，小鸡数量为78
	公鸡数量为8，母鸡数量为11，小鸡数量为81
	公鸡数量为12，母鸡数量为4，小鸡数量为84

人家的代码（通过等式减少一层循环）：

	for x in range(0, 20):
    	for y in range(0, 33):
    	    z = 100 - x - y
    	    if 5 * x + 3 * y + z / 3 == 100:
    	        print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


## 生成“斐波拉切数列”

斐波那契数列（Fibonacci sequence），在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)。

生成20个斐波那契数列:

	fib = []
	fib.extend([1,1])
	for i in range(2, 20):
		num = fib[i-1] + fib[i-2]
		fib.append(num)
	print(fib)

返回的结果是：

	[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

优化的方案：

	a = 0
	b = 1
	for _ in range(20):
    	(a, b) = (b, a + b)
    	print(a, end=' ')


## Craps赌博游戏

玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。

我想知道玩十万次，赌徒赢几次，庄家赢几次（和原本的题目好像不太一样，anyway开心就好hhh）

	import random
	counter = 0
	gambler = 0
	maker = 0
	rounds = 100000

	while counter < rounds:
    	counter += 1
    	x = random.randint(1, 6)
    	y = random.randint(1, 6)
    	sum0 = x + y
    	if (sum0 == 7) | (sum0 == 11):
    	    gambler += 1  #The gambler wins the game
    	elif (sum0 == 2) | (sum0 == 3) | (sum0 == 12):
    	    maker += 1  #The maker wins the game
    	else:
    	    while True:
    	        x = random.randint(1, 6)
    	        y = random.randint(1, 6)
    	        new_sum = x + y
    	        if new_sum == sum0:
    	            gambler += 1  #The gambler wins the game
    	            break
    	        elif new_sum == 7:
    	            maker += 1  #The maker wins the game
    	            break
    	        else:
    	            continue
	print('In %d rounds, the gambler wins %d while the maker wins %d.' % (rounds, gambler, maker))
	if maker != 0:
    	odds = gambler/maker
    	print('The odd-ratio is %.4f' % odds)
	else:
    	print('This time the odd-ratio is infinite')

运行的3次，返回的结果是：

	In 100000 rounds, the gambler wins 49340 while the maker wins 50660.
	The odd-ratiois 0.9739
	>>> 
	In 100000 rounds, the gambler wins 49251 while the maker wins 50749.
	The odd-ratio is 0.9705
	>>> 
	In 100000 rounds, the gambler wins 49488 while the maker wins 50512.
	The odd-ratio is 0.9797
	>>> 
		
> 加油！