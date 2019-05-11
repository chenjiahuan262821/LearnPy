# Python100 - Day7

## 字符串与常用的数据结构（列表、元组、集合、字典）

### 1. 字符串的操作

计算字符串的长度len()、使字符串首字母大写capitalize()、使字符串全部字母大写upper()、查找子串所在的位置find()、检查字符串是否以指定的字符串开头或结尾startswith()与endswith()、字符串的切片[:]、检查是否由数字构成isdigit()、检查是否由字母构成isalpha()、检查是否由数字和字母共同构成isalnum()、修剪左右两侧空格strip()

	str1 = 'hello, world!'
	str2 = 'abcdef123456'
	str3 = '  joyce@163.com '

	print(len(str1))  # 13
	print(str1.capitalize())  # Hello, World!
	print(str1.upper())  # HELLO WORLD!
	print(str1.find('or'))  # 8
	print(str1.find('hi'))  # -1，找不到就返回-1
	print(str1.startswith('He')) # False
	print(str1.startswith('hel'))  # True
	print(str1.endswith('!')) # True

	print(str2[1]) # 注意python从0开始，所以b
	print(str2[1:6]) # bcdef
	print(str2.isdigit()) # False
	print(str2.isalpha()) # False
	print(str2.isalnum()) # True
	
	print(str3.strip()) # 修剪左右两侧空格，joyce@163.com

### 2. 列表list的操作

计算列表的长度即所含元素的个数len()、列表的下标索引[]、通过下标索引修改元素值、删除元素remove(具体元素的值)或者del后跟列表索引、清空列表clear()、切片操作与赋值[]、排序操作sort与sorted、生成式语法创建列表

	list1 = [1, 3, 5, 7, 100]
	list2 = ['hello'] * 5   # ['hello', 'hello', 'hello', 'hello', 'hello']
	print(len(list2)) # 计算长度，5
	print(list1[1]) # 索引，3
	print(list1[-2]) # 索引，7
	list1[3] = 6  # 修改，print(list1) 返回[1, 3, 5, 6, 100]
	list1.remove(3)
	if 100 in list1:
		list1.remove(100)
	print(list1) # remove的括号中填具体数值，[1, 5, 6]
	del list1[1]
	print(list1) # del后面跟列表索引，[1, 6]
	list2.clear()  # print(list2) 返回[]

	# 切片操作
	fruits = ['strawberry', 'waxberry']
	fruits.append('pear') # print(fruits) 返回['strawberry', 'waxberry', 'pear']
	fruits.extend(['pitaya', 'mango']) # print(fruits) 返回['strawberry', 'waxberry', 'pear', 'pitaya', 'mango']
	print(fruits) # ['strawberry', 'waxberry', 'pear', 'pitaya', 'mango']
	fruits2 = fruits[1:4] # print(fruits2) 返回['strawberry', 'waxberry']
	fruits4 = fruits[::-1] # 可以通过反向切片操作来获得倒转后的列表的拷贝，['mango', 'pitaya', 'pear', 'waxberry', 'strawberry']

	# 排序操作
	list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
	list2 = sorted(list1)
	list3 = sorted(list1, reverse=True)
	list4 = sorted(list1, key=len)
	print(list2) # 按字母顺序 ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
	print(list3) # 按字母逆序 ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
	print(list4) # 按照字母长度 ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

	list1.sort(reverse=True) # 直接作用在list1，对list产生了更改
	print(list1) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

	# 生成式语法创建列表
	f = [x for x in range(1, 10)]
	print(f) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

### 3. 元组tuple的操作
	
	t = ('亮亮', 22, 'bf', '上海') #创建元组
	bf = list(t) #将元组转换成列表
	p = tuple(bf) #将列表转换成元组

元组中的元素是无法修改的，一个不变的对象要比可变的对象更加容易维护。如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。

### 4. 集合set的操作

通过{}或者set()来创建集合、通过add()或者update([])来添加元素、通过discard()来删除元素、交集&、并集|、差集-、子集的判断<=。

	set1 = {1, 2, 3, 3, 3, 2} #通过{}创建集合
	set2 = set(range(1, 10)) #通过set()创建集合，将列表或元组转换成集合
	print(set1)  # {1, 2, 3} 自动删除重复的元素
	print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

	set1.add(4) #添加一个元素用add，括号里是元素
	set2.update([11, 12])  #添加多个元素用update，括号里是list
	print(set1)  # {1, 2, 3, 4}
	print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}

	set2.discard(5)
	print(set2) # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}

### 5. 字典dictionary的操作

常用的操作：字典的创建{'key':value}、更新元素的值、添加新的元素、删除元素、清空字典。

	scores = {'python': 95, 'java': 90, 'C++': 92}
	print(scores['python'])

	scores['python'] = 100 #更新字典中的元素的值
	scores.update(R=93, stata=98) #添加字典中的元素
	print(scores) #{'python': 100, 'java': 90, 'C++': 92, 'R': 93, 'stata': 98}
	
	print(scores.pop('java', 90))
	print(scores) #{'python': 100, 'C++': 92, 'R': 93, 'stata': 98}

	scores.clear() #清空字典
