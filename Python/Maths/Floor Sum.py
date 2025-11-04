# Sum of [n/1] + [n/2] + [n/3] + .... + [n/n]
x = 1
sm = 0
while x<=n:
	y = n//x
	z = n//y
	sm += (z-x+1)*y
	x = z+1
