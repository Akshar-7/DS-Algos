# Smallest Prime Factor
N = 10**7
spf = list(range(N+1))
primes = []
for i in range(2, N+1):
  if spf[i] == i:
    primes.append(i)
  for p in primes:
    if i*p > N: break
    spf[i*p] = p
    if i%p == 0: break

# Largest Prime Factor
N = 10**7
lpf = list(range(N+1))
primes = []
for i in range(2, N+1):
  if lpf[i] == i:
    primes.append(i)
  for p in primes:
    if i*p > N: break
    lpf[i*p] = lpf[i]
    if i%p == 0: break
