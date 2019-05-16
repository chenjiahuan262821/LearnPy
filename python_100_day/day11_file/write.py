from math import sqrt

# is_prime函数的返回结果是True或者False
def is_prime(n):
	assert n > 0
	for factor in range(2, int(sqrt(n)) + 1):
		if n % factor == 0:
			return False
	return True if n != 1 else False

'''
将1-9999直接的素数分别写入三个文件中
1-99之间的素数保存在a.txt中
100-999之间的素数保存在b.txt中
1000-9999之间的素数保存在c.txt中
'''

def main():
	filenames = ('a.txt', 'b.txt', 'c.txt')
	fs_list = []  #创建一个空列表
	try:
		for filename in filenames:
			fs_list.append(open(filename, 'w', encoding='utf-8')) #将文本文件打开，作为一个元素加入fs_list中
			print(fs_list)
		for number in range(1,10000):
			if is_prime(number):
				if number < 100:
					fs_list[0].write(str(number) + '\n') #写入对应的文本文件中
				elif number < 1000:
					fs_list[1].write(str(number) + '\n')
				else:
					fs_list[2].write(str(number) + '\n')
	except IOError as ex:
		print(ex)
		print('写文件时发生错误')
	finally:
		for fs in fs_list:
			fs.close
	print('操作完成')

if __name__ == '__main__':
	main()
