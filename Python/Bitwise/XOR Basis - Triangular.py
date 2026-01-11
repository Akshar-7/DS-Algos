lg = 32
def insert(x, j):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    if b[i]==0:
      b[i] = x; d[i] = j
      #m[i] = mask^(1<<i)
      return 1
    #mask ^= m[i]
    x ^= b[i]
  return 0

def query(x):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    x ^= b[i]
    #mask ^= m[i]
  return x==0

def lexk(k):
  res = 0
  ttl = 1<<len(b)
  for i in range(lg-1, -1, -1):
    if b[i]==0: continue
    ttl >>=1
    bit = res&1<<i
    if (k<=ttl and bit) or (k>ttl and not bit):
      res ^= b[i]
    if k>ttl: k -=ttl
  return res
