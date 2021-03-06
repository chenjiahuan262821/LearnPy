'''
集合set的常见操作

通过{}或者set()来创建集合、通过add()或者update([])来添加元素、通过discard()来删除元素、
交集&、并集|、差集-、子集的判断<=。

'''

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