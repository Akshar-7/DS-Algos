  @bootstrap
  def dfs(x,p):
    nonlocal t
    tt[x] = low[x] = t
    t+=1; vis[x]=1
    for v in g[x]:
      if v==p: continue
      if vis[v]:
        low[x] = min(low[x], tt[v])
      else:
        yield dfs(v,x)
        low[x] = min(low[x], low[v])
        if low[v]>tt[x]:
          bridge.add((x,v)); bridge.add((v,x))
    yield 0
  
  def dfs2(x):
    s = [x]; vis[x]=1
    while s:
      x = s.pop()
      comp[x] = k
      for v in g[x]:
        if vis[v] or (x,v) in bridge: continue
        vis[v]=1
        s.append(v)
  
  bridge = set()
  tt = [0]*(n+1)
  low = [0]*(n+1)
  vis = [0]*(n+1)
  dfs(1,1)
  vis = [0]*(n+1)
  comp = [-1]*(n+1)
  k = 0
  for i in range(1, n+1):
    if vis[i]: continue
    dfs2(i); k+=1
