n = 100
p = []
pr = [1]*(n+1)
phi = [0]*(n+1)
phi[1]=1
for i in range(2,n):
  if pr[i]:
    p.append(i); phi[i] = i-1
  for x in p:
    if i*x>n: break
    pr[i*x] = 0
    if i%x==0:
      phi[i*x] = phi[i]*x
      break
    else:
      phi[i*x] = phi[i]*phi[x]
