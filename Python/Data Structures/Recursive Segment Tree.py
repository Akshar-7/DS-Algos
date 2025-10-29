class node:
  x = 10**18
  i = 0; lazy = 0

class Seg:
	def __init__(self, n):
	  self.n = n
	  self.seg = [node()]*(4*n+1)
	
	# change here
	def combine(a, b):
		res = a
		if (b.x < res.x): res=b
		return res

	# change here
	def assign(x, idx):
		res = node()
		res.x = x
		res.idx = idx
		return res

	# change here
	def no_overlap_return():
		res = node();  res.x = 10**18;
		return res

	# change here
	def update_logic(idx, tl, tr, val):
		seg[idx].lazy += val

	# change here
	def propagate(idx, tl, tr):
		if (seg[idx].lazy != 0):
			seg[idx].x += seg[idx].lazy
			if (tl != tr):
				seg[2 * idx + 1].lazy += seg[idx].lazy
				seg[2 * idx + 2].lazy += seg[idx].lazy
			seg[idx].lazy = 0

	def build_seg(idx, tl, tr, a):
		if (tl == tr):
			seg[idx] = assign(a[tl], tl);
			return;
		mid = tl + ((tr - tl) >> 1)
		build_seg(2 * idx + 1, tl, mid, a)
		build_seg(2 * idx + 2, mid + 1, tr, a)
		seg[idx] = combine(seg[2 * idx + 1], seg[2 * idx + 2])

	def query_seg(idx, tl, tr, l, r):
		propagate(idx, tl, tr)
		if (tl >= l and tr <= r): return seg[idx]
		if (tr < l or tl > r): return no_overlap_return()
		mid = tl + ((tr - tl) >> 1)
		left = query_seg(2 * idx + 1, tl, mid, l, r)
		right = query_seg(2 * idx + 2, mid + 1, tr, l, r)
		return combine(left, right)

	def update_seg(idx, tl, tr, l, r, x):
		propagate(idx, tl, tr)
		if (tl > r or tr < l): return;
		if (tl >= l and tr <= r):
			update_logic(idx, tl, tr, x)
			propagate(idx, tl, tr)
			return;
		mid = tl + ((tr - tl) >> 1);
		update_seg(2 * idx + 1, tl, mid, l, r, x)
		update_seg(2 * idx + 2, mid + 1, tr, l, r, x)
		seg[idx] = combine(seg[2 * idx + 1], seg[2 * idx + 2])

	def build(a):
		build_seg(0, 0, n - 1, a)

	def query(l, r):
		return query_seg(0, 0, n - 1, l, r)

	def update(l, r, val):
		update_seg(0, 0, n - 1, l, r, val)
