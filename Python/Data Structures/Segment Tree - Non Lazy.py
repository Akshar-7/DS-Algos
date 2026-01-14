DEF = 0
def merge(a, b):
  return a+b

def build(a):
  global N
  n = len(a)
  N = 1
  while N<n:  # N= 2^x & N>= n
    N *=2
  t = [DEF for _ in range(2*N)]
  for i in range(n):
    t[N+i] = a[i]
  for i in range(N-1, 0, -1):
    t[i] = merge(t[i<<1], t[i<<1 |1])
  return t

def update(t, i, v):
  i +=N
  t[i] = v
  while i>1:
    i >>=1
    t[i] = merge(t[i<<1], t[i<<1 |1])
# [l, r)
def query_rng(t, l, r):
  l +=N; r +=N
  ansL = ansR = DEF
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
    if L==R:  return L
    mid = (L+R)//2
    if not(R<l or mid+1>r) and t[i<<1|1].x >= k:
      s.append((i<<1|1, mid+1, R))
    if not(mid<l or L>r) and t[i<<1].x >= k:
      s.append((i<<1, L, mid))
  return -1
