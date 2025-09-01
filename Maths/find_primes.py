N = 10**6+1
pr = [1]*N
p = 2
while p*p<N:
	if pr[p]:
		for i in range(2*p, N, p):
			pr[i]=0
	p+=1
