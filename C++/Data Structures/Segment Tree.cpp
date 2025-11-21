using ll = long long;
const ll LAZY_DEF = 0;

struct node {
	ll x = 1e18;  ll idx=-1;  ll lazy=LAZY_DEF;  };

class Seg {
public:
	ll n;  vector<node> seg;
	Seg(ll n) {
		this->n = n;  seg.resize(4LL*(n +1LL));
	}
	// change here
	node combine(node &a, node &b) {
		node res = a;
		if (b.x < res.x) res = b;
		return res;
	}
	// change here
	node assign(ll x, ll idx) {
		node res;
		res.x = x;
		res.idx = idx;
		return res;
	}
	// change here
	void update_logic(ll idx, ll tl, ll tr, ll val) {
		seg[idx].x += val;
		seg[idx].lazy += val;
	}
	node no_overlap_return() {
		node res;
		return res;
	}
	void propagate(ll &idx, ll &tl, ll &tr) {
		if (seg[idx].lazy != LAZY_DEF and tl != tr) {
			ll mid = tl + ((tr - tl) >> 1LL);
			update_logic(2*idx +1, tl, mid, seg[idx].lazy);
			update_logic(2*idx +2, mid+1, tr, seg[idx].lazy);
			seg[idx].lazy = LAZY_DEF;
		}
	}
	void build_seg(ll idx, ll tl, ll tr, vector<ll> &a) {
		if (tl == tr) {
			seg[idx] = assign(a[tl], tl);
			return;
		}
		ll mid = tl + ((tr - tl) >> 1LL);
		build_seg(2*idx +1, tl, mid, a);
		build_seg(2*idx +2, mid+1, tr, a);
		seg[idx] = combine(seg[2*idx +1], seg[2*idx +2]);
	}
	node query_seg(ll idx, ll tl, ll tr, ll &l, ll &r) {
		propagate(idx, tl, tr);
		if (tl >= l and tr <= r) return seg[idx];
		if (tr < l or tl > r) return no_overlap_return();
		ll mid = tl + ((tr - tl) >> 1LL);
		node left = query_seg(2*idx +1, tl, mid, l, r);
		node right = query_seg(2*idx +2, mid+1, tr, l, r);
		return combine(left, right);
	}
	void update_seg(ll idx, ll tl, ll tr, ll &l, ll &r, ll &x) {
		propagate(idx, tl, tr);
		if (tl > r or tr < l) return;
		if (tl >= l and tr <= r) {
			update_logic(idx, tl, tr, x);
			return;
		}
		ll mid = tl + ((tr - tl) >> 1LL);
		update_seg(2*idx +1, tl, mid, l, r, x);
		update_seg(2*idx +2, mid+1, tr, l, r, x);
		seg[idx] = combine(seg[2*idx +1], seg[2*idx +2]);
	}
	int find_seg(ll idx, ll tl, ll tr, ll &l, ll &r, ll k) {
		if (tl > r or tr < l) return -1;
		if (seg[idx].x < k) return -1;
	    if (tl == tr) return tl;
	    propagate(idx, tl, tr);
	    ll mid = tl + ((tr - tl) >> 1LL);
	    ll res = find_seg(2*idx +1, tl, mid, l, r, k);
	    if (res != -1) return res;
	    return find_seg(2*idx +2, mid+1, tr, l, r, k - seg[2*idx +1].x);
	}

	void build(vector<ll> &a) {
		build_seg(0, 0, n-1, a);
	}
	node query(ll l, ll r) {
		return query_seg(0, 0, n-1, l, r);
	}
	void update(ll l, ll r, ll val) {
		update_seg(0, 0, n-1, l, r, val);
	}
	int find(ll l, ll r, ll k) {
    	return find_seg(0, 0, n-1, l, r, k);
  	}
};
