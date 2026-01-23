def find(x, d):
  for i in range(k):
    if d&1<<i:
      x = p[i][x]
  return x

def lca(u,v):
  if lvl[u]>lvl[v]: u,v = v,u
  d = lvl[v]-lvl[u]
  v = find(v, d)
  if u==v: return u
  for m in range(k-1,-1,-1):
    pu, pv = p[m][u], p[m][v]
    if pu!=pv:
      u,v = pu,pv
  return p[0][u]

k = 0
while (1<<k)<=n: k+=1
p = [[0]*(n+1) for i in range(k)]
lvl = [0]*(n+1)
s = [(1,0)]
while s:
  x,par = s.pop()
  lvl[x] = lvl[par]+1
  p[0][x] = par
  for i in range(1,k):
    p[i][x] = p[i-1][p[i-1][x]]
  for v in g[x]:
    if v==par: continue
    s.append((v,x))
