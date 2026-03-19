def query(i):
  res = 0
  while i>0:
    res += t[i]
    i -= (i&-i)
  return res

def update(i,x):
  while i<len(t):
    t[i] += x
    i += (i&-i)

def lower_bound(w):
  x = 0
  n = len(t) -1
  k = 1 << (n.bit_length() -1)
  while k:
    if x+k <= n and t[x+k] < w:
      w -= t[x+k]
      x += k
    k >>=1
  return x+1

t = [0]*(n+1)
for i in range(n): t[i+1] = a[i]
for i in range(1, n):
  p = i + (i&-i)
  if p<=n:
    t[p] = t[p] + t[i]
