'''
选择排序的算法
'''

def selectionSort(list):
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			minIndex = i
			if list[j] < list[minIndex]:
				minIndex = j

				list[i], list[minIndex] = list[minIndex], list[i]
	print(list)

selectionSort([6,5,4,3,2,1,10,8,9,8.1])