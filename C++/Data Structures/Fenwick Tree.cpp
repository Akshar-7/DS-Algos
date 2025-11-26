class Fenwick {
public:
	int n;  vector<ll> t; int LOGN;
	Fenwick_Tree(int sz) {
		this -> n = sz;
		this -> LOGN = 31 - __builtin_clz(sz);
		t.assign(n + 5, 0);
	};
	void build(vector<ll> &a) {
	    for (int i = 1; i <= n; i++) {
			t[i] += a[i-1];
	        int par = i + (i & -i);
	        if (par <= n) t[par] += t[i];
	    }
	}
	int kth_element(int k) {
	    int idx = 0;
	    for (int i = 1 << LOGN; i > 0; i >>= 1) {
	        if (idx + i <= n && tree[idx + i] < k) {
	            idx += i;
	            k -= tree[idx];
	        }
	    }
    	return idx + 1;
	}
	ll make_query(ll idx) {
		ll res = 0;
		for (; idx > 0; idx -= (idx & (-idx)))  res += t[idx];
		return res;
	}
	ll query(ll l, ll r) {
		return make_query(r) - make_query(l - 1);
	}
	void add(ll idx, ll x) {
		for (; idx <= n; idx += (idx & (-idx)))  t[idx] += x;
	}
};
