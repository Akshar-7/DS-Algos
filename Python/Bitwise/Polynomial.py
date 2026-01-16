def msb(n):
  return n.bit_length()-1 if n>0 else -1

def add(a, b):
  return a^b

def mul(a, b):
  res = 0
  while b>0:
    if b&1:  res ^= a
    a <<=1; b >>=1
  return res

def divmod(a, b):
  if b==0: return -1
  dga = msb(a); dgb = msb(b)
  qut = 0; rem = a
  for i in range(dga - dgb, -1, -1):
    if (rem >> (i + dgb)) &1:
      qut |= (1<<i)
      rem ^= (b<<i)
  return qut, rem

def gcd(a, b):
  if b>a: a,b = b,a
  while b>0:
    shift = msb(a) - msb(b)
    a ^= (b << shift)
    if b>a: a,b = b,a
  return a
