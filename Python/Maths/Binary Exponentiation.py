def pw(x,y,m):
	res=1
	while y:
		if y&1: res=(res*x)%m
		x = (x*x)%m
		y >>=1
	return res
