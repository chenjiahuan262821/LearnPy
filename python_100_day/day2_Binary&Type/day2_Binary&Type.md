# Python100 - Day2

### 1. 二进制、十进制、八进制与十六进制

二进制：逢2进1，所以只有0和1两个数字；十进制：0-9；八进制：0-7；十六进制：0-9以及ABCDEF，逢15进1。

**二进制转十进制**

2的对应位数次方求和。以小数点左右分割，左边：个位上的数字的次数是0，十位上的数字的次数是1，依次递增，右边：十分位的数字的次数是-1，百分位上数字的次数是-2，依次递减。

比如二进制1010.10，就是十进制(1x2^3)+(0x2^2)+(1x2^1)+(0x2^0)+(1x2^(-1))+(0x2^(-2))=10.5。

**十进制转二进制**

以小数点左右分割，整数部分是：除以2直到商整数部分为0，取余并逆序排列（除二取余法），小数部分是：乘以2直到积的小数部分为0，取积的整数部分，顺序排列（乘2取整法）。

比如十进制的10.8125转二进制：10除以2得5余0，5除以2得2余1，2除以2得1余0，1除以2得0余1，所以整数部分是1010；0.8125乘以2得1.625，0.625乘以2得1.25，0.25乘以2得0.50，0.50乘以2得1.0，所以小数部分是1101；合并得对应得二进制是1010.1101。

**二进制转八进制**

以小数点作为分割，整数部分从右向左、小数部分从左向右，每3位为一组（不足3位的要用“0”补足3位），每组分别按权展开求和后得到用一位八进制数字，组合得到一个八进制数。

比如二进制的1111.100001110，整数部分：分两组（001）与（111），分别对应（0x2^2+0x2^1+1x2^0=1）与（1x2^2+1x2^1+1x2^0=7）,对应17；小数部分：分组（100）、（001）与（110），分别对应（1x2^2+0x2^1+0x2^0=4）、（1x2^0=1）与(1x2^2+1x2^1=6)，对应416；合并得对应的八进制是17.416。

**八进制转二进制**

把每一个八进制数转换成3位的二进制数，就得到一个二进制数。

比如八进制的37.416，整数部分：3对应011，7对应111，所以整数部分是11111；小数部分：4对应100，1对应001，6对应110，所以小数部分是100001110；合并得到对应的二进制是11111.100001110。

**二进制转十六进制**

类似于二进制转八进制的操作，但是是以每4位为一组（不足用0补全），进行转换。

比如二进制的1100001.111 ，整数部分：两组（0110）与（0001），分别对应（2^2+2^1=5）以及（2）就是52；小数部分：（1110）对应（8+4+2=14就是E）；合并得到对应的十六进制是52.E。

**十六进制转二进制**

把每一个十六进制数转换成4位的二进制数，就得到一个二进制数。

比如十六进制的5DF.9，整数部分：5对应0101，D对应十进制的13对应1101，F对应十进制的15对应1111，小数部分9对应1001，合并得10111011111.1001。

### 2. 变量类型

变量的类型：int、float、str、bool，可以通过type(a)查看变量a的类型。

int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。

	a = int(input('a = ')) #使用input函数输入，使用int()进行类型转换
	b = int(input('b = '))
	print('%d + %d = %d' % (a, b, a + b)) #用占位符格式化输出的字符串


### 3. 小练习:输入年份判断是不是闰年

	year = int(input('请输入年份：'))
	is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
	print('年份%d:' % year, is_leap)