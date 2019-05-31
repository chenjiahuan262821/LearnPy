'''
选择排序的算法
先设置minIndex为i，对应值为list[i]
然后从i+1开始往后遍历找出最小的值，并将minIndex设置为该值的位置
最后将i位置与minIndex位置的数值互换，就得到第i大的值
'''

a = [6,5,4,3,2,1,10,8,9,8.1]

def selectionSort(list):
	for i in range(len(list)):
		minIndex = i
		for j in range(i+1, len(list)):
			if list[j] < list[minIndex]:
				minIndex = j
		list[i], list[minIndex] = list[minIndex], list[i]

	print(list)

selectionSort(a)