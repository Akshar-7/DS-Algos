class Edge:
  #__slots__ = ['to', 'next']
  __slots__ = ['to', 'w', 'next']
  def __init__(self, to, nxt_i, weight=1):
    self.to = to
    self.w = weight
    self.next = nxt_i

class FlatGraph:
  __slots__ = ['head', 'edges', 'ecnt']
  def __init__(self, nv, mxe):
    # head[i] stores the index of the first edge for vertex i. -1 means no edges.
    self.head = [-1] * nv
    # Pre-allocate edge pool
    self.edges = [None] * mxe
    self.ecnt = 0
      
  def add(self, u, v, w):
    # The new edge points to the current head of u
    self.edges[self.ecnt] = Edge(v, self.head[u], w)
    # Update head of u to be this new edge's index
    self.head[u] = self.ecnt
    self.ecnt += 1
      
  def ngbr(self, u: int):
    neighbors = []
    e = self.head[u]
    while e != -1:
      edge = self.edges[e]
      #neighbors.append(edge.to)
      neighbors.append((edge.to, edge.weight))
      e = edge.next
    return neighbors
