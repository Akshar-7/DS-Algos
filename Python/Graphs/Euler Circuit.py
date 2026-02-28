# Uncomment lines for undirected graph
# Use list of lists to store edges not sets

def euler(x):
  ans = []
  #vis = [False]*m
  s = [(x, 0)]
  while s:
    u,k = s[-1]
    #while g[u] and vis[g[u][-1][1]]: g[u].pop()
    if g[u]:
      vj = g[u].pop()
      #vis[vj[1]] = True
      s.append(vj)
    else:
      y,k = s.pop()
      ans.append(y)
      #idx.append(k)
  return ans
