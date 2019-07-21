'''
collections是Python内建的一个集合模块，提供了许多有用的集合类
'''

'''
namedtuple
用法：namedtuple('名称', [属性list])
创建一个自定义的tuple对象，并且规定了tuple的属性及元素的个数，可以用属性而不是索引来引用tuple的某个元素
用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
'''

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)   # 1
print(p.y)   # 2

print(isinstance(p, Point)) # True
print(isinstance(p, tuple)) # True


'''
deque
高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
from collections import deque
l = ['a','b','c','v']
q = deque(l)
q.append('w')
q.appendleft('o')
print(q) #deque(['o', 'a', 'b', 'c', 'v', 'w'])


'''
Counter
可以用来统计元素出现的次数
'''

# 找出序列中出现次数最多的元素

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3)) #[('eyes', 8), ('the', 5), ('look', 4)]

print(counter