def update(tree, i, v):
  i +=n
  tree[i] = v
  while i>1:
    i //=2
    tree[i] = max(tree[2*i], tree[2*i+1])

def query(tree, l, r):
  l +=n; r +=n
  ans = 0
  while l<r:
    if l&1==1:
      ans = max(ans, tree[l]); l +=1
    if r&1==1:
      r-=1; ans = max(ans, tree[r])
    l>>=1; r>>=1
  return ans

N = 1
while N<n: N *=2  # N= 2^x & N>= n
tree = [0]*2*n
  for i in range(n):
    tree[n+i] = a[i]
  for i in range(n-1, 0, -1):
    tree[i] = max(tree[2*i], tree[2*i+1])
