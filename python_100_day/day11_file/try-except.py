def main():
	try:
		with open('story.txt', 'r', encoding='utf-8') as f:
			print(f.read())
	except FileNotFoundError:
		print('无法打开指定文件')
	except LookupError:
		print('指定了未知编码')
	except UnicodeDecodeError:
		print('读取文件解码错误')

if __name__ == '__main__':
	main()

