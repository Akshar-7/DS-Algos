mod = 10**9 +7
def init(k):
  y = [0]  # Initializing with y(0)
  curr = 0
  # Calculating all y(i)'s
  for i in range(1, k + 2):
    term = pw(i, k, mod)
    curr = (curr + term) %mod
    y.append(curr)
  return y

def get(n, k, y):
  szy = len(y) # Degree of poly + 1
  if n <= k+1: return y[n]
  ans = 0
  cur = 1  # Creating G(0)
  for i in range(1, szy):
    cur = (cur *(n-i)) %mod
    cur = (cur *pw(-i, mod-2, mod)) %mod
  # Calc 'ans' & Transition from G(i) to G(i+1)
  for i in range(szy):
    ans = (ans + cur*y[i]) %mod
    if i == k+1: break
    cur = (cur *(n-i)) %mod
    cur = (cur *pw(n -(i+1), mod-2, mod)) %mod
    cur = (cur *(i -(k+1))) %mod
    cur = (cur *pw(i+1, mod-2, mod)) %mod
  return (ans +mod) %mod
