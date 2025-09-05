  def update(i, v):
    i +=N
    t[i] = v
    while i>1:
      i //=2
      t[i] = max(t[2*i], t[2*i+1])
  
  def query(l, r):
    l +=N; r +=N
    ans = 0
    while l<r:
      if l&1==1:
        ans = max(ans, t[l])
        l +=1
      if r&1==1:
        r-=1
        ans = max(ans, t[r])
      l>>=1; r>>=1
    return ans
  
  N = 1
  while N<n: N *=2  # N= 2^x & N>= n
  t = [0]*2*N
