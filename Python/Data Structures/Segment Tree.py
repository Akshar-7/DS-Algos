# Under Testing
class Node():
  __slots__ = ['x', 'i', 'lazy']
  def __init__(self):
    self.x = 10**9+1; self.i = 0; self.lazy = 0
  def __repr__(self):
    return f"Node(x:{self.x}, i:{self.i}, lazy:{self.lazy})"

def copy(a):
  res = assign(a.x, a.i)
  return res

def merge(a, b):
  res = copy(a)
  if a.x > b.x: res = copy(b)
  return res

def assign(x, i):
  res = Node()
  res.x = x
  res.i = i
  return res

def apply(i, val):
  t[i].x += val
  if i<N: t[i].lazy += val

def build(a):
  global N, H
  n = len(a)
  N = 1; H = 0
  while N<n:  # N= 2^x & N>= n
    N *=2; H +=1
  t = [Node() for _ in range(2*N)]
  for i in range(n):
    t[N+i] = assign(a[i], i)
  for i in range(N-1, 0, -1):
    t[i] = merge(t[i<<1], t[i<<1 |1])
  return t

def push(t, p):
  for s in range(h, 0, -1):
    i = p >> s
    if t[i].lazy != 0:
      apply(i<<1, t[i].lazy)
      apply(i<<1|1, t[i].lazy)
      t[i].lazy = 0

def propagate(t, p):
  while p>1:
    p>>=1
    t[p].x = merge(t[p<<1], t[p<<1 |1]).x +t[p].lazy

# [l, r)
def update_rng(t, l, r, v):
  l +=N; r +=N
  l0,r0 = l,r
  push(t, l); push(t, r-1)  # NEW
  while l<r:
    if l&1==1:
      apply(l, v)
      l +=1
    if r&1==1:
      r-=1
      apply(r, v)
    l>>=1; r>>=1
  propagate(t, l0)
  propagate(t, r0-1)

def update(t, i, v):
  i +=N
  t[i] = assign(v, i-N)
  while i>1:
    i //=2
    t[i] = merge(t[i<<1], t[i<<1 |1])
# [l, r)
def query_rng(t, l, r):
  l +=N; r +=N
  push(t, l); push(t, r-1)  # NEW
  ansL = Node(); ansR = Node()
  while l<r:
    if l&1==1:
      ansL = merge(ansL, t[l])
      l +=1
    if r&1==1:
      r-=1
      ansR = merge(t[r], ansR)
    l>>=1; r>>=1
  return merge(ansL, ansR)
# [l, r]
def query_idx(t, l, r, k):
  L, R = 0, N-1
  s = [(1, L, R)]
  while s:
    i,L,R = s.pop()
    if t[i].x < k: continue
    if R<l or L>r: continue
    if L==R:
      return L
    mid = (L+R)//2
    if not(R<l or mid+1>r) and t[i<<1|1].x >= k:
      s.append((i<<1|1, mid+1, R))
    if not(mid<l or L>r) and t[i<<1].x >= k:
      s.append((i<<1, L, mid))
  return -1
