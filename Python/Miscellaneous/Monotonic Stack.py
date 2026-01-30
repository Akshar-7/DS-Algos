# Previous Greater Element
s = []
pg = [-1]*n
for i in range(n-1, -1, -1):
  while s and a[s[-1]] < a[i]:
    j = s.pop()
    pg[j] = i
  s.append(i)
# Next Greater Element
s = []
ng = [n]*n
for i in range(n):
  while s and a[s[-1]] < a[i]:
    j = s.pop()
    ng[j] = i
  s.append(i)
