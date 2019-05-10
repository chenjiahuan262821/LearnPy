from random import randint

def roll_dice(n=2):
	tot = 0
	for _ in range(n):
		tot += randint(1,6)
	return tot

def add(a =0, b=0, c=0):
	return a+b+c

print(roll_dice())   #按照默认值n=2
print(roll_dice(6)) #传递了参数n=6

print(add())
print(add(1,2))
print(add(1,2,3)) #需要按照设定的顺序进行传递
print(add(a=10, c=30, b=20)) #传递参数可以不按照设定的顺序进行传递

# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add_new(*args):
    tot = 0
    for val in args:
        tot += val
    return tot
print(add_new(1,2,3,4,5,6,7,8))

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()