import time
import random

list = []
for _ in range(1000000):
    a = random.randint(0,99999)
    list.append(a)

def find_max2(x):
	l = sorted(x)
	m1 = l[-1]
	m2 = l[-2]
	return m1, m2

start = time.process_time()
print(find_max2(list))
end = time.process_time()
print("执行时间:", (end - start), "秒")

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
print(max2(list))
end = time.process_time()
print("执行时间:", (end - start), "秒")