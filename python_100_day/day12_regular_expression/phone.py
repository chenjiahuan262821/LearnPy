'''
从一段文字中提取出国内手机号码。
截止到2017年底，国内三家运营商推出的手机号段:
电信号：133 153 180 181 189 177
联通号：130 131 132 155 156 185 145 176
移动号：134 135 136 137 138 139 150 151 152  
		157 158 159 182 183 184 187 188 147 178
'''

import re

def main():

	# 使用前瞻(?<=\D)和回顾(?=\D)来保证手机号前后不应该出现数字
	pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')

	sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''

	# 查找所有匹配并保存到一个列表中
	phone_list = re.findall(pattern, sentence)
	print(phone_list)
	print('------')

	# 通过迭代器取出匹配对象并获得匹配的内容
	for temp in pattern.finditer(sentence):
		print(temp.group())
	print('------')

	# 通过search函数指定搜索位置找出所有匹配
	m = pattern.search(sentence)
	while m:
		print(m.group())
		m = pattern.search(sentence, m.end())
	print('------')
	
if __name__ == '__main__':
    main()

