'''
插入排序的算法
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


