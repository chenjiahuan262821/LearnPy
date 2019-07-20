'''
自底向上的归并排序法

从单个单个的元素开始，两个有序数列两两合并，一直到最上面合为一个数列
没有用到递归，只用到迭代

'''

def mergeSortBU(list):
	step = 1
	while step < len(list): 
		for i in range(0, len(list)-step, step*2):
			left_list = list[i : i+step]
			right_list = list[i+step : min(i+step+step, len(list))]
			list[i :min(i+step+step, len(list))] = merge(left_list, right_list)
		step *= 2
	return list


def merge(left_list, right_list):
	list = []
	i, j = 0, 0
	while i < len(left_list) and j < len(right_list):
		if left_list[i] < right_list[j]:
			list.append(left_list[i])
			i += 1
		else:
			list.append(right_list[j])
			j += 1
	list += left_list[i:]
	list += right_list[j:]
	return list


a = [9,8,9,6,7,4,22,11,3]
print(mergeSortBU(a))