n = 100
p = []
pr = [1]*(n+1)
mobius = [0]*(n+1)
mobius[1]=1
for i in range(2,n):
  if pr[i]:
    p.append(i); mobius[i] = -1
  for x in p:
    if i*x>n: break
    pr[i*x] = 0
    if i%x==0:
      mobius[i*x] = 0
      break
    else:
      mobius[i*x] = mobius[i]*mobius[x]
