# Max nodes calculation: (N * bits) + 1
lg = 30
BITS = tuple(range(lg-1, -1, -1))
MAX_NODES = n*lg +1
# child[node * 2 + bit] stores the index of the next node
child = [0] * (MAX_NODES * 2)
count = [0] * MAX_NODES
nodes_cnt = 1
def insert(x):
  nonlocal nodes_cnt
  nd = 0
  for i in BITS:
    bit = (x>>i) &1
    idx = (nd<<1) |bit
    if not child[idx]:
      child[idx] = nodes_cnt
      nodes_cnt += 1
    nd = child[idx]
    count[nd] += 1

def remove(x):
  nd = 0
  for i in BITS:
    bit = (x>>i) &1
    idx = (nd<<1) |bit
    prev = nd
    nd = child[idx]
    count[nd] -= 1
    if count[nd] == 0:
      child[(prev<<1) |bit] = 0
      return

def query_max(x):
  nd = 0
  res = 0
  for i in BITS:
    bit = (x>>i) &1
    bit ^=1
    idx = (nd<<1) |bit
    if child[idx] and count[child[idx]]>0:
      res |= (1<<i)
      nd = child[idx]
    else:
      nd = child[idx^1]
  return res
