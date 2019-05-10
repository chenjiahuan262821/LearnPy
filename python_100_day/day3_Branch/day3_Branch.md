# Python100 - Day3

## 分支结构与IF语句

在Python中构造分支结构，使用if、elif和else关键字，通过缩进的方式来设置代码的层次结构。


例子：

	#分段函数求值
        	3x - 5  (x > 1)
	f(x) =  x + 2   (-1 <= x <= 1)
        	5x + 3  (x < -1)


	x = float(input('请输入x值:'))
	if x>1 :
		y = 3*x-5
	elif x>-1 :
		y = x+2
	else :
		y = 5*x+3
	print('x值%.2f所对应的y值为%.2f' % (x,y))


	#掷骰子游戏

	from random import randint #random模块的randint函数生成指定范围的随机数
	face = randint(1, 6)
	if face == 1:
	    result = '唱首歌'
	elif face == 2:
    	result = '跳个舞'
	elif face == 3:
    	result = '学狗叫'
	elif face == 4:
    	result = '做俯卧撑'
	elif face == 5:
		result = '念绕口令'
	else:
    	result = '讲冷笑话'
	print(result)


