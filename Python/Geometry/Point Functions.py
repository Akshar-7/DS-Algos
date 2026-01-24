from functools import cmp_to_key
# key = cmp_to_key(cmp)
def cross(p1, p2):
  x1,y1, x2,y2 = *p1, *p2
  return x1*y2 - y1*x2

bi = {True:-1, False:1}
def cmp(i, j):
  p1, p2 = p[i], p[j]
  x1,y1, x2,y2 = *p1, *p2
  ah = (y1 < 0 or (y1 == 0 and x1 < 0))
  bh = (y2 < 0 or (y2 == 0 and x2 < 0))
  if (ah != bh): return bi[ah < bh];
  return bi[(cross(p1, p2) > 0)]
