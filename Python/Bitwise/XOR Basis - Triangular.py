lg = 32
def insert(x, j):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    if b[i]==0:
      b[i] = x; d[i] = j
      #m[i] = mask^(1<<i)
      break
    #mask ^= m[i]
    x ^= b[i]

def query(x):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    x ^= b[i]
    #mask ^= m[i]
  return x==0

