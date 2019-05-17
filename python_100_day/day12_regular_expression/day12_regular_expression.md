# Python100 - Day12
## 正则表达式

### 基础介绍：

> 在编写处理字符串的程序或网页时，经常会有**查找符合某些复杂规则的字符串**的需要。正则表达式就是用于**描述这些规则**的工具，就是记录文本规则的代码。
> 
> 假设在一篇英文小说里查找hi，可以使用正则表达式hi。通常，处理正则表达式的工具会提供一个忽略大小写的选项，如果选中了这个选项，它可以匹配hi,HI,Hi,hI这四种情况中的任意一种。不幸的是，很多单词里包含hi这两个连续的字符，比如him,history,high等等。如果要精确地查找hi这个单词的话，我们应该使用\bhi\b。
> 


| 符号 | 解释 | 示例 | 说明 |
| :------:| :------: | :------: | :------: |
| . | 匹配任意字符 | b.t | bat but b#t b_t b1t |
| \w | 匹配字母/数字/下划线 | b\wt | bat b_t b1t 但不能b#t |
| \W | 匹配非字母/数字/下划线 | b\Wt | b#t b't |
| \s | 匹配空白字符（包括\r、\n、\t）| love\syou | love you |
| \S | 匹配非空白字符| love\Syou | love_you love%you |
| \d | 匹配数字 | \d\d | 66 06 08 18 |
| \D | 匹配非数字 | \d\D | 6* 6% 8& 9_ |
| \b | 匹配单词边界 | \bThe\b | 精确匹配The |
| \B | 匹配非单词边界 | \Bhe\B | 可以匹配there |
| ^ | 匹配字符串的开始 | ^The | 可以匹配The开头的，如There |
| $ | 匹配字符串的结束 | .py$ | 可以匹配.py结尾的，如exp.py |
| [] | 匹配来自字符集的任意单一字符 | [aeiou] | 可以匹配a、e、... |
| [^] | 匹配不在字符集的任意单一字符 | [^aeiou] | 匹配t、p、...|
| * | 匹配0次或多次 | a.*b | 应用于aabab会得到aabab
| + | 匹配1次或多次 | \w+ |
| ? | 匹配0次或1次 | \w? |
| {N} | 匹配N次 | \w{3} |
| {M,} | 匹配至少M次 | \w{3,} |
| {M,N} | 匹配至少M次至多N次 | \w{3,6} |
| *? | 重复任意次，但尽可能少重复 | a.*?b |应用于aabab会得到aab与ab两个字符串
| +? | 重复1次或多次，但尽可能少重复 |
| ?? | 重复0次或1次，但尽可能少重复 |
| {M,N}? | 重复M到N次，但尽可能少重复 |
| {M,}? | 重复M次以上，但尽可能少重复 |
| l | 分支 |   |可以匹配foo或者bar |
| (?#) | 注释 |
| (str) | 匹配字符str并捕获到自动命名的组中 |
| (?<name>str) | 匹配字符str并捕获到名为name的组中 |
| (?:str) | 匹配字符str但是不捕获匹配的文本 |
| (?=str) | 匹配str前面的位置 | \b\w+(?=ing) | 匹配I'm dancing中的danc
| (?<=str) | 匹配str后面的位置 | (?<=\bdanc)\w+\b | 可以匹配I love dancing and reading中的第一个ing
| (?!str) | 匹配后面不是str的位置 |
| (?<!str) | 匹配前面不是str的位置 |

> 如果需要匹配的字符是正则表达式中的特殊字符，那么可以使用\进行转义处理。例如，想匹配小数点可以写成\.的样子，因为直接写.会匹配任意字符；同理，想匹配圆括号必须写成\(和\)，否则圆括号被视为正则表达式中的分组。

### Python对正则表达式的支持：

Python提供了re模块，支持正则表达式操作~

+ compile(pattern, flags=0)，编译正则表达式返回正则表达式对象
+ match(pattern, string, flags=0)，用正则表达式匹配字符串，成功返回匹配对象，否则返回None
+ search(pattern, string, flags=0)，搜索字符串中第一次出现正则表达式的模式，成功返回匹配对象，否则返回None
+ split(pattern, string, maxsplit=0, flags=0)，用正则表达式指定的模式分隔符拆分字符串，返回列表
+ sub(pattern, repl, string, count=0, flags=0)，用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
+ fullmatch(pattern, string, flags=0)，match函数的完全匹配（从字符串开头到结尾）版本
+ findall(pattern, string, flags=0)，查找字符串所有与正则表达式匹配的模式，返回字符串的列表
+ finditer(pattern, string, flags=0)，查找字符串所有与正则表达式匹配的模式，返回一个迭代器
+ purge()，清除隐式编译的正则表达式的缓存
+ re.I / re.IGNORECASE，忽略大小写匹配标记
+ re.M / re.MULTILINE，多行匹配标记

> 如果一个正则表达式需要重复的使用，那么可以先通过compile函数编译正则表达式并创建出正则表达式对象。

#### 验证输入用户名和账号是否有效，match函数的使用

	import re

	def main():
	
		username = input('请输入用户名：')
		account = input('请输入账号：')
	
		#用户名必须由字母、数字或下划线构成且长度在6~10个字符之间
		m1 = re.match(r'^[0-9a-zA-Z_]{6,10}$', username)
	
		#账号是6~16的数字且首位不能为0
		m2 = re.match(r'^[1-9]\d{5,15}$', account)
	
		if not m1:
			print('请输入有效用户名')
		if not m2:
			print('请输入有效账号')
		if m1 and m2:
			print('你输入的信息是有效的')

	if __name__ == '__main__':
		main()


> 在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r），字符串中的每个字符都是它原始的意义，没有转义字符

#### 从一段文字中提取出国内手机号码，compile函数、findall与finditer

截止到2017年底，国内三家运营商推出的手机号段:

+ 电信号：133 153 180 181 189 177
+ 联通号：130 131 132 155 156 185 145 176
+ 移动号：134 135 136 137 138 139 150 151 152 157 158 159 182 183 184 187 188 147 178

注意像14开头的号码只有145或147、15开头是150-153及155-159

	import re

	def main():

		# 使用前瞻(?<=\D)和回顾(?=\D)来保证手机号前后不应该出现数字
		pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')

		sentence = '''
    	重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    	不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    	'''

		# 查找所有匹配并保存到一个列表中
		phone_list = re.findall(pattern, sentence)
		print(phone_list)
		print('------')
	
		# 通过迭代器取出匹配对象并获得匹配的内容
		for temp in pattern.finditer(sentence):
			print(temp.group())
		print('------')
	
		# 通过search函数指定搜索位置找出所有匹配
		m = pattern.search(sentence)
		while m:
			print(m.group())
			m = pattern.search(sentence, m.end())
		print('------')
	
	if __name__ == '__main__':
    	main()

#### 替换字符串中的不良内容，sub函数

re模块的正则表达式相关函数中都有一个flags参数，它代表了正则表达式的匹配标记，可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。

	import re

	def main():
	    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
	    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
	                      '*', sentence, flags=re.IGNORECASE)
	    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

	if __name__ == '__main__':
	    main()

#### 拆分长字符串，split函数

	import re

	def main():
		poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
		sentence_list = re.split(r'[,.，。]', poem)
		print(sentence_list)
		#['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']

		while '' in sentence_list:
			sentence_list.remove('')
		print(sentence_list)
		#['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

	if __name__ == '__main__':
		main()


---

更多参考：[正则表达式30分钟入门教程](https://deerchao.net/tutorials/regex/regex.htm)