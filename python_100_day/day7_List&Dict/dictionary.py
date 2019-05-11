'''
字典的常用操作：

字典的创建{'key':value}、更新元素的值、添加新的元素、删除元素、清空字典

'''


scores = {'python': 95, 'java': 90, 'C++': 92}
print(scores['python'])

scores['python'] = 100 #更新字典中的元素的值
scores.update(R=93, stata=98) #添加字典中的元素
print(scores) #{'python': 100, 'java': 90, 'C++': 92, 'R': 93, 'stata': 98}

print(scores.pop('java', 90))
print(scores) #{'python': 100, 'C++': 92, 'R': 93, 'stata': 98}

scores.clear() #清空字典


