d = []
for i in range(n+1):
  b = [[10**18]*(n+1) for i in range(n+1)]
  d.append(b)
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      d[i][j] = min(d[i][j], d[i][k]+d[k][j])
