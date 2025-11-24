//    -----    On Hiatus    -----
using ll = long long;

struct node {
    ll x = 1e18;  ll idx = -1;
    int l = 0;  int r = 0; 
};

class PersistentSeg {
public:
    ll n;
    vector<node> seg;
    vector<int> roots; // NEW: Stores the root node index for each version
    int nodes_cnt = 0; // NEW: Counter for allocated nodes
    PersistentSeg(ll n, ll max_updates) {
        this->n = n;
        seg.resize(4LL * n + max_updates * 20LL);    // 2 *N + Q *logN
        roots.push_back(0); // Version 0
    }
    int new_node() { return ++nodes_cnt; }

    int copy_node(int idx) {
        int new_idx = new_node();
        seg[new_idx] = seg[idx];
        return new_idx;
    }
    // change here
    node combine(node &a, node &b) {
        node res;
        res.x = min(a.x, b.x);
        return res;
    }
    // change here
    node assign(ll x, ll idx) {
        node res;
        res.x = x;
        res.idx = idx;
        return res;
    }
    node no_overlap_return() {
        node res;
        return res;
    }
    // Returns the index of the current node constructed
    int build_seg(ll tl, ll tr, vector<ll> &a) {
        int idx = new_node();
        if (tl == tr) {
            seg[idx] = assign(a[tl], tl);
            return idx;
        }
        ll mid = tl + ((tr - tl) >> 1LL);
        seg[idx].l = build_seg(tl, mid, a);
        seg[idx].r = build_seg(mid + 1, tr, a);
        node left_node = seg[seg[idx].l];
        node right_node = seg[seg[idx].r];
        int curr_l = seg[idx].l;
        int curr_r = seg[idx].r;
        seg[idx] = combine(left_node, right_node);
        seg[idx].l = curr_l;
        seg[idx].r = curr_r;
        return idx;
    }
    // Returns the index of the NEW node created for this version
    int update_seg(int prev_node_idx, ll tl, ll tr, ll pos, ll val) {
        // Create a copy of the previous version's node
        int idx = copy_node(prev_node_idx);
        if (tl == tr) {
            // Logic for leaf update
            seg[idx] = assign(val, tl); 
            return idx;
        }
        ll mid = tl + ((tr - tl) >> 1LL);
        // Path Copying Logic
        if (pos <= mid) {
            // Link new Left child, Reuse old Right child
            seg[idx].l = update_seg(seg[prev_node_idx].l, tl, mid, pos, val);
            seg[idx].r = seg[prev_node_idx].r;
        } else {
            // Reuse old Left child, Link new Right child
            seg[idx].l = seg[prev_node_idx].l;
            seg[idx].r = update_seg(seg[prev_node_idx].r, mid + 1, tr, pos, val);
        }
        node left_node = seg[seg[idx].l];
        node right_node = seg[seg[idx].r];
        int curr_l = seg[idx].l;
        int curr_r = seg[idx].r;
        seg[idx] = combine(left_node, right_node);
        seg[idx].l = curr_l;
        seg[idx].r = curr_r;
        return idx;
    }
    node query_seg(int idx, ll tl, ll tr, ll l, ll r) {
        if (tl >= l and tr <= r) return seg[idx];
        if (tr < l or tl > r) return no_overlap_return();
        ll mid = tl + ((tr - tl) >> 1LL);
        node left = query_seg(seg[idx].l, tl, mid, l, r);
        node right = query_seg(seg[idx].r, mid + 1, tr, l, r);
        return combine(left, right);
    }
    int find_seg(int idx, ll tl, ll tr, ll l, ll r, ll k) {
        if (tl > r or tr < l) return -1;
        if (seg[idx].x < k) return -1;
        if (tl == tr) return tl;
        ll mid = tl + ((tr - tl) >> 1LL);
        int res = find_seg(seg[idx].l, tl, mid, l, r, k);
        if (res != -1) return res;
        return find_seg(seg[idx].r, mid + 1, tr, l, r, k);
    }
    void build(vector<ll> &a) {
        int root = build_seg(0, n - 1, a);
        roots.push_back(root); // Store Version 1 (Initial State)
    }
    // Updates version 'v' at 'pos' with 'val', creating a NEW version
    void update(int v, ll pos, ll val) {
        int new_root = update_seg(roots[v], 0, n - 1, pos, val);
        roots.push_back(new_root);
    }
    // Query on specific version 'v'
    node query(int v, ll l, ll r) {
        return query_seg(roots[v], 0, n - 1, l, r);
    }
    // Find on specific version 'v'
    int find(int v, ll l, ll r, ll k) {
        return find_seg(roots[v], 0, n - 1, l, r, k);
    }
};
