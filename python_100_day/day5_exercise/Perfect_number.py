'''
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
'''

# 方案1：
import time
start = time.clock()
for i in range(1, 10000):
    end = i-1
    sum = 0
    for j in range(1, end):
        if i % j == 0:
            sum += j
    if sum == i:
        print('we find the Perfect number:', i)
end = time.clock()
print("执行时间:", (end - start), "秒")

# 方案2：
import time
start = time.clock()
def find_perfect(i):
    end = i-1
    sum = 0
    for j in range(1, end):
        if i % j == 0:
            sum += j
    if sum == i:
        print('we find the Perfect number:', i)

l = map(find_perfect, range(1, 10000))
list(l)
end = time.clock()
print("执行时间:", (end - start), "秒")

# 方案3（最快的）：
import time
import math

start = time.clock()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print('we find the Perfect number:', num)
end = time.clock()
print("执行时间:", (end - start), "秒")
