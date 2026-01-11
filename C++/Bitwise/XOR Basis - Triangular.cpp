template < ll B = 64 >
struct Basis{
    ll n, sz, basis[B];
    void clear(){
        n = sz = 0;
        mem(basis, 0);
    }
    Basis() { clear(); }
    bool insert(ll x) {
        n++;
        for(ll i = B - 1; i >= 0; i--) {
            if((x >> i) & 1ll == 0) continue;
            if(basis[i] == 0) {
                basis[i] = x; sz++;
                return true;
            }
            x ^= basis[i];
        }
        return false;
    }
    // merge the current basis with another one
    bool merge(Basis &b) {
        bool flag = false;
        for(ll i = B -1; i >= 0; i--)
            if(b.basis[i] && !insert(b.basis[i])) flag = true;
        return flag;
    }
    // returns the number of distinct (unique) XOR values that can be formed
    ll distincts() { return 1ll << sz; }
    // returns true if x can be formed as the XOR of some subset of the basis
    bool can(ll x) {
        for(ll i = B - 1; i >= 0; i--)
            x = min(x, x ^ basis[i]);
        return x == 0;
    }
    // returns the total number of subsets of the original set whose XOR is exactly x
    ll mod_exp(ll x, ll n, ll m = mod) { ll res = 1; while(n)
    { if(n % 2) res = (((res % m) * (x % m)) % m); x = (((x % m) * (x % m)) % m); n /= 2; } return res; }
    ll count(ll x) {
        if(!can(x)) return 0;
        return mod_exp(2ll, n - sz);
    }
    // returns the maximum XOR you can get by XORing x with any subset of the basis
    ll minXor(ll x = 0) {
        for(ll i = B - 1; i >= 0; i--)
            x = min(x, x ^ basis[i]);
        return x;
    }
    // returns the maximum XOR you can get by XORing x with any subset of the basis
    ll maxXor(ll x = 0) {
        for(ll i = B - 1; i >= 0; i--)
            x = max(x, x ^ basis[i]);
        return x;
    }
    // returns the k-th smallest distinct XOR value (1-st is 0)
    ll kth(T k) {
        ll cnt = (1ll << sz);
        if(k < 1 || k > cnt) return -1;
        ll x = 0;
        for(ll i = B - 1; i >= 0; i--) {
            if(basis[i]) {
                if(k > (cnt >> 1ll)) {
                    if(!((x >> i) & 1ll)) x ^= basis[i];
                    k -= (cnt >> 1ll);
                }
                else {
                    if((x >> i) & 1ll) x ^= basis[i];
                }
                cnt >>= 1ll;
            }
        }
        return x;
    }
    // returns the rank (order) of x among the distinct XOR values (1-st is 0)
    ll getOrder(ll x) {
        if(!can(x)) return -1;
        ll k = 0;
        for(ll i = B - 1; i >= 0; i--)
            if(basis[i])
                k = 2*k + ((x >> i) & 1ll);
        return k + 1;
    }
    // applies a bitwise AND with x to every value in the XOR basis, then rebuilds the basis
    void updateAnd(ll x) {
        vector < ll > v;
        for(ll i = 0; i < B; i++) {
            if(basis[i]) {
                v.push_back(basis[i] & x);
                basis[i] = 0;
            }
        }
        sz = 0;
        for(const auto &i : v) insert(i);
    }
    // return the number of distinct XOR subset values that are < x
    ll countLess(ll x) {
        if(x < 0) return 0;
        ll ans = 0, cnt = (1ll << sz), mask = 0;
        for(ll i = B - 1; i >= 0; i--) {
            if(basis[i]) {
                if((x >> i) & 1ll) {
                    ans += (cnt >> 1ll);
                    if(!((mask >> i) & 1ll)) mask ^= basis[i];
                }
                else {
                    if((mask >> i) & 1ll) mask ^= basis[i];
                }
                cnt >>= 1ll;
            }
            else {
                if(((x >> i) & 1ll) != ((mask >> i) & 1ll)) {
                    if((x >> i) & 1ll) return ans + cnt;
                    else  return ans;
                }
            }
        }
        return ans;
    }
};
