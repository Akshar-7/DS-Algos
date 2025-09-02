a = []
for i in range(n):
  b = [int(i) for i in input().split()]
  a.append(b)
mn = 0-(n-1)
b = [[0]*2*n for i in range(2*n)]
for i in range(n):
  for j in range(n):
    b[i+j+1][i-j-mn+1] = a[i][j]
# Prefix Sum
for i in range(2*n):
  for j in range(1,2*n):
    b[i][j]+=b[i][j-1]
