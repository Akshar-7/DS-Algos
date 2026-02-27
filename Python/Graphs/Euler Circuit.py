def euler(x, k=-1):
  ans = []
  s = [(x,k)]
  while s:
    u,k = s[-1]
    if g[u]:
      v,j = g[u].pop()
      g[v].discard((u,j))
      s.append((v,j))
    else:
      u,k = s.pop()
      ans.append(u)
      #idx.append(k)
  return ans[::-1]
