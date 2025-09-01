class Node:
  def __init__(self):
    self.c = 0
    self.child = [None]*2

def merge(x, root):
  nd = root
  for i in range(29, -1, -1):
    bit = (x>>i)&1
    if nd.child[bit]==None:
      nd.child[bit] = Node()
    chd = nd.child[bit]
    chd.c +=1
    nd = chd

def remove(x, root):
  nd = root
  for i in range(29, -1, -1):
    bit = (x>>i)&1
    chd = nd.child[bit]
    chd.c -=1
    if chd.c==0:
      nd.child[bit] = None
      del chd
      break
    nd = chd

def query(x, root):
  nd = root
  res = 0
  for i in range(29, -1, -1):
    bit = (x>>i)&1
    if nd.child[bit]:
      res ^=(bit<<i)
      nd = nd.child[bit]
    else:
      res ^=((bit^1)<<i)
      nd = nd.child[bit^1]
  return res
