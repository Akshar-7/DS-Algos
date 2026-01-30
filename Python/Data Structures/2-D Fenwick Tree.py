def query(i,j):
	res = 0; j0 = j
	while i>0:
	  j = j0
	  while j>0:
  		res += t[i][j]
  		j -= (j&-j)
  	i -= (i&-i)
	return res

def update(i,j,x):
  j0 = j
	while i<=n:
	  j = j0
	  while j<=m:
		  t[i][j] += x
		  j += (j&-j)
		i += (i&-i)

t = [[0]*(m+1) for i in range(n+1)]
