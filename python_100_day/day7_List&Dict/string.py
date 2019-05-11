'''
常见的字符串的操作

计算字符串的长度len()、使字符串首字母大写capitalize()、使字符串全部字母大写upper()、
查找子串所在的位置find()、检查字符串是否以指定的字符串开头或结尾startswith()与endswith()、
字符串的切片[:]、检查是否由数字构成isdigit()、检查是否由字母构成isalpha()、检查是否由数字和字母共同构成isalnum()、
修剪左右两侧空格strip()

'''

str1 = 'hello, world!'
str2 = 'abcdef123456'
str3 = '  joyce@163.com '

print(len(str1))  # 13
print(str1.capitalize())  # Hello, World!
print(str1.upper())  # HELLO WORLD!
print(str1.find('or'))  # 8
print(str1.find('hi'))  # -1，找不到就返回-1
print(str1.startswith('He')) # False
print(str1.startswith('hel'))  # True
print(str1.endswith('!')) # True

print(str2[1]) # 注意python从0开始，所以b
print(str2[1:6]) # bcdef
print(str2.isdigit()) # False
print(str2.isalpha()) # False
print(str2.isalnum()) # True

print(str3.strip()) # 修剪左右两侧空格，joyce@163.com