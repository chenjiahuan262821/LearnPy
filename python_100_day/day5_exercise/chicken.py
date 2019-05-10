# 方案1：
for x in range(20):
    for y in range(33):
        for z in range(100):
            if (x + y + z == 100) & (5 * x + 3 * y + 1/3 * z == 100):
                print('公鸡数量为%d，母鸡数量为%d，小鸡数量为%d' % (x, y, z))

#方案2（优化的代码）：
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
