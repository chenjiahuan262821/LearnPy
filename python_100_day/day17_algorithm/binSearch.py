
'''折半查找'''

def binSearch(items, key):
	start, end = 0, len(items)-1
	while start <= end:
		mid = (start+end)//2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1

a = [8,9,7,6,5,4,8]
# print(binSearch(a, 8))  # 返回6，说明只能找到一个

