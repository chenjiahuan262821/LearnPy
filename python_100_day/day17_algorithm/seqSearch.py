
'''初步版'''

def seqSearch_single(items, key):
	for index, item in enumerate(items):
		if item == key:
			return index
	return -1


a = [8,9,7,6,5,4,8]
print(seqSearch_single(a, 8)) #只返回了0


'''升级版'''

def seqSearch_multi(items, key):
	loc = []
	for index, item in enumerate(items):
		if item == key:
			loc.append(index)
	if loc != []:
		return loc
	else:
		return -1

a = [8,9,7,6,5,4,8]
print(seqSearch_multi(a, 8))  # 返回[0, 6]