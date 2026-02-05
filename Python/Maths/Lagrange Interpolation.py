# Problem: https://codeforces.com/contest/622/problem/F
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
  # Degree of poly = k+1
  szy = len(y) # Degree of poly + 1
  if n <= k+1: return y[n]
  # Calc Factorials and its Inverses upto Degree of Poly
  pre = [1] *szy
  suf = [1] *szy
  curr = 1
  for i in range(szy):
    curr = (curr *(n-i)) %mod
    pre[i] = curr
  curr = 1
  for i in range(szy-1, -1, -1):
    curr = (curr *(n-i)) %mod
    suf[i] = curr
  ans = 0
  for i in range(1, szy):
    num = pre[i-1]
    if i < k+1:
      num = (num *suf[i+1]) %mod
    den = (fr[i] *fr[k+1-i]) %mod
    sign = -1 if ((k+1 -i) % 2) else 1
    term = y[i] *num *den %mod
    ans = (ans + sign*term) %mod
  return ans
