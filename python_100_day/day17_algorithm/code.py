
'''嵌套的列表'''

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误：scores = [[None] * len(courses)] * len(names)
# 正确：嵌套的列表
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
	for col, courses in enumerate(courses):
		# scores[row][col] = float(input(f'请输入{name}的{courses}成绩：'))
		print(scores)


"""
heapq、itertools等的用法:
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools

print(list(itertools.permutations('ABCD')))
print(list(itertools.combinations('ABCDE', 3)))
print(list(itertools.product('ABCD', '123')))