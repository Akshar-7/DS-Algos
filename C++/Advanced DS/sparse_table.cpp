template <typename Node>
class SparseTable {
public:
 
	ll n, LOG;
	vector<vector<Node>> table;
	vector<ll> lg;
 
	SparseTable(vector<ll> &a) {
		ll sz = a.size();
		this -> n = sz;
		this -> LOG = log2(n) + 1;
		table = vector<vector<Node>>(LOG, vector<Node>(n));
		for (ll i = 0; i < n; i++) table[0][i] = a[i];
		lg = vector<ll>(n + 1, 0);
		build();
	}
 
	void build() {
		for (ll i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
		for (ll j = 1; j < LOG; j++) {
			ll len = (1 << j);
			for (ll i = 0; i + len <= n; i++)
				table[j][i].merge(table[j - 1][i], table[j - 1][i + (1 << (j - 1))]);
		}
	}
 
	Node query(ll l, ll r) {
		ll x = lg[r - l + 1];
		Node ans = Node();
		ans.merge(table[x][l], table[x][r - (1 << x) + 1]);
		return ans;
	}
};
 
struct Node1 {
	ll x = 0;
	Node1() {}
	Node1(ll _x) : x(_x) {}
	void merge(Node1& l, Node1& r) {
		this -> x = max(l.x, r.x);
	}
	ll val() {
		return this -> x;
	}
};
