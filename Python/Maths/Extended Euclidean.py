def gcd(a, b):
  if b==0:
    return a,1,0
  g,x1,y1 = gcd(b, a%b)
  x = y1
  y = x1 -y1*(a//b)
  return g,x,y
