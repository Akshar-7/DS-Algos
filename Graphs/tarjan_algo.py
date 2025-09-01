def dfs(x,p):
  global t
  stack.append(x); instack[x]=1
  tt[x] = low[x] = t
  t+=1
  for v in g[x]:
    if tt[v]==-1:
      dfs(v,x)
      low[x] = min(low[x], low[v])
    elif instack[v]:
      low[x] = min(low[x], tt[v])
  if low[x]==tt[x]:
    scc = []
    while stack:
      y = stack.pop()
      scc.append(y); instack[y]=0
      if y==x: break
    sccs.append(scc)

n,m = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(m):
  u,v = map(int, input().split())
  g[u].append(v)
t = 0
sccs = []
tt = [-1]*(n+1)
low = [-1]*(n+1)
instack = [0]*(n+1)
for i in range(1,n+1):
  stack = []
  if tt[i]==-1:
    dfs(i,0)
print(sccs)
