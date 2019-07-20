'''
归并排序法
递归（二分）+合并，具体：
将一组数字不断二分，直至每一组都只存在单个元素，则此时每一组都是有序数列（only one element）
然后开始将每一组有序数列进行合并，具体操作类似于把前面的二分逆回去，但是一边合并一边排序：
既然是把二分逆回去，那就是有左右两个数列，先copy一份，从两个数列分别的第一个元素开始比大小，
小的放入数列的第一个位置，随之在那个数列里指针往后移一位，重复操作直到指针移到左数列或右数列的末端
此时将还没放入数列的元素全部添加到数列（不一定有序），参与下一次合并……

难点：递归的理解（一定要限定终止条件，理解虽然是同一个函数但是传入的参数不同）
要点：两个有序序列的合并

'''

def mergeSort(list):
	n = len(list)
	if n <= 1:
		return list
	mid_index = n//2
	left = mergeSort(list[:mid_index])
	right = mergeSort(list[mid_index:])
	return merge(left, right)

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



a = [9,8,9,6]
print(mergeSort(a))


