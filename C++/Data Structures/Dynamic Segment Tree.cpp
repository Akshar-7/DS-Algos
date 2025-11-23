using ll = long long;
const ll LAZY_DEF = 0; 

struct node {
    ll sum = 0;  ll mxp = 0;  ll lazy = LAZY_DEF;  bool has_lazy = false;  int l = -1;  int r = -1;
};

class DynamicSeg {
public:
    ll n;
    vector<node> seg;
    DynamicSeg(ll n) {
        this->n = n;
        seg.reserve(5000000); // Pre-allocate memory
        create_node(); // Dummy root at i=0
    }
    int create_node() {
        seg.push_back(node());
        return seg.size() - 1;
    }
    void clear(ll new_n) {
        n = new_n;
        seg.clear();
        create_node();
    }
    void extend(int idx) {
        if (seg[idx].l == -1) seg[idx].l = create_node();
        if (seg[idx].r == -1) seg[idx].r = create_node();
    }
    node no_overlap_return() {
        return node();
    }
    // change here
    node combine(node &a, node &b) {
        node res;
        res.sum = a.sum + b.sum;
        res.mxp = max(a.mxp, a.sum + b.mxp);
        return res;
    }
    // change here
    void update_logic(int idx, ll tl, ll tr, ll val) {
        seg[idx].lazy = val;
        seg[idx].has_lazy = true;
        seg[idx].sum = val * (tr - tl + 1);
        seg[idx].mxp = (val > 0) ? seg[idx].sum : 0;
    }

    void propagate(int idx, ll tl, ll tr) {
        if (seg[idx].has_lazy && tl != tr) {
            extend(idx);
            ll mid = tl + ((tr - tl) >> 1LL);
            update_logic(seg[idx].l, tl, mid, seg[idx].lazy);
            update_logic(seg[idx].r, mid + 1, tr, seg[idx].lazy);
            seg[idx].has_lazy = false;
            seg[idx].lazy = LAZY_DEF;
        }
    }

    void update_seg(int idx, ll tl, ll tr, ll &l, ll &r, ll &val) {
        if (tl > r or tr < l) return;
        
        if (tl >= l and tr <= r) {
            update_logic(idx, tl, tr, val);
            return;
        }
        propagate(idx, tl, tr);
        extend(idx);
        ll mid = tl + ((tr - tl) >> 1LL);
        update_seg(seg[idx].l, tl, mid, l, r, val);
        update_seg(seg[idx].r, mid + 1, tr, l, r, val);
        node res = combine(seg[seg[idx].l], seg[seg[idx].r]);
        seg[idx].sum = res.sum;
        seg[idx].mxp = res.mxp;
    }

    // Merges tree rooted at 'b' into tree rooted at 'a' and return idx of new root
    int merge(int a, int b, ll tl, ll tr) {
        if (a == -1 || b == -1) return (a != -1) ? a : b;
        if (tl == tr) {
            seg[a].sum += seg[b].sum;
            seg[a].mxp = (seg[a].sum > 0) ? seg[a].sum : 0;
            return a;
        }
        // Push lazy down before merging children to ensure consistency
        propagate(a, tl, tr);
        propagate(b, tl, tr);
        ll mid = tl + ((tr - tl) >> 1LL);
        seg[a].l = merge(seg[a].l, seg[b].l, tl, mid);
        seg[a].r = merge(seg[a].r, seg[b].r, mid + 1, tr);
        // Pull up
        node left = (seg[a].l != -1) ? seg[seg[a].l] : no_overlap_return();
        node right = (seg[a].r != -1) ? seg[seg[a].r] : no_overlap_return();
        node res = combine(left, right);
        seg[a].sum = res.sum;
        seg[a].mxp = res.mxp;
        return a;
    }

    node query_seg(int idx, ll tl, ll tr, ll &l, ll &r) {
        propagate(idx, tl, tr);
        if (tl >= l and tr <= r) return seg[idx];
        if (tr < l or tl > r) return no_overlap_return();
        ll mid = tl + ((tr - tl) >> 1LL);
        node left, right;
        if (seg[idx].l != -1) left = query_seg(seg[idx].l, tl, mid, l, r);
        else left = no_overlap_return();
        if (seg[idx].r != -1) right = query_seg(seg[idx].r, mid + 1, tr, l, r);
        else right = no_overlap_return();
        return combine(left, right);
    }

    int find_seg(int idx, ll tl, ll tr, ll h, ll ch) {
        if (ch + seg[idx].mxp <= h)  return (tr - tl + 1);
        if (tl == tr) return 0;
        propagate(idx, tl, tr);
        extend(idx);
        ll mid = tl + ((tr - tl) >> 1LL);
        if (current_h + seg[seg[idx].l].mxp > h)  return find_seg(seg[idx].l, tl, mid, h, current_h);
        return (mid - tl + 1) + find_seg(seg[idx].r, mid+1, tr, h, ch +seg[seg[idx].l].sum);
    }

    void update(ll l, ll r, ll val) {
        update_seg(0, 1, n, l, r, val);
    }
    node query(ll l, ll r) {
        return query_seg(0, 1, n, l, r);
    }
    int find(ll h) {
        return find_seg(0, 1, n, h, 0);
    }
};
