# Summation of floor((a*i + b)/m) from 0 to n-1
def floor_sum(n, m, a, b):
  a1, a2 = a //m, a %m
  s = n * (n-1) //2 *a1
  b1, b2 = b //m, b %m
  if a2==0:
    return s + b1 * n
  k = (a2 *(n-1) +b2) //m
  return s +n *(k +b1) -floor_sum(k, a2, m, m +a2 -b2 -1)
