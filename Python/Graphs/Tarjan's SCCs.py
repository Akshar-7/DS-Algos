def scc_dfs(x):
  global t
  stk.append(x); instack[x]=1
  tt[x] = low[x] = t
  t+=1
  for v in g[x]:
    if tt[v]==-1:
      scc_dfs(v,x)
      low[x] = min(low[x], low[v])
    elif instack[v]:
      low[x] = min(low[x], tt[v])
  if low[x]==tt[x]:
    scc = []
    while stk:
      y = stk.pop()
      scc.append(y); instack[y]=0
      if y==x: break
    sccs.append(scc)

# Take Graph I/P
t = 0
sccs = []
tt = [-1]*(n+1)
low = [-1]*(n+1)
instack = [0]*(n+1)
stk = []
for i in range(1,n+1):
  if tt[i]==-1:
    dfs(i)
print(sccs)
