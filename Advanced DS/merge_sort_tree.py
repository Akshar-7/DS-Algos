from bisect import bisect_left as bi

def query(l, r, x):
  l +=N; r +=N
  ans = 0
  while l<r:
    if l&1==1:
      j = bi(tree[l], x)
      ans += j
      l +=1
    if r&1==1:
      r-=1
      j = bi(tree[r], x)
      ans += j
    l>>=1; r>>=1
  return ans

N = 1
while N<n: N *=2  # N= 2^x & N>= n
tree = [[] for i in range(2*N)]
b = []
for i in range(n):
  b.append((a[i], i))
b.sort()
for x,j in b:
  j+=N
  while j>0:
    tree[j].append(x)
    j>>=1
