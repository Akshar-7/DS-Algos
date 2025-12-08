using ll = long long;
const ll LAZY_DEF = 0; 

struct node {
    ll sum = 0;  ll lazy = LAZY_DEF;  bool has_lazy = false;  int l = -1;  int r = -1;
};

class DynamicSeg {
public:
    int n;
    vector<node> seg;
    DynamicSeg(int n) {
        this->n = n;
        seg.reserve(5000000); // Pre-allocate memory ~ Q * logN
        create_node(); // Dummy root at i=0
    }
    int create_node() {
        seg.push_back(node());
        return seg.size() - 1;
    }
    void clear(int new_n) {
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
        return res;
    }
    // change here
    void update_logic(int idx, int tl, int tr, int val) {
        seg[idx].lazy = val;
        seg[idx].has_lazy = true;
        seg[idx].sum = val * (tr - tl + 1);
    }
    void propagate(int idx, int tl, int tr) {
        if (seg[idx].has_lazy && tl != tr) {
            extend(idx);
            ll mid = tl + ((tr - tl) >> 1LL);
            update_logic(seg[idx].l, tl, mid, seg[idx].lazy);
            update_logic(seg[idx].r, mid + 1, tr, seg[idx].lazy);
            seg[idx].has_lazy = false;
            seg[idx].lazy = LAZY_DEF;
        }
    }

    void update_seg(int idx, int tl, int tr, int &l, int &r, int &val) {
        if (tl > r or tr < l) return;
        if (tl >= l and tr <= r) {
            update_logic(idx, tl, tr, val);
            return;
        }
        propagate(idx, tl, tr);
        extend(idx);
        int mid = tl + ((tr - tl) >> 1LL);
        update_seg(seg[idx].l, tl, mid, l, r, val);
        update_seg(seg[idx].r, mid + 1, tr, l, r, val);
        node res = combine(seg[seg[idx].l], seg[seg[idx].r]);
        seg[idx].sum = res.sum;
    }
    // Merges tree rooted at 'b' into tree rooted at 'a' and return idx of new root
    int merge(int a, int b, int tl, int tr) {
        if (a == -1 || b == -1) return (a != -1) ? a : b;
        if (tl == tr) {
            seg[a].sum += seg[b].sum;
            return a;
        }
        // Push lazy down before merging children to ensure consistency
        propagate(a, tl, tr);
        propagate(b, tl, tr);
        int mid = tl + ((tr - tl) >> 1LL);
        seg[a].l = merge(seg[a].l, seg[b].l, tl, mid);
        seg[a].r = merge(seg[a].r, seg[b].r, mid + 1, tr);
        // Pull up
        node left = (seg[a].l != -1) ? seg[seg[a].l] : no_overlap_return();
        node right = (seg[a].r != -1) ? seg[seg[a].r] : no_overlap_return();
        node res = combine(left, right);
        seg[a].sum = res.sum;
        return a;
    }
    node query_seg(int idx, int tl, int tr, int &l, int &r) {
        propagate(idx, tl, tr);
        if (tl >= l and tr <= r) return seg[idx];
        if (tr < l or tl > r) return no_overlap_return();
        int mid = tl + ((tr - tl) >> 1LL);
        node left, right;
        if (seg[idx].l != -1) left = query_seg(seg[idx].l, tl, mid, l, r);
        else left = no_overlap_return();
        if (seg[idx].r != -1) right = query_seg(seg[idx].r, mid + 1, tr, l, r);
        else right = no_overlap_return();
        return combine(left, right);
    }
    int find_seg(int idx, int tl, int tr, int h, int ch) {
        if (ch + seg[idx].sum <= h)  return (tr - tl + 1);
        if (tl == tr) return 0;
        propagate(idx, tl, tr);
        extend(idx);
        ll mid = tl + ((tr - tl) >> 1LL);
        if (ch + seg[seg[idx].l].sum > h)  return find_seg(seg[idx].l, tl, mid, h, ch);
        return (mid - tl + 1) + find_seg(seg[idx].r, mid+1, tr, h, ch +seg[seg[idx].l].sum);
    }

    void update(int l, int r, int val) {
        update_seg(0, 1, n, l, r, val);
    }
    node query(int l, int r) {
        return query_seg(0, 1, n, l, r);
    }
    int find(int h) {
        return find_seg(0, 1, n, h, 0);
    }
};
