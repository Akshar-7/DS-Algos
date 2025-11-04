def gcd(a, b):
  if (b == 0):
    x, y = 0, 1
    return a
  d, x1, y1 = gcd(b, a %b)
  x = y1
  y = x1 -y1 *(a /b)
  return d, x, y
