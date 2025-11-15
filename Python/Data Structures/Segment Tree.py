# TODO : Add Lazy Propagation
  default = 0
  def func(x, y):
    return max((x, y))

  def build(a):
    global N
    n = len(a)
    N = 1
    while N<n: N *=2  # N= 2^x & N>= n
    t = [default]*(2*N)
    for i in range(n):
      t[N+i] = a[i]
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
      t[i] = func(t[2*i], t[2*i+1])
  
  def query_rng(l, r):
    l +=N; r +=N
    ans = default
    while l<r:
      if l&1==1:
        ans = func(ans, t[l])
        l +=1
      if r&1==1:
        r-=1
        ans = func(ans, t[r])
      l>>=1; r>>=1
    return ans

  def query2(x):
    i = 1
    while i<N:
      if t[2*i]>=x:
        i = 2*i
      else:
        x -=t[2*i]
        i = 2*i +1
    return i
