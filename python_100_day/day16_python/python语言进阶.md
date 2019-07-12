# Python100 - Day16
## Python语言进阶

**小目录**

+ 数据结构的算法
+ 函数的使用方式
+ 面向对象相关知识
+ 迭代器和生成器
+ 并发编程

### 1.数据结构和算法

算法可以理解为**解决问题的方法和步骤**，评价算法从**渐进时间复杂度和渐进空间复杂度**进行。


<img src="https://raw.githubusercontent.com/chenjiahuan262821/LearnPy/master/python_100_day/day16_python/time_complexity.jpg" width="40%" height="40%">


学到这里的时候，最多是能通过循环的层数区别n的几次方，所以要继续加把劲学，把这些都搞懂~~~

#### 排序算法（选择、插入、冒泡和归并）

##### 选择排序

选择排序的算法：先设置minIndex为i，对应值为list[i]，然后，从i+1开始往后遍历找出最小的值，并将minIndex设置为该值的位置，最后将i位置与minIndex位置的数值互换，就得到第i大的值
	
	a = [6,5,4,3,2,1,10,8,9,8.1]
	
	def selectionSort(list):
		for i in range(len(list)):
			minIndex = i
			for j in range(i+1, len(list)):
				if list[j] < list[minIndex]:
					minIndex = j
			list[i], list[minIndex] = list[minIndex], list[i]
	
		print(list)
	
	selectionSort(a)

##### 插入排序

插入排序的算法：一组数据视作分成两组，分别为有序组与待插入组，每次从待插入组中取出一个元素，与有序组的元素进行比较，找到合适的位置，插到有序组当中。

插入过程中涉及到了元素的移动，有不同的方式。以下，insertionSort1是待插入数一边移动一边比较，直到所在位置比前一个数大（多次插入），insertionSort2是先将待插入数赋给新变量，先比较好、移动出空位在插入（一次插入）

	a = [6,5,4,3,2,1,10,8,9,8.1]
	
	def insertionSort1(list):
		for i in range(1, len(list)):
			for j in range(i, 0, -1):
				if list[j] < list [j-1]:
					list[j], list[j-1] = list[j-1], list[j]
				else: 
					break
		print(list)
	
	insertionSort1(a)
	
	def insertionSort2(list):
		for i in range(1, len(list)):
			ins = list[i] 
			for j in range(i, 0, -1):
				if list[j-1] > ins:
					list[j] = list[j-1]
				else:
					list[j] = ins
					break
		print(list)
	
	insertionSort2(a)

##### 希尔排序

希尔排序是升级版的插入排序，主要思想是：把序列按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

这里用一张图表达希尔排序的过程：

<img src="https://raw.githubusercontent.com/chenjiahuan262821/LearnPy/master/python_100_day/day16_python/shellSort.jpg" width="40%" height="40%">

通过增量的设置，希尔排序减少了插入排序中许多无效的比较，所以其时间复杂度较直接插入排序低，低于O(n^2)，它的时间是所取“增量”序列的函数:最好时间复杂度是O(n)，平均时间复杂度： O(1.2^n ~ 1.5^n)，最坏时间复杂度： O(n^2)。

在希尔排序的理解时，我们倾向于以每一个分组进行处理去理解，但在代码实现中，不用这么按部就班地处理完一组再调转回来处理下一组，实现过程中，是从第step个元素开始，逐个跨组处理，同时，在插入数据时，采用元素交换法寻找最终位置。


首先，设置一个递减的增量序列作为步长step（通常是：n/2, n/4, n/8...，不过实际上会有更好的序列）。其次，每次循环都从第step个元素开始遍历，（i>=step）倘若第i个元素值小于第i-step个元素值，则交换。交换后i-=step（这是很重要的一步），倘若新的i依然满足（i>=step）的条件则继续对比及交换的过程，此处相当于每一组内进行插入排序的过程（要把组内前面的先排好再增添新的元素进来参与排序），以此类推。随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，排序完成后，算法便终止。

	def shellSort(list):
		n = len(list)
		step = int(n/2)
		while step > 0 :
			for i in range(step, n):
				while i >= step and list[i] < list[i-step]:
					list[i-step], list[i] = list[i], list[i-step]
					i -= step
			step = int(step/2) 
		return list
	
	import numpy as np
	
	a = np.random.randint(low=0, high =200, size=9)
	
	print(a) # [107 120  90 104 158  64  75 133 174]
	print(shellSort(a)) # [ 64  75  90 104 107 120 133 158 174]


##### 冒泡排序

+ bubbleSort1-基本款

比较相邻的元素，如果前一个比后一个大，就交换他们两个；对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这步做完后，最后的元素会是最大的数。针对除了最后一个元素重复以上的步骤，得到第二大的元素在倒数第二位上，即已排出最大的两个元素，即在i次循环后，最大的i个元素已经归位在尾端，只需对前面未排好序的n-i个元素进行上述操作，直到没有任何一对数字需要比较，则序列最终有序。其中，外层循环总趟数为len-1，内层循环为在第i趟下所需要比较的次数。

	def bubbleSort1(list):
		n = len(list)
		for i in range(n-1):
			for j in range(n-i-1):
				if list[j] > list[j+1]:
					list[j], list[j+1] = list[j+1], list[j]
		return list

+ bubbleSort2-升级款（标记判断）

基于bubbleSort1，考虑到也许不用循环len-1这么多次，数列就已经排序好了，比如（这里只需交换4和5） 1 2 3 5 4 6 7 8 9 10。 可以加一个flag来记录是否上一次循环是否发生过交换，倘若没有，就可以终止循环了。
	
	def bubbleSort2(list):
		n = len(list)
		for i in range(n-1):
			flag = 0
			for j in range(n-i-1):
				if list[j] > list[j+1]:
					list[j], list[j+1] = list[j+1], list[j]
					flag = 1
			if flag == 0:
				break
	
		return list

+ bubbleSort3-升级款（记录标记位置）

基于bubbleSort2只是打了标记，事实上，可以进一步记住它最后一次交换的位置，也就是上一段中flag最后一次置1的位置。假设这个位置为P，那么P之后的元素已经有序，P之前的元素还可能无序，所以我们只需要对P之前的元素再进行排序就可以了。下面代码中，flag_pos记录下最后一次交换的位置，当flag_pos为0，则表明上一次循环没有任何交换-排序已完成，则会终止循环。

	def bubbleSort3(list):
		n = len(list)
		flag_pos = n-1
		while flag_pos>0:
			pos = flag_pos
			flag_pos = 0
			for j in range(pos):
				if list[j] > list[j+1]:
					list[j], list[j+1] = list[j+1], list[j]
					flag_pos = j
		return list

+ bubbleSort4（cocktailSort）-鸡尾酒款（来回搅拌）

先对数组从左到右进行升序的冒泡排序，再对数组进行从右到左的降序的冒泡排序，以此类推，持续的、依次的改变冒泡的方向，并不断缩小没有排序的数组范围。

	def cocktailSort(list):
		flag = 1
		bottom = 0
		top = len(list)-1
		while flag:
			flag = 0
			for j in range(bottom, top , 1):
				if list[j] > list[j+1]:
					list[j], list[j+1] = list[j+1], list[j]
					flag = 1
			top = top - 1
	
			for j in range(top, bottom, -1):
				if list[j] < list[j-1]:
					list[j], list[j-1] = list[j-1], list[j]
					flag = 1
			bottom = bottom + 1
		return list


+ 归并排序


