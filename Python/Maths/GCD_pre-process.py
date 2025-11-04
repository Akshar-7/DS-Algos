mx = 20
g = [[0]*(mx+1) for i in range(mx+1)]
for i in range(mx+1): g[i][i] = g[i][0] = g[0][i] = i
for i in range(1, mx+1):
  for j in range(1, i): g[i][j] = g[j][i] = g[j][i%j]
