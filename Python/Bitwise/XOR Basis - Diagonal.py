# Independent Vectors
# Basis does not depend on insertion order
# Maintains minimum basis
# Check equality of basis
# Simple k-th queries (in O(1) using Four Russian)
# Not good for merging / modification

sz = 0
def insert(x):
  global sz
  for y in b:
    x = min(x, x^y)
  for i in range(sz):
    b[i] = min(b[i], b[i]^x)
  if x==0: return 0
  b.append(x); sz+=1
  for i in range(sz-1,0,-1):
    if b[i]<b[i-1]:
      b[i],b[i-1] = b[i-1],b[i]
  return 1

def query(x):
  for y in b:
    x = min(x, x^y)
  return x==0

def lexk(k):
  k-=1  # k starts from 1
  ans = 0
  for i in range(sz):
    if k&1<<i:
      ans ^= b[i]
  return ans
