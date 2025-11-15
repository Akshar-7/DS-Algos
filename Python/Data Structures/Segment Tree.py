#1 TODO : Add Lazy Propagation
#2 Under Construction
class Node():
  __slots__ = ['x', 'i', 'lazy']
  x = 0; i = 0; lazy = 0

def func(a, b):
  res = a
  if a.x < b.x: res = b
  return res

def assign(x, idx):
  res = Node()
  res.x = x
  res.idx = idx
  return res

def build(a):
  global N
  n = len(a)
  N = 1
  while N<n: N *=2  # N= 2^x & N>= n
  t = [Node()]*(2*N)
  for i in range(n):
    t[N+i] = assign(a[i], i)
  for i in range(N-1, 0, -1):
    t[i] = func(t[i<<1], t[i<<1 |1])
  return t

def update_rng(l, r, v):
  l +=N; r +=N
  while l<r:
    if l&1==1:
      t[l] = func(v, t[l])
      l +=1
    if r&1==1:
      r-=1
      t[r] = func(v, t[r])
    l>>=1; r>>=1

def push():
  for i in range(1, n):
    t[i<<1] = func(t[i<<1], t[i])
    t[i<<1|1] = func(t[i<<1|1], t[i])
    t[i] = 10**18

def update(i, v):
  i +=N
  t[i] = v
  while i>1:
    i //=2
    t[i] = func(t[i<<1], t[i<<1 |1])

def query_rng(l, r):
  l +=N; r +=N
  ans = Node()
  while l<r:
    if l&1==1:
      ans = func(ans, t[l])
      l +=1
    if r&1==1:
      r-=1
      ans = func(ans, t[r])
    l>>=1; r>>=1
  return ans
# This is not updated yet
def query2(x):
  i = 1
  while i<N:
    if t[2*i]>=x:
      i = 2*i
    else:
      x -=t[2*i]
      i = 2*i +1
  return i
