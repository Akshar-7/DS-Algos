from collections import deque
  def bipartite(sx):
    s = deque([sx]); vis[sx]=1; clr[sx]=0
    while s:
      x = s.popleft()
      for v in g[x]:
        if vis[v]:
          if clr[v]==clr[x]: return False
          continue
        vis[v]=1; clr[v] = clr[x]^1
        s.append(v)
    return True
  
  clr = [-1]*(n+1)
  vis = [0]*(n+1)
