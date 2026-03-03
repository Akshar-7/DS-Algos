N = 5*10**5
token = 0   # Increase on every testcase
par = [0]*(N+1)  # Parent Node
pe = [0]*(N+1)   # Parent Edge ID
vis = [0]*(N+1)

def dfs(u, p=0):
  s = [u]
  vis[u] = token
  order = []
  while s:
    x = s.pop()
    order.append(x)
    # Node Initialization
    for v,i in g[x]:
      if vis[v]==token: continue
      vis[v] = token
      par[v], pe[v] = x, i
      s.append(v)
  for x in reversed(order):
    if x == u: continue   # Skip Root
    px = par[x]   # Parent
    # Logic for Transition b/w Parent and Child
    # when the Child is already processed
