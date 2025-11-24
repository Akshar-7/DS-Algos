// NOT TESTED
uint64_t hilbertorder(uint64_t x, uint64_t y) {
    const uint64_t logn = __lg(max(x, y) * 2 + 1) | 1;
    const uint64_t maxn = (1ull << logn) - 1;
    uint64_t res = 0;
    for (uint64_t s = 1ull << (logn - 1); s; s >>= 1) {
        bool rx = x & s, ry = y & s;
        res = (res << 2) | (rx ? ry ? 2 : 1 : ry ? 3 : 0);
        if (!rx) {
            if (ry) x ^= maxn, y ^= maxn;
            swap(x, y);
        }
    }
    return res;
}
struct Query {
    int l, r, id;
    int64_t ord;
    bool operator<(const Query& other) const {
        return ord < other.ord;
    }
};
class MoSolver {
private:
    int n;
    vector<int> a;
    vector<Query> queries;
    vector<int> freq;
    int current_ans;
    void add(int idx) {
        int val = a[idx];
        if (freq[val] == 0)  current_ans++;
        freq[val]++;
    }
    void remove(int idx) {
        int val = a[idx];
        freq[val]--;
        if (freq[val] == 0)  current_ans--;
    }
    int get_answer() {  return current_ans;  }

public:
    MoSolver(const vector<int>& input_array) : a(input_array) {
        n = input_array.size();
        current_ans = 0;
        freq.resize(1000005, 0); 
    }
    void add_query(int l, int r, int id) {
        queries.push_back({l, r, id, hilbertorder(l, r)});
    }

    vector<int> solve() {
        sort(queries.begin(), queries.end());
        vector<int> answers(queries.size());
        int curr_l = 0;
        int curr_r = -1;
        for (const auto& q : queries) {
            while (curr_l > q.l) add(--curr_l);
            while (curr_r < q.r) add(++curr_r);
            while (curr_l < q.l) remove(curr_l++);
            while (curr_r > q.r) remove(curr_r--);
            answers[q.id] = get_answer();
        }
        return answers;
    }
};
