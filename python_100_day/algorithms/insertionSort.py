'''
插入排序的算法

一组数据视作分成两组，分别为有序组与待插入组
每次从待插入组中取出一个元素，与有序组的元素进行比较，找到合适的位置，插到有序组当中

插入过程中涉及到了元素的移动，有不同的方式
insertionSort1是待插入数一边移动一边比较，直到所在位置比前一个数大（多次插入）
insertionSort2是先将待插入数赋给新变量，先比较好、移动出空位在插入（一次插入）
'''

a = [6,5,4,3,2,1,10,8,9,8.1]

def insertionSort1(list):
	for i in range(1, len(list)):
		for j in range(i, 0, -1):
			if list[j] < list [j-1]:
				list[j], list[j-1] = list[j-1], list[j]
			else: 
				break
	print(list)

insertionSort1(a)

def insertionSort2(list):
	for i in range(1, len(list)):
		ins = list[i] 
		for j in range(i, 0, -1):
			if list[j-1] > ins:
				list[j] = list[j-1]
			else:
				list[j] = ins
				break
	print(list)

insertionSort2(a)


