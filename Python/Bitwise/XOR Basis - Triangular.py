lg = 32
def insert(x, j = -1):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    if b[i]==0:
      b[i] = x; d[i] = j
      #m[i] = mask^(1<<i)
      return 1
    x ^= b[i]; #mask ^= m[i]
  return 0

def query(x):
  #mask = 0
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    x ^= b[i]; #mask ^= m[i]
  return x==0

def maxxor(x):
  #mask = 0
  for i in range(lg - 1, -1, -1):
    if x < x^b[i]:
      x ^= b[i]; #mask ^= m[i]
  return x
# Returns the k-th smallest XOR [1, 2^sz]
def lexk(k):
  res = 0
  sz = sum((1*(x>0) for x in b))
  ttl = 1<<sz
  if k>ttl: return -1
  for i in range(lg-1, -1, -1):
    if b[i]==0: continue
    ttl >>=1
    bit = res&1<<i
    if (k<=ttl and bit) or (k>ttl and not bit):
      res ^= b[i]
    if k>ttl: k -=ttl
  return res
# Returns the no of distinct XOR < x
def cntl(x):
  ans = res = 0
  sz = sum((1*(x>0) for x in b))
  for i in range(lg-1, -1, -1):
    if b[i]>0:
      sz -=1
      if x&1<<i:
        ans += (1<<sz)
        if res&1<<i==0: res ^= b[i]
      elif res&1<<i: res ^= b[i]
    else:
      bx = x&1<<i
      br = res&1<<i
      if bx > br: return ans + (1<<sz)
      elif bx != br: return ans
  return ans
