class Fenwick {
public:
	int n;  vector<ll> fw;
	Fenwick_Tree(int sz) {
		this -> n = sz;
		fw.assign(n + 5, 0);
	};
	void build(vector<ll> &a) {
		for (ll i = 1; i <= n; i++)  add(i, a[i]);
	}
	ll make_query(ll idx) {
		ll res = 0;
		for (; idx > 0; idx -= (idx & (-idx)))  res += fw[idx];
		return res;
	}
	ll query(ll l, ll r) {
		return make_query(r) - make_query(l - 1);
	}
	void add(ll idx, ll x) {
		for (; idx <= n; idx += (idx & (-idx)))  fw[idx] += x;
	}
};
