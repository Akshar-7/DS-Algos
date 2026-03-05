def pw(x,y,m):
	res=1
	while y:
		if y&1: res=(res*x)%m
		x = (x*x)%m
		y >>=1
	return res

N = 10**5+1
mod = 10**9+7
f = [1]*N
for i in range(2,N):
	f[i] = f[i-1]*i %mod
fr = [1]*N
fr[N-1] = pw(f[N-1], mod-2, mod)
for i in range(N-2, 1, -1):
	fr[i] = fr[i+1]*(i+1) %mod

def comb(n, r):
	if n<0 or n<r: return 0
	return f[n] *fr[r] *fr[n-r] %mod
