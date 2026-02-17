def dfs(x):
  while g[x]:
    v = g[x].pop()
    g[v].remove(x)
    yield dfs(v)
  ans.append(x+1)
  yield 0

cod = 0
for x in dg: cod += x&1
if cod!=0:# and cod!=2:
  print("IMPOSSIBLE")

st = 0
for i in range(n):
  if dg[i]&1:
    st = i; break
ans = []
dfs(st)
if len(ans)<m+1: print("IMPOSSIBLE")
else: print(*ans)
