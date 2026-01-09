# For range :-  0, 1, 2, ..., 2^n -1

a = []
for i in range(1<<n):
  cnt=0; x=i
  while x:
    cnt+=1; x=x&(x-1)
  if cnt==k: a.append(i)
b = [0]*logk; base=0
d = [0]*logk
for j in range(len(a)):
  x = a[j]
  for i in range(logk-1,-1,-1):
    if x&1<<i==0: continue
    if b[i]==0:
      b[i]=x; d[i]=j
      base+=1; break
    x^=b[i]
for i in range(logk):
  b[i] = a[d[i]]
if base==n:
  ans = [0]
  for i in range(base):
    for j in range((1<<i)-1, -1, -1):
      ans.append(ans[j]^b[i])
else:
  # NOT POSSIBLE
