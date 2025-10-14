# FOR GRAPHS
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

# FOR MATRICES
  dr = [(0,1), (0,-1), (1,0), (-1,0)]
  while q:
    i,j = q.popleft()
    for dx,dy in dr:
      x,y = i+dx, j+dy
      if 0<=x<n and 0<=y<m and a[x][y]=='.' and b[i][j]+1<b[x][y]:
        b[x][y] = b[i][j]+1
        q.append((x,y))
