#1 TODO : Add Lazy Propagation
#2 Under Construction
#3 The Added Lazy methods are wrong for iterative. Fix that
class Node():
  __slots__ = ['x', 'i', 'lazy']
  def __init__(self):
    self.x = 10**9+1; self.i = 0; self.lazy = 0
  def __repr__(self):
    return f"Node(x:{self.x}, i:{self.i}, lazy:{self.lazy})"

def copy(a):
  res = assign(a.x, a.i)
  return res

def func(a, b):
  res = copy(a)
  if a.x > b.x: res = copy(b)
  return res

def assign(x, i):
  res = Node()
  res.x = x
  res.i = i
  return res
# NOT TESTED
def apply(i, val):
  t[i].x += val
  if i<N: t[i].lazy += val

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
# Need some work here # [l, r]
def update_rng(t, l, r, v):
  l +=N; r +=N
  while l<r:
    if l&1==1:
      t[l] = func(t[l], v)
      l +=1
    if r&1==1:
      r-=1
      t[r] = func(t[r], v)
    l>>=1; r>>=1
# NOT TESTED
def propagate(t, i):
  if t[i].lazy != 0 and i < N:
      t[i<<1].lazy += t[i].lazy
      t[i<<1 |1].lazy += t[i].lazy
			t[i].lazy = 0

def update(t, i, v):
  i +=N
  t[i] = assign(v, i-N)
  while i>1:
    i //=2
    t[i] = func(t[i<<1], t[i<<1 |1])
# [l, r)
def query_rng(t, l, r):
  l +=N; r +=N
  ansL = Node(); ansR = Node()
  while l<r:
    if l&1==1:
      propagate(t, l)  # NEW
      ansL = func(ansL, t[l])
      l +=1
    if r&1==1:
      r-=1
      propagate(t, r)  # NEW
      ansR = func(t[r], ansR)
    l>>=1; r>>=1
  return func(ansL, ansR)
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
