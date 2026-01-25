N = 3*10**5
f = [[] for i in range(N+1)]
for i in range(2, N+1):
  for j in range(i*i, N+1, i):
    f[j].append(i)
    if i*i!=j:
      f[j].append(j//i)
