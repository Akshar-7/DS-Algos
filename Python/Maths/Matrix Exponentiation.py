mod = 998244353
def prod(a, b):
  n = len(a)
  c = [[0]*n for i in range(n)]
  for i,ci in enumerate(c):
    for k,aik in enumerate(a[i]):
      for j,bkj in enumerate(b[k]):
        ci[j] = (ci[j] + aik*bkj) %mod
  return c

def mpw(a, y):
  res = [[0]*len(a) for x in a]
  for j,resi in enumerate(res): resi[j]=1
  while y:
    if y&1:
      res = prod(res, a)
    a = prod(a, a)
    y >>=1
  return res
