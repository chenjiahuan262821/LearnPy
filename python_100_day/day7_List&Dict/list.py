'''
常见的列表操作

计算列表的长度即所含元素的个数len()、列表的下标索引[]、通过下标索引修改元素值、
删除元素remove(具体元素的值)或者del后跟列表索引、清空列表clear()、切片操作与赋值[]、
排序操作sort与sorted、生成式语法创建列表

'''

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
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits.append('pear') # print(fruits) 返回['grape', 'apple', 'strawberry', 'waxberry', 'pear']
fruits.extend(['pitaya', 'mango']) # print(fruits) 返回['grape', 'apple', 'strawberry', 'waxberry', 'pear', 'pitaya', 'mango']
print(fruits) # ['grape', 'apple', 'strawberry', 'waxberry', 'pear', 'pitaya', 'mango']
fruits2 = fruits[1:4] # print(fruits2) 返回['apple', 'strawberry', 'waxberry']
fruits3 = fruits[-3:-1] # print(fruits3)返回['pear', 'pitaya']
fruits4 = fruits[::-1] # 可以通过反向切片操作来获得倒转后的列表的拷贝，print(fruits4) 返回['mango', 'pitaya', 'pear', 'waxberry', 'strawberry', 'apple', 'grape']

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

# 元组与列表
t = ('亮亮', 22, 'bf', '上海') #创建元组
bf = list(t) #将元组转换成列表
p = tuple(bf) #将列表转换成元组
print(bf)
print(p)