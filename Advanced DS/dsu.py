def find(x):
  if x==p[x]: return x
  p[x] = find(p[x])
  return p[x]

def union(x, y):
  x, y = find(x), find(y)
  if x==y: return 0
  if sz[x]<sz[y]: x,y = y,x
  p[y] = x
  sz[x] += sz[y]
  return 1

p = [i for i in range(n+1)]
sz = [1]*(n+1)
