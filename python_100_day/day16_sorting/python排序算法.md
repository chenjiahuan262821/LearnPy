# Python100 - Day16
## 排序算法的学习

**小目录**

+ 渐进时间复杂度概念
+ 排序算法的学习
	+ 选择排序
	+ 插入排序
	+ 希尔排序
	+ 冒泡排序
	+ 归并排序
	+ 快速排序

### 1.渐进时间复杂度

算法可以理解为**解决问题的方法和步骤**，评价算法从**渐进时间复杂度和渐进空间复杂度**进行。


<img src="https://raw.githubusercontent.com/chenjiahuan262821/LearnPy/master/python_100_day/day16_python/time_complexity.jpg" width="40%" height="40%">


学到这里的时候，最多是能通过循环的层数区别n的几次方，所以要继续加把劲学，把这些都搞懂~~~

### 2.排序算法（选择、插入、希尔、冒泡、归并（自顶向下、自底向上）、快速排序）

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




##### 归并排序

> 自顶向下对的归并排序以及快速排序都用到了一个很重要的思想，那就是：分而治之——将原问题分解为若干个规模更小但结构与原问题相似的子问题，用递归的方法地解这些子问题，然后将这些子问题的解组合为原问题的解。
> 
> 自底向上的归并排序虽然没有用递归，用的是迭代的思想，但是传说这道题在算法面试的时候经常考到，这也是用于解决链表排序的重要方法。

+ 自顶向下归并排序

“归并”拆成：递归（二分）+合并，下面mergeSort函数就是不断进行二分直到直至每一组都只存在单个元素，然后调用merge函数，而merge函数作用就是对两个有序数列进行合并成新的有序数列（大致是有序，但是会将剩下的元素直接加入数列，它们不一定有序）。

具体操作：
将一组数字不断二分，直至每一组都只存在单个元素，则此时每一组都是有序数列（only one element）。然后，开始对有序数列进行合并，类似于把前面的二分逆回去，一边合并一边排序：左右两个数列，先copy一份，从两个数列分别的第一个元素开始比大小，小的放入数列的第一个位置，随之在那个数列里指针往后移一位，重复操作直到指针移到左数列或右数列的末端。此时将还没放入数列的元素全部添加到数列（不一定有序），参与下一次合并……

难点在于对递归的理解（一定要限定终止条件，理解虽然是同一个函数但是传入的参数不同），在理解利用递归实现的二分后，编写函数实现两个有序序列的合并就Ok了。

	def mergeSort(list):
		n = len(list)
		if n <= 1:
			return list
		mid_index = n//2
		left = mergeSort(list[:mid_index])
		right = mergeSort(list[mid_index:])
		return merge(left, right)
	
	def merge(left_list, right_list):
		list = []
		i, j = 0, 0
		while i < len(left_list) and j < len(right_list):
			if left_list[i] < right_list[j]:
				list.append(left_list[i])
				i += 1
			else:
				list.append(right_list[j])
				j += 1
		list += left_list[i:]
		list += right_list[j:]
		return list


+ 自底向上归并排序

自底向上的归并排序没有用到递归，只用到迭代。传说是面试常考题，它的特殊的点在于，没有使用数组index的特性（疑问：真的没有用到吗，我怎么觉得用到了？），可以用于实现对链表的nlogN复杂度的排序。

从单个单个的元素开始，两个有序数列两两合并，一直到最上面合为一个数列

	def mergeSortBU(list):
		step = 1
		while step < len(list): 
			for i in range(0, len(list)-step, step*2):
				left_list = list[i : i+step]
				right_list = list[i+step : min(i+step+step, len(list))]
				list[i :min(i+step+step, len(list))] = merge(left_list, right_list)
			step *= 2
		return list
	
	
	def merge(left_list, right_list):
		list = []
		i, j = 0, 0
		while i < len(left_list) and j < len(right_list):
			if left_list[i] < right_list[j]:
				list.append(left_list[i])
				i += 1
			else:
				list.append(right_list[j])
				j += 1
		list += left_list[i:]
		list += right_list[j:]
		return list

##### 快速排序

在序列中抽取一个元素，先把这个元素放到它排序后应该在的位置上，同时使得这个元素把序列分割成两个独立部分——左边部分的序列都比划分值小，右边部分的序列比划分值大，然后再对这两个序列按照同样的方法进行排序，直到整个序列都有序。

下面partition函数的作用就是找到那个分割的位置，具体操作是：先把待排序的一个值赋给pivot_value，然后与序列中的值从右到左进行比较，倘若值比pivot_value大则不用动，指针向左移一位即可，但如果比pivot_value小，那么这个值要放去左边的位置，这里的操作是放入左边指针所在位置，覆盖后则从左到右开始比较，倘若值比pivot_value小则不用动，指针向右移一位即可，但如果比pivot_value大，则要放去右边，这里的操作时覆盖掉上一步里被放到左边的那个数的值（右边指针停留的位置）；而q_sort函数用递归的方式对被分割的两个序列重复操作~

	def quickSort(L):
		return q_sort(L, 0, len(L)-1)
	
	def q_sort(L, left, right):
		if left<right:
			pivot = partition(L, left, right)
			q_sort(L, left, pivot-1)
			q_sort(L, pivot+1, right)
		return L
	
	def partition(L, left, right):
		pivot_value = L[left]
	
		while left<right:
			while left<right and L[right]>=pivot_value:
				right -= 1
			L[left] = L[right]
			while left<right and L[left]<=pivot_value:
				left += 1
			L[right] = L[left]
	
		L[left] = pivot_value
		return left
	
	a = [9,8,9,6,7,4,22,11,3]
	print(quickSort(a))

其他考虑：对于上面的代码，分组基准的选取只是取列表的第一个值，太过于随便，如果能够取到序列的中间值时，快排效率是最高的；若序列长度过于小(比如只有几个元素)，快排效率就不如插入排序了，可以设置一个列表元素大小的临界值，若小于这个值，就用插入排序，大于这个值用快排。

**撒花，至此，排序的算法基本学过一遍啦！！！**


