
'''
冒泡排序

bubbleSort1 
比较相邻的元素，如果前一个比后一个大，就交换他们两个；
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这步做完后，最后的元素会是最大的数；
针对除了最后一个元素重复以上的步骤，得到第二大的元素在倒数第二位上，即已排出最大的两个元素；
即在i次循环后，最大的i个元素已经归位在尾端，需对前面未排好序的n-i个元素进行上述操作；
直到没有任何一对数字需要比较，则序列最终有序
其中，外层循环总趟数为len-1，内层循环为在第i趟下所需要比较的次数

bubbleSort2
基于bubbleSort1，考虑到也许不用循环len-1这么多次，数列就已经排序好了，比如：  1 2 3 5 4 6 7 8 9 10
可以加一个flag来记录是否上一次循环是否发生过交换，倘若没有，就可以终止循环了

bubbleSort3
基于bubbleSort2,  每完成一趟外层循环，可以记住它最后一次交换的位置，也就是flag最后一次置1的位置
假设这个位置为P，那么P之后的元素已经有序，P之前的元素还可能无序，所以我们只需要对P之前的元素再进行排序就可以了

bubbleSort4（cocktailSort）
鸡尾酒排序、搅拌排序，改进的冒泡排序
先对数组从左到右进行升序的冒泡排序，再对数组进行从右到左的降序的冒泡排序
以此类推，持续的、依次的改变冒泡的方向，并不断缩小没有排序的数组范围

'''


def bubbleSort1(list):
	n = len(list)
	for i in range(n-1):
		for j in range(n-i-1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list


def bubbleSort2(list):
	n = len(list)
	for i in range(n-1):
		flag = 0
		for j in range(n-i-1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
				flag = 1
		if flag == 0:
			break

	return list


def bubbleSort3(list):
	n = len(list)
	flag_pos = n-1
	while flag_pos>0:
		pos = flag_pos
		flag_pos = 0
		for j in range(pos):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
				flag_pos = j
	return list


def cocktailSort(list):
	flag = 1
	bottom = 0
	top = len(list)-1
	while flag:
		flag = 0
		for j in range(bottom, top , 1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
				flag = 1
		top = top - 1

		for j in range(top, bottom, -1):
			if list[j] < list[j-1]:
				list[j], list[j-1] = list[j-1], list[j]
				flag = 1
		bottom = bottom + 1
	return list


import numpy as np
import time
a = np.random.randint(low=0, high =100, size=10)
print(a)
print(bubbleSort1(a))
print(bubbleSort2(a))
print(bubbleSort3(a))
print(cocktailSort(a))
