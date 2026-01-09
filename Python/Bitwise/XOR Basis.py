lg = 32
def insert(x, j):
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    if b[i]==0:
      b[i] = x; d[i] = j
      break
    x ^= b[i]

def query(x):
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    x ^= b[i]
  return x==0

