x,y,z=1,1,1
print('X+2 :','	 X*2 :')
for i in range(9):
	print(x,"	",y)
	y=y*2
	x=x+2
print('----------------------')
print('num :','	 hex : ',' bin :','	 morse :')
e = int(input('make choices : '))
for i in range(pow(2,e)):
	z=i
	a = str(bin(z)[2:])
	a = a.replace('0','_')
	a = a.replace('1','-')
	print(z,'	',hex(z)[2:],'	',bin(z)[2:],'	',a)
