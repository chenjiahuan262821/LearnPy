def main():
	try:
		with open('wechat.jpg', 'rb') as fs_r:
			data = fs_r.read()
			print(type(data))
		with open('wechat.jpg', 'wb') as fs_w:
			fs_w.write(data)
	except FileNotFoundError as e1:
		print('指定文件无法打开')
	except IOError as e2:
		print('文件读写出现错误')

if __name__ == '__main__':
	main()