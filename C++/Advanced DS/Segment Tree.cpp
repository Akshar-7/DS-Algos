struct node {
	ll x = 1e18;  ll idx=0;  ll lazy=0;  };

class SegmentTree {
public:
	ll n;  vector<node> seg;

	SegmentTree(ll n) {
		this->n = n;  seg.resize(4LL * (n + 1LL));
  }
	// change here
	node combine(const node &a, const node &b) {
		if (b.x < a.x) return b;
		return a;
	}
	// change here
	node assign(ll x, ll idx) {
		node res;
		res.x = x;
		res.idx = idx;
		return res;
  }
	// change here
	node no_overlap_return() {
		node res;  res.x = 1e18;
		return res;
	}
	// change here
	void update_logic(ll &idx, ll &tl, ll &tr, ll &val) {
		seg[idx].lazy -= val;
	}
	// change here
	void propagate(ll &idx, ll &tl, ll &tr) {
		if (seg[idx].lazy != 0) {
			seg[idx].x += seg[idx].lazy;
			if (tl != tr) {
				seg[2 * idx + 1].lazy += seg[idx].lazy;
				seg[2 * idx + 2].lazy += seg[idx].lazy;
			}
			seg[idx].lazy = 0;
		}
	}

	void build_seg(ll idx, ll tl, ll tr, vector<ll> &a) {
		if (tl == tr) {
			seg[idx] = assign(a[tl], tl);
			return;
		}
		ll mid = tl + ((tr - tl) >> 1LL);
		build_seg(2LL * idx + 1LL, tl, mid, a);
		build_seg(2LL * idx + 2LL, mid + 1, tr, a);
		seg[idx] = combine(seg[2LL * idx + 1LL], seg[2LL * idx + 2LL]);
	}

	node query_seg(ll idx, ll tl, ll tr, ll &l, ll &r) {
		propagate(idx, tl, tr);
		if (tl >= l and tr <= r) return seg[idx];
		if (tr < l or tl > r) return no_overlap_return();
		ll mid = tl + ((tr - tl) >> 1LL);
		node left = query_seg(2LL * idx + 1LL, tl, mid, l, r);
		node right = query_seg(2LL * idx + 2LL, mid + 1LL, tr, l, r);
		return combine(left, right);
	}
	void update_seg(ll idx, ll tl, ll tr, ll &l, ll &r, ll &x) {
		propagate(idx, tl, tr);
		if (tl > r or tr < l) return;
		if (tl >= l and tr <= r) {
			update_logic(idx, tl, tr, x);
			propagate(idx, tl, tr);
			return;
		}
		ll mid = tl + ((tr - tl) >> 1LL);
		update_seg(2LL * idx + 1LL, tl, mid, l, r, x);
		update_seg(2LL * idx + 2LL, mid + 1LL, tr, l, r, x);
		seg[idx] = combine(seg[2LL * idx + 1LL], seg[2LL * idx + 2LL]);
	}

	void build(vector<ll> &a) {
		build_seg(0, 0, n - 1, a);
	}

	node query(ll l, ll r) {
		return query_seg(0, 0, n - 1, l, r);
	}

	void update(ll l, ll r, ll val) {
		update_seg(0, 0, n - 1, l, r, val);
	}
};
