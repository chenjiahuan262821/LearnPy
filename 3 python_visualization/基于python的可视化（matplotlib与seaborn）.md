### 基于python的可视化——matplotlib与seaborn

**小目录**

+ python自带画图
+ matplotlib图形绘制
+ seaborn应用



#### 1. python自带的画图

python自带画图的常用命令是xxx.plot()

	df.plot()  #将datafreame整体可视化，以index为横轴，不同columns_name作不同曲线
	df.plot(figsize = (8,6), title = 'graph title') #调整图表大小，给图表命名
	df.plot(ylim = [np.min(df.col), np.max(df.col)*1.2] #设置坐标轴范围

	df[['col1','col2']].plot() #选取dataframe中某些列
	df[['col1','col2']].plot(subplots=True) #子图，不同的列分开作图

	df.hist(figsize=(6,8), bins=12) #画直方图
	df.plot(x='col1', y='col2', kind='scatter'） #画散点图
	df.plot(style=['o', 'm--']) #曲线颜色与样式可以修改（列表中元素分别对应不同列）'m--'相当于color='m',linestyle='--'
	df.plot(secondary_y = 'col2'）#如果不同数据的数量级差别大，可以用次坐标轴解决

#### 2. matplotlib图形绘制

	pip install matplotlib

	import matplotlib.pyplot as plt
	plt.figure(figsize=(6,8)) #确定图片大小
	plt.plot(x_data, y_data, 'm--', linewidth=1, label='data') #第一个位置放x轴数据，第二个位置放y轴数据，之后可以设置颜色和样式、图例中的名称
	plt.title('TITLE') #给图表命名
	plt.ylabel('YLABEL') #给y轴命名
	plt.xlabel('XLABEL') #给x轴命名
	plt.legend() #显示图例
	plt.ylim(0, 10) #设置坐标轴范围
	plt.bar(x, y, color='r') #绘制柱状图
	plt.scatter(x, y, color='r') #绘制散点图，设置颜色
	plt.gird(True) #设置网格

有些时候想把多条曲线绘制在同一幅图里：

	plt.plot(x, y1, 'r--',
			 x, y2, 'o',
			 x, y3, '--') #一次性绘制多线条在一幅图里	
	
	plt.figure(figsize = (8,6))    
	plt.plot(x1,y1,linewidth=1, label = 'line1')   
	plt.plot(x2,y2,linewidth=1, label = 'line2')
	plt.title('Two Line Plot')
	plt.ylabel('Y axis')
	plt.xlabel('X axis')   #也可以分别设定，然后放在同一幅图里，更常用

双坐标轴的设定：

	fig1,ax = plt.subplots(figsize = (10,6))   #plt.subplots会返回一个figure对象和一个坐标轴对象；
	plt.plot(y[:, 0], lw=1.5, label='line1')
	plt.legend(loc=8)
	plt.xlabel('x')
	plt.ylabel('y1')
	plt.title('plot')
	ax2 = ax.twinx()       #复制上一张子图的横坐标轴；
	plt.plot(y[:, 1], 'g', lw=1.5, label='line2')
	plt.legend(loc=10)
	plt.ylabel('y2')

有些时候想把绘制子图进行对比：
	
	plt.subplot(abc) #例如211，212，121，122；a代表横向几幅图，b代表纵向几幅图，c表示接下去设置几幅图
	

#### 3. seaborn应用

	pip install seaborn

暂时还木有用到seaborn的高端制图~~ 

参考：[seaborn官方制图示例（附代码）](https://seaborn.pydata.org/examples/index.html)

十分突出的功能：数据集分布可视化

	import seaborn as sns

单变量分布

	sns.distplot()
	sns.distplot(kde=False) #直方图
	sns.distplot(hist=False) #核密度估计，或者敲sns.kdeplot()
	sns.distplot(kde=False, fit=) #拟合参数分布

双变量分布

	sns.jointplot() #散布图
	Hexbinsns.jointplot(kind='hex') #二维直方图
	sns.jointplot(kind=‘kde’) #核密度估计
	sns.pairplot() #数据集中变量间关系可视化


备注：

**颜色**

b: blue;
g: green;
r: red;
c: cyan;
m: magenta;
y: yellow;
k: black;
w: white;

**标记**

'.'; 'o'; 'v'; '^';

**线型**

'-': 实线，
'--'： 虚线