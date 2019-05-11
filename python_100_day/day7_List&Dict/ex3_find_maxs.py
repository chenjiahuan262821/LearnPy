'''
设计一个函数返回传入的列表中最大和第二大的元素的值。

最开始的思路：先找到最大的，然后大家都减最大的，看谁和最大的距离小就是第二大的
思考更快的方法：先排序一下（默认从小到大），然后倒数两个就是最大和第二大的了
程序员的思路：从列表最初的两位开始向右遍历，不断更新在遍历过的数值中的最大与第二大

'''

import time
import random

l = []
for _ in range(1000000):
    a = random.randint(0,99999)
    l.append(a)


# 最开始的思路
def find_max2_v1(x):
	m1 = max(x)
	diff = []
	lenth = len(x)

	for i in range(0, lenth-1):
		d = x[i] - m1
		diff.append(d)

	diff_max = max(diff) #注意diff中的数都会是负数，要找最大的那个（负得越小）
	loc_m2 = diff.index(diff_max)
	m2 = x[loc_m2]

	return m1, m2

start = time.process_time()
print(find_max2_v1(l))
end = time.process_time()
print("执行时间1:", (end - start), "秒")  # 执行时间: 0.453125 秒

# sort的方法
def find_max2_v2(x):
	l = sorted(x)
	m1 = l[-1]
	m2 = l[-2]
	return m1, m2

start = time.process_time()
print(find_max2_v2(l))
end = time.process_time()
print("执行时间2:", (end - start), "秒") # 执行时间: 1.015625 秒


# 遍历的方法
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
start = time.process_time()
print(max2(l))
end = time.process_time()
print("执行时间3:", (end - start), "秒") # 执行时间: 0.234375 秒
