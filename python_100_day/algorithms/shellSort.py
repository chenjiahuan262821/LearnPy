'''
希尔排序的算法
这是一个优化的插入排序，通过设置增量，减少再插入排序中那种无效的排序

主要思想是：
设置一个递减的增量序列作为步长step（通常是：n/2, n/4, n/8...，不过实际上会有更好的序列）
每次循环都从第step个元素开始遍历，（i>=step）倘若第i个元素值小于第i-step个元素值，则交换
交换后i-=step（这是很重要的一步），倘若新的i依然满足（i>=step）的条件则继续对比及交换的过程
此处每一组内进行的就是插入排序的过程（要把组内前面的先排好再增添新的元素进来参与排序）
以此类推
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，排序完成后，算法便终止
'''


def shellSort(list):
	n = len(list)
	step = int(n/2)
	while step > 0 :
		for i in range(step, n):
			while i >= step and list[i] < list[i-step]:
				list[i-step], list[i] = list[i], list[i-step]
				i -= step
		step = int(step/2) 
	return list

import numpy as np

a = np.random.randint(low=0, high =200, size=9)

print(a)
print(shellSort(a))







