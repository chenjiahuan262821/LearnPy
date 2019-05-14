from math import sqrt

class Triangle(object):

	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c

	@staticmethod		#静态方法，说明接下来的这个方法是绑定在类上的
	def is_valid_static(a, b, c):
		return a + b > c and b + c > a and a + c > b #有效的话会返回True

	@classmethod		#类方法，第一个参数约定名为cls，代表当前类相关的信息
	def is_valid_class(cls, a, b, c):
		return a + b > c and b + c > a and a + c > b

	def perimeter(self):
		return self._a + self._b + self._c 
	def area(self):
		half = self.perimeter() / 2
		return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
	a, b, c = 6, 10, 6
	
	if Triangle.is_valid_static(a, b, c):   #静态方法是在给类发消息的时候调用的
		t = Triangle(a, b, c)
		print(t.perimeter())
	else:
		print('无法构成三角形')

	if Triangle.is_valid_class(a, b, c):   #类方法是在给类发消息的时候调用的
		t = Triangle(a, b, c)
		print(t.area())
	else:
		print('无法构成三角形')

	#静态方法、类方法，都是绑定在类上的，但是对象也可以访问
	print(t.is_valid_static(5,3,4)) 
	print(t.is_valid_class(5,3,4)) 

if __name__ == '__main__':
	main()