def phi(n):
  ans = n
  for i in range(2, n+1):
    if i*i > n: break
    if n%i==0:
      while n%i==0: n//=i
      ans -= ans//i
  if n>1:
    ans -= ans//n
  return ans
