# Independent Vectors
# Basis does not depend on insertion order
# Maintains minimum basis
# Check equality of basis
# Simple k-th queries (in O(1) using Four Russian)
# Not good for merging / modification

lg = 31
def insert(x):
  for y in b: x = min(x, x^y)
  for i in range(lg): b[i] = min(b[i], b[i]^x)
  if x==0: return 0
  for i in range(lg-1, -1, -1):
    if x&1<<i:
      b[i] = x; return 1

def solve(a, aug = 1):
  """
  Reduces the col-vector augmented matrix (list of ints) in-place returns the rank.
  aug : defines whether the matrix a is augmented or not.
  Time Complexity: O(N * bits).
  """
  n = len(a)
  rank = 0
  for j in range(lg-1, -1, -1):
    pivot = -1
    for i in range(rank, n-aug):
      if a[i]&1<<j:
        pivot = i; break
    if pivot == -1:
      if a[n-1]&1<<j: return -1
      continue
    a[rank], a[pivot] = a[pivot], a[rank]
    for i in range(n):
      if i!=rank and a[i]&1<<j:
        a[i] ^= a[rank]
    rank +=1
  return rank

def lexk(k):
  ans = 0; k-=1  # k starts from 1
  for i in range(lg):
    if k&1<<i:  ans ^= b[i]
  return ans
