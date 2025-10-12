# TODO : Add Lazy Propagation
  def func(x, y):
    return max(x, y)

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
    ans = 0
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
  
  N = 1
  while N<n: N *=2  # N= 2^x & N>= n
  t = [0]*2*N
