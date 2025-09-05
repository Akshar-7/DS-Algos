	def sum(i):
		res = 0
		while i>0:
			res += t[i]
			i -= (i&-i)
		return res
	
	def update(i,x):
		while i<=n:
			t[i] += x
			i += (i&-i)
	
	n = len(a)
	a = [int(i) for i in input().split()]
	t = [0]*(n+1)
	for i in range(n): t[i+1] = a[i]
	for i in range(1, n):
		p = i + (i&-i)
		if p<=n:
			t[p] = t[p] + t[i]
