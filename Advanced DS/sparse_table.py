	def query(l, r):
		x = dp[r-l+1]
		return gcd(st[x][l], st[x][r-(1<<x)+1])
	
	def query2(l, r):
	  res = a[l]
	  for i in range(k-1, -1, -1):
	    if (r-l+1)< 1<<i: continue
	    res = gcd(res, st[i][l])
	    l += (1<<i)
	  return res
	
	dp = [0]*(n+1)
	for i in range(2,n+1):
		dp[i] = 1+dp[i>>1]
	k = dp[n]+1
	st = [[0]*n for i in range(k)]
	st[0] = a.copy()
	for i in range(1,k):
		for j in range(n):
			if j+(1<<i)>n: break
			x = 1<<(i-1)
			st[i][j] = gcd(st[i-1][j], st[i-1][j+x])
