from collections import deque
from random import randint as ri
MX = (1<<60) -1
K = 3
hval = [0]*(n+1)
for i in range(n+1):
  hval[i] = ri(1, MX)
fq = [0]*(n+1)  # Storing freq of each element
f = {0:1}
idx = [deque([]) for i in range(n+1)]  # For exactly K occurrences of elements type
hsh = [0]*(n+1)  # Storing prefix hashes for each index
ans = l = 0
for i in range(n):
  # Calculating prefix hashes for each index while keeping the conditions satisfied.
  x = a[i]
  bef = fq[x]
  while len(idx[x]) >= K:
    pi = idx[x].popleft()
    while l<=pi:  # before prefix starts at l-th hash, now it starts with the pi-th hash which is the prefix hash of pi-th index
      f[hsh[l]] -=1
      l+=1
  idx[x].append(i)
  fq[x] = (fq[x] + 1) % K
  hsh[i+1] = (hsh[i] + (fq[x]-bef)*hval[x]) & MX  # Taking modulus with bitwise AND
  ans += f.get(hsh[i+1], 0)
  f[hsh[i+1]] = f.get(hsh[i+1], 0) +1
print(ans)  # Total no. of subarrays
