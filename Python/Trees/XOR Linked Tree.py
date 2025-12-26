# Source : https://codeforces.com/blog/entry/135239
P = [0] * n
C = [0] * n
deg = [0] * n
for _ in range(n - 1):
    u,v,c = map(int, input().split())
    P[u] ^= v   ;  P[v] ^= u
    C[u] ^= c   ;  C[v] ^= c
    deg[u] += 1 ;  deg[v] += 1
XOR_traversal_order = []
deg[root] = 0
for i in range(n):
  node = i
  # While node is a leaf
  while deg[node] == 1:
    nei = xor[node]
    # Pluck away node
    XOR_traversal_order.append(node)
    deg[node] = 0
    deg[nei] -= 1
    xor[nei] ^= node
    #C[nei] ^= C[node]
    # Check if nei has become a leaf
    node = nei
# Compute subtree sizes
subtree_size = [1] * n
for node in XOR_traversal_order:
    # Note that xor[node] is the parent of node
    p = xor[node]
    subtree_size[p] += subtree_size[node]
# Compute the index each node would have in a DFS using subtree_size
# NOTE: This modifies subtree_size
for node in reversed(XOR_traversal_order):
    p = xor[node]
    subtree_size[node], subtree_size[p] = subtree_size[p], subtree_size[p] - subtree_size[node]
DFS_traversal_order = [None] * n
for node in range(n):
    DFS_traversal_order[subtree_size[node] - 1] = node
