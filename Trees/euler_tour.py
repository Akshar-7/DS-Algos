	def dfs(x,p):
		global c
		c+=1
		tt[x][0] = c
		for v in g[x]:
			if v==p: continue
			dfs(v,x)
		tt[x][1] = c
	
	n = int(input())
	g = [[] for i in range(n+1)]
	for i in range(n-1):
		u,v = map(int, input().split())
		g[u].append(v)
		g[v].append(u)
	c = 0
	tt = [[0]*2 for i in range(n+1)]
	dfs(1,0)
	eu = [0]*(c+1)
	for i in range(1, n+1):
		eu[tt[i][0]] = i
