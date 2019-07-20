def Factorial(n):
	if n == 0 | n == 1:
		return 1
	return Factorial(n-1)*n

# print(Factorial(6))

def Fibonaqi(n):

	if n == 1:
		return 0
	if n == 2:
		return 1
	return Fibonaqi(n-1)+Fibonaqi(n-2)

print(Fibonaqi(30))

