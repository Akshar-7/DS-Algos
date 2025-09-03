N = 10**6
pr = [1]*(N+1)
for p in range(2, N+1):
	if p*p>N: break
	if pr[p]==0: continue
	for i in range(p*p, N, p):
		pr[i]=0
