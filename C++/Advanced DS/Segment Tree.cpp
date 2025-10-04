struct Seg {
  int n;
  vector<int> tree, lazy;
  
  Seg(const vector<int>& v) : 
      n(v.size()), tree(4 * n), lazy(4 * n, 0) {
    build(1, 0, n - 1, v);
  }

  int func(int A, int B) { return min(A,B); }
 
  void build(int node, int L, int R, const vector<int>& v) {
    if (L == R) {
      tree[node] = v[L];
      return;
    }
    int M = (L + R) / 2;
    build(node * 2, L, M, v);
    build(node * 2 + 1, M + 1, R, v);
    tree[node] = func(tree[node * 2], tree[node * 2 + 1]);
  }
  
  void add(int node, int l, int r, int i, int val) {
    if (r < i) return;
    if (l >= i) {
      lazy[node] += val;
      tree[node] += val;
      return;
    }
    int m = (l + r) / 2;
    add(node * 2, l, m, i, val);
    add(node * 2 + 1, m + 1, r, i, val);
    tree[node] = func(tree[node * 2], tree[node * 2 + 1]) + lazy[node];
  }
 
  int pop(int node, int l, int r, int val) {
    if (l == r) {
      tree[node] = 2e18;
      return b;
    }
    int m = (l + r) / 2;
    val -= lazy[node];
 
    int ret = -1;
    if (tree[node * 2 + 1] == val)
      ret = pop(node * 2 + 1, m + 1, r, val);
    else ret = pop(node * 2, l, m, val);
    tree[node] = func(tree[node * 2], tree[node * 2 + 1]) + lazy[node];
    return ret;
  }
 
  void Add(int l, int val) { add(1, 0, n - 1, l, val); }
  int Pop() { return pop(1, 0, n - 1, 0); }
};
