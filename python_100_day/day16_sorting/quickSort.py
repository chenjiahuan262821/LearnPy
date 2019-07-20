'''
在序列中抽取一个元素，先把这个元素放到它排序后应该在的位置上
同时使得这个元素把序列分割成两个独立部分——左边部分的序列都比划分值小右边部分的序列比划分值大
然后再对这两个序列按照同样的方法进行排序，直到整个序列都有序

下面partition函数的作用就是找到那个分割的位置，而q_sort函数用递归的方式对被风格的两个序列重复操作
'''



def quickSort(L):
	return q_sort(L, 0, len(L)-1)

def q_sort(L, left, right):
	if left<right:
		pivot = partition(L, left, right)
		q_sort(L, left, pivot-1)
		q_sort(L, pivot+1, right)
	return L

def partition(L, left, right):
	pivot_value = L[left]

	while left<right:
		while left<right and L[right]>=pivot_value:
			right -= 1
		L[left] = L[right]
		while left<right and L[left]<=pivot_value:
			left += 1
		L[right] = L[left]

	L[left] = pivot_value
	return left

a = [9,8,9,6,7,4,22,11,3]
print(quickSort(a))
 