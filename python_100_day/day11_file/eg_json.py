import json

def main():
	mydict = {
		'name' : '老王',
		'age' : 22,
		'qq' : 914932028,
		'friends' : ['老陈', '老李'],
		'cars' : [
			{'brand':'BYD', 'max_speed':180},
			{'brand':'AUDI', 'max_speed':280},
			{'brand':'Benz', 'max_speed':320}]
	}
	try:
		with open('data.json', 'w', encoding='utf-8') as fs:
			json.dump(mydict, fs)
	except IOError as e:
		print(e)
	print('保存数据完成')

if __name__ == '__main__':
	main()