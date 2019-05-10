
# 俺的方案：

fib = []
fib.extend([1,1])
for i in range(2, 20):
    num = fib[i-1] + fib[i-2]
    fib.append(num)
print(fib)

# 优化的方案：

a = 0
b = 1
for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')