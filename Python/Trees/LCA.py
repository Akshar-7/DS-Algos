def find(x, d):
  for i in range(k):
    if d&1<<i:
      x = p[x][i]
  return x

def lca(u,v):
  if lvl[u]>lvl[v]: u,v = v,u
  d = lvl[v]-lvl[u]
  v = find(v, d)
  if u==v: return u
  for m in range(k-1,-1,-1):
    pu, pv = p[u][m], p[v][m]
    if pu!=pv:
      u,v = pu,pv
  return p[u][0]

k = 0
while (1<<k)<=n: k+=1
p = [[0]*k for i in range(n+1)]
lvl = [0]*(n+1)
s = [(1,0)]
while s:
  x,par = s.pop()
  lvl[x] = lvl[par]+1
  p[x][0] = par
  for i in range(1,k):
    p[x][i] = p[p[x][i-1]][i-1]
  for v in g[x]:
    if v==par: continue
    s.append((v,x))
