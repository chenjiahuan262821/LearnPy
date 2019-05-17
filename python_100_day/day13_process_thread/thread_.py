'''
Python中的多线程，推荐使用threading模块进行多线程开发
'''

from random import randint
from threading import Thread
from time import time, sleep

# 直接使用threading模块的Thread类来创建线程，和之前的Process是一样的

def download(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(6, 10)
	sleep(time_to_download)
	print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main1():
	start = time()
	t1 = Thread(target=download, args=('python从1到100.pdf',))
	t1.start()
	t2 = Thread(target=download, args=('i want to sleep.txt',))
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('总共耗费%.2f秒' % (end-start))

# 继承Thread类的方式来创建自定义的线程类

class DownloadTask(Thread):

	def __init__(self, filename):
		super().__init__()
		self._filename = filename

	def run(self):
		print('开始下载%s...' % self._filename)
		time_to_download = randint(6,10)
		sleep(time_to_download)
		print('%s下载完成，耗费了%d秒' % (self._filename, time_to_download))

def main2():
	start = time()
	t1 = DownloadTask('python从1到100.pdf')
	t1.start()
	t2 = DownloadTask('i want to sleep.txt')
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('总共耗费%.2f秒' % (end-start))

if __name__ == '__main__':
	main1()
	main2()
