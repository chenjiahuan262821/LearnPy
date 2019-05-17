# Python100 - Day13
## 进程和线程

进程和线程都是操作系统的概念，略抽象，参考阮一峰的一个比喻：
> 计算机的核心是CPU，它承担了所有的计算任务。它就像一座工厂，时刻在运行。
> 
> 假定工厂的电力有限，一次只能供给一个车间使用。也就是说，一个车间开工的时候，其他车间都必须停工。背后的含义就是，单个CPU一次只能运行一个任务。进程就好比工厂的车间，它代表CPU所能处理的单个任务。任一时刻，CPU总是运行一个进程，其他进程处于非运行状态。
> 
> 一个车间里，可以有很多工人，协同完成一个任务，线程就好比车间里的工人。一个进程可以包括多个线程。车间的空间是工人们共享的，比如许多房间是每个工人都可以进出的。这象征一个进程的内存空间是共享的，每个线程都可以使用这些共享内存。
> 
> 可是，每间房间的大小不同，有些房间最多只能容纳一个人，比如厕所。里面有人的时候，其他人就不能进去了。这代表一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。一个防止他人进入的简单方法，就是门口加一把锁。先到的人锁上门，后到的人看到上锁，就在门口排队，等锁打开再进去。这就叫"互斥锁"（Mutual exclusion，缩写 Mutex），防止多个线程同时读写某一块内存区域。
> 
> 还有些房间，可以同时容纳n个人，比如厨房。也就是说，如果人数大于n，多出来的人只能在外面等着。这好比某些内存区域，只能供给固定数目的线程使用。这时的解决方法，就是在门口挂n把钥匙。进去的人就取一把钥匙，出来时再把钥匙挂回原处。后到的人发现钥匙架空了，就知道必须在门口排队等着了。这种做法叫做"信号量"（Semaphore），用来保证多个线程不会互相冲突。
> 
> 操作系统的设计，因此可以归结为三点：
> 
> （1）以多进程形式，允许多个任务同时运行；
> 
> （2）以多线程形式，允许单个任务分成不同的部分运行；
> 
> （3）提供协调机制，一方面防止进程之间和线程之间产生冲突，另一方面允许进程之间和线程之间共享资源。

### 对比使用多线程与不使用多线程的差别

在下面使用多线程的模块里，通过Process类创建了进程对象，通过target参数传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。

	# 不使用多进程，代码是一行一行往下执行，处理完一个再一个

	from random import randint
	from time import time, sleep

	#这里是模拟下载文件
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
		main1()   #总共耗费13.00秒
		main2()	  #总共耗费8.44秒

### 在Python中的多线程

可以直接使用threading模块的Thread类来创建线程（用法与上面的Process类似），也可以基于“继承”的概念，从已有的类创建新的类——通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程。

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

	if __name__ == '__main__':
		main1()

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

### 上锁保护临界资源

多个线程可以共享进程的内存空间，因此要实现多个线程间的通信最直接的办法就是设置一个全局变量，多个线程共享这个全局变量即可。但是当多个线程共享同一个变量时，很有可能产生不可控的结果从而导致程序失效甚至崩溃。

> 比如，100个线程向同一个银行账户转账（转入1元钱），因为没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money，多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，结果远远小于100元。

**使用“锁”来保护对银行账户的操作:**

	from time import sleep
	from threading import Thread, Lock
	
	class Account(object):
	
		def __init__(self):
			self._balance = 0 
			self._lock = Lock()
	
		def deposit(self, money):
			self._lock.acquire()  #先获取了锁才能执行后续操作
			try:
				new_balance = self._balance + money # 计算存款后的余额
				sleep(0.01)    # 模拟受理存款业务需要0.01秒的时间
				self._balance = new_balance    # 修改账户余额
			finally:
				self._lock.release # 在finally中执行释放锁的操作保证正常异常锁都能释放

		@property
		def balance(self):
			return self._balance

	class AddMoneyThread(Thread):
	
		def __init__(self, account, money):
			super().__init__()
			self._account = account
			self._money = money

		def run(self):
			self._account.deposit(self._money)

	def main():
		account = Account()
		threads = []
		# 创建100个存款的线程向同一个账户中存钱
		for _ in range(100):
			t = AddMoneyThread(account, 1)
			threads.append(t)
			t.start()
		# 等所有存款的线程都执行完毕
		for t in threads:
			t.join()
		print('账户余额为: ￥%d元' % account.balance)

	if __name__ == '__main__':
		main()	