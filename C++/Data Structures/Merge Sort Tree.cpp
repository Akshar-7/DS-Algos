/*
  TO-DO: Test and Improve the Code
  Warning : Untested Code (may contain errors)
*/

class Merge {
public:
  ll n;
  vector<int> seg[4*n +5];
  Merge(ll n) {
	  this->n = n;
  }

  void build_tree(int node, int l, int r, vector<int> &a){
    if (l==r){
      seg[node].push_back(a[l]);
      return;}
    int mid = (l+r)/2;
    build(node*2, l, mid, a);
    build(node*2+1, mid+1, r, a);
    int i=0, j=0;
    // use two pointers to merge the two vectors in O(r-l+1)
    while (i<seg[node*2].size() && j<seg[node*2+1].size()){
      if (seg[node*2][i]<seg[node*2+1][j]) seg[node].push_back(seg[node*2][i++]);
      else seg[node].push_back(seg[node*2+1][j++]);
    }
    while (i<seg[node*2].size()) seg[node].push_back(seg[node*2][i++]);
    while (j<seg[node*2+1].size()) seg[node].push_back(seg[node*2+1][j++]);
    return;
  }
  
  int query_tree(int node, int l, int r, int lx, int rx, int x){
    //if outside -> 0
    if (l>rx || r<lx) return 0;
    //if inside do binary search
    if (l>=lx && r<=rx){
      int L=0, R=seg[node].size()-1, mid, ans=0;
      while (L<=R) {
        mid = (L+R)/2;
        if (seg[node][mid]<x) {
          ans = mid+1;
          L = mid+1;
        } else R = mid-1;
      } return ans;
    }
    int mid = (l+r)/2;
    return query(node*2, l, mid, lx, rx, x)+query(node*2+1, mid+1, r, lx, rx, x);
  }
  
  void build(vector<ll> &a) {
		build_tree(0, 0, n-1, a);
	}

	int query(ll l, ll r, ll x) {
		return query_tree(0, 0, n-1, l, r, x);
	}
}
