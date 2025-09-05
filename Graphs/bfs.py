from collections import deque
  def bfs(x):
    d = [10*18]*(n+1); d[x]=0
    q = deque([(0,x)])
    while q:
      dx,x = q.popleft()
      if dx!=d[x]: continue
      for v in g[x]:
        if d[v]>d[x]+1:
          d[v]=d[x]+1
          q.append((d[v],v))
