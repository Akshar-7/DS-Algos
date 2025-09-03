import heapq
def djk(x):
  d = [10*18]*(n+1); d[x]=0
  h = [(0,x)]
  while h:
    dx,x = heapq.heappop(h)
    if dx!=d[x]: continue
    for v,w in g[x]:
      if d[v]>d[x]+w:
        d[v]=d[x]+w
        heapq.heappush(h, (d[v],v))
