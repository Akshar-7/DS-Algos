def comb(n, r):
  if r>n: return 0
  c = [0]*(n+1)
  c[0] = 1
  for i in range(1, n+1):
    j = min(i, r) 
    while(j>0):
      c[j] = (c[j] + c[j-1]) %p
      j -=1
  return c[r]

def lucas(n, r, p):
  if r==0: return 1
  ni = n%p
  ri = r%p
  return lucas(n//p, r//p, p) * comb(ni, ri, p) %p
