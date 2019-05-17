'''
对比使用多进程与不使用多进程的差别
'''
# 不使用多进程，代码是一行一行往下执行，处理完一个再一个

from random import randint
from time import time, sleep

def download_task1(filename):
	print('开始下载%s...' % filename)
	time_to_download = randint(6,10)
	sleep(time_to_download)
	print('%s下载完成，耗费%d秒' % (filename, time_to_download))

def main1():
	start = time()
	download_task1('python从1到100.pdf')
	download_task1('i want to sleep.txt')	
	end = time()
	print('总共耗费%.2f秒' % (end - start))

# 使用多进程，不同的任务可以同时进行，提高效率

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task2(filename):
	print('启动下载进程，进程号[%d]' % getpid())
	print('开始下载%s...' % filename)
	time_to_download = randint(6,10)
	sleep(time_to_download)
	print('%s下载完成，耗费%d秒' % (filename, time_to_download))

def main2():
	start = time()
	p1 = Process(target = download_task2, args = ('python从1到100.pdf',))
	p1.start()
	p2 = Process(target = download_task2, args = ('i want to sleep.txt',))	
	p2.start()
	p1.join()
	p2.join()
	end = time()
	print('总共耗费%.2f秒' % (end - start))

if __name__ == '__main__':
	main1()
	main2()

