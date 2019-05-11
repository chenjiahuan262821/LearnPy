'''
EX.2 设计一个函数返回给定文件名的后缀名。

'''

def get_suffix(filename, has_dot=False):

	pos = filename.rfind('.')
	if 0 < pos < len(filename)-1:
		index = pos if has_dot else pos+1  #返回的后缀名是否需要带点
		return filename[index:]
	else:
		return 'no suffix'

print(get_suffix('ex.py', has_dot=True))  # 返回.py
print(get_suffix('ex.py'))  # 返回py
print(get_suffix('app'))  #返回no suffix