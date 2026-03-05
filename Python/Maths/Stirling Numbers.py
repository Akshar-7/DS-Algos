# First Kind
N = 5000
mod = 10**9 +7
s = [[0]*(n+1) for i in range(n+1)]
s[0][0] = 1
for i in range(1, n+1):
  for j in range(1, i+1):
    # 1: Place element in its own new cycle -> s[i-1][j-1]
    # 2: Insert into an existing cycle -> (i-1) * s[i-1][j]
    s[i][j] = (s[i-1][j-1] + (i-1)*s[i-1][j]) %mod

# Second Kind
N = 5000
mod = 10**9 +7
S = [[0]*(n+1) for i in range(n+1)]
S[0][0] = 1
for i in range(1, n+1):
  for j in range(1, i+1):
    # 1: Place element in its own new subset -> S[i-1][j-1]
    # 2: Add to one of the j existing subsets -> j * S[i-1][j]
    S[i][j] = (S[i-1][j-1] + j*S[i-1][j]) %mod
