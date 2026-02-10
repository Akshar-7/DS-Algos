from array import array
LAZY_DEF = 0
INF = 10**18
n = 0
x = idx = lazy = []
# CHANGE HERE
def init_seg(sz):   # Initialization
  global n, x, idx, lazy
  n = sz
  x = array('q', [INF]) *(4*n)
  idx = array('i', [-1]) *(4*n)
  lazy = array('q', [LAZY_DEF]) *(4*n)
# CHANGE HERE
def combine(v1, i1, v2, i2):   # Used in query and pull
  if v1 <= v2:
    return (v1, i1)
  else:
    return (v2, i2)
# CHANGE HERE
def pull(node):   # Used in build & update
  L = node<<1 |1
  R = node+1 <<1
  x[node], idx[node] = combine(x[L], idx[L], x[R], idx[R])
# CHANGE HERE
def update_logic(node, tl, tr, val):   # Used in update
  x[node] += val
  lazy[node] += val

def no_overlap_return():   # Used in query
  return (INF, -1)

def propagate(node, tl, tr):   # Used in update & query
  if lazy[node] != LAZY_DEF and tl != tr:
    mid = tl + ((tr-tl)>>1)
    update_logic(node<<1 |1, tl, mid, lazy[node])
    update_logic(node+1 <<1, mid+1, tr, lazy[node])
    lazy[node] = LAZY_DEF

def build_seg(node, tl, tr, a):
  if tl == tr:
    x[node], idx[node], lazy[node] = (a[tl], tl, LAZY_DEF)
    return
  mid = tl + ((tr-tl) >> 1)
  build_seg(node<<1 |1, tl, mid, a)
  build_seg(node+1 <<1, mid+1, tr, a)
  pull(node)

def query_seg(node, tl, tr, l, r):
  propagate(node, tl, tr)
  if tl >= l and tr <= r:
    return (x[node], idx[node])
  if tr < l or tl > r:
    return no_overlap_return()
  mid = tl + ((tr-tl)>>1)
  L = query_seg(node<<1 |1, tl, mid, l, r)
  R = query_seg(node+1 <<1, mid+1, tr, l, r)
  # Paste pull logic here & add return values
  return combine(L[0], L[1], R[0], R[1])

def update_seg(node, tl, tr, l, r, val):
  propagate(node, tl, tr)
  if tl>r or tr<l: return 
  if tl >= l and tr <= r:
    update_logic(node, tl, tr, val)
    return
  mid = tl + ((tr-tl)>>1)
  update_seg(node<<1 |1, tl, mid, l, r, val)
  update_seg(node+1 <<1, mid+1, tr, l, r, val)
  pull(node)

def find_seg(node, tl, tr, l, r, k):
  if tl > r or tr < l: return -1
  if x[node] < k: return -1
  if tl == tr: return tl
  propagate(node, tl, tr)
  mid = tl + ((tr-tl)>>1)
  res = find_seg(node<<1 |1, tl, mid, l, r, k)
  if res != -1: return res
  return find_seg(node+1 <<1, mid+1, tr, l, r, k - x[node<<1 |1])

def build(a): build_seg(0, 0, n-1, a)
def query(l, r): return query_seg(0, 0, n-1, l, r)
def update(l, r, val): update_seg(0, 0, n-1, l, r, val)
def find(l, r, k): return find_seg(0, 0, n-1, l, r, k)
