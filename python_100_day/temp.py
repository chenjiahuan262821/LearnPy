x = float(input('请输入x值:'))
if x>1 :
    y = 3*x-5
elif x>-1 :
    y = x+2
else :
    y = 5*x+3
print('x值%.2f所对应的y值为%.2f' % (x,y))
