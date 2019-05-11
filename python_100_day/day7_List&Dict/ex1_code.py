'''
EX.1 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

'''

import random

def generate_code(code_len=6):
	nums = '0123456789'
	chars = 'abcdefghijklmnopqrstuvwxyz'
	all_chars = nums + chars
	last_pos = len(all_chars) - 1
	code = ''
	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]
	return code

print(generate_code(8)) #y14eox24
