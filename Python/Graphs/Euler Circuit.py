def euler(x):
    ans = []
    s = [x]
    while s:
      u = s[-1]
      if g[u]:
        v,j = g[u].pop()
        g[v].discard((u,j))
        s.append(v)
      else:
        ans.append(s.pop() +1)
    return ans
