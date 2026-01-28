MAX_N = 100005 
p = list(range(MAX_N))
sz = [1] * MAX_N
history = []  # Stack to store (child,parent) for rollback
tree = [[] for _ in range(4*MXQ)]

def find(x):
  while x != p[x]: x = p[x]
  return x

def union(x, y):
  x, y = find(x), find(y)
  if x == y:  return 0
  if sz[x]<sz[y]:  x,y = y,x
  p[y] = x
  sz[x] += sz[y]
  history.append((y, x))
  return 1

def rollback(snapshot):
  while len(history) > snapshot:
    y, x = history.pop()
    p[y] = y
    sz[x] -= sz[y]

def insert(i, L, R, l, r, edge):
  if l>R or r<L: return 0
  if l <= start and end <= r:
    tree[i].append(edge)
    return 0
  mid = (L+R) //2
  insert(i<<1, L, mid, l, r, edge)
  insert(i<<1 |1, mid+1, R, l, r, edge)

def solve(i, L, R, que):
  current_snapshot = len(history)
  for u, v in tree[i]:
    union(u, v)
  if L == R:
    if L < len(que):
      q_type, u, v = que[start]
      if q_type == 3: # Example query type
        if find(u) == find(v):
          print("Connected")
        else:
          print("Disconnected")
  else:
    mid = (L+R) //2
    solve(i<<1, L, mid, que)
    solve(i<<1 |1, mid+1, R, que)
  rollback(current_snapshot)

# --- Example Usage Logic ---
# Suppose we have N nodes and Q queries (time steps 0 to Q-1)
# queries list stores tuple: (type, u, v)
# 'ADD': Edge added, 'REMOVE': Edge removed, 'QUERY': Check connectivity

"""
# Helper to map edge lifespans usually required here:
# You would preprocess queries to find (u,v) exists from time [L, R]
# and call: insert(1, 0, Q-1, L, R, (u, v))

# Example Call:
# n = 5
# p = [i for i in range(n + 1)]
# sz = [1] * (n + 1)
# solve(1, 0, num_queries - 1, queries)
"""
