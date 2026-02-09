# Top-Right
tr = [[0]*(m+2) for _ in range(n+2)]
for i in range(n):
  curr = tr[i+1]
  prev = tr[i]
  row = a[i]
  for j in range(m-1, -1, -1):
    curr[j+1] = (curr[j+2] + prev[j+1] - prev[j+2] + row[j])

# Top-Left
tl = [[0]*(m+2) for _ in range(n+2)]
for i in range(n):
  curr = tl[i+1]
  prev = tl[i]
  row = a[i]
  for j in range(m):
    curr[j+1] = (curr[j] + prev[j+1] - prev[j] + row[j])

# Bottom-Right
br = [[0]*(m+2) for _ in range(n+2)]
for i in range(n-1, -1, -1):
  curr = br[i+1]
  prev = br[i+2]
  row = a[i]
  for j in range(m-1, -1, -1):
    curr[j+1] = (curr[j+2] + prev[j+1] - prev[j+2] + row[j])

#Bottom-Left
bl = [[0]*(m+2) for _ in range(n+2)]
for i in range(n-1, -1, -1):
  curr = bl[i+1]
  prev = bl[i+2]
  row = a[i]
  for j in range(m):
    curr[j+1] = (curr[j] + prev[j+1] - prev[j] + row[j])
