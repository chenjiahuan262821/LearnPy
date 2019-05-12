class Student(object):

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def study(self, course_name):
		print('%s正在学习%s' % (self.name, course_name))

	def love(self):
		if self.age >= 18:
			print('%s已经是大人了，谈恋爱是开启一项长期投资' % self.name)
		else:
			print('%s还是个小孩，谈恋爱会遭到家长限制' % self.name)

	def dating(self):
		if self.gender == '男':
			print('%s约会出门前只需1分钟梳头穿鞋，跟着女朋友吃就对了' % self.name)
		else:
			print('%s约会出门前需要两小时化妆更衣，负责吃就对了' % self.name)



def main():
	
	stu1 = Student('小亮', 22, '男')
	stu1.study('php')
	stu1.love()
	stu1.dating()

	stu2 = Student('小欢', 16, '女' )
	stu2.study('python')
	stu2.love()
	stu2.dating()

if __name__ == '__main__':
	main()
