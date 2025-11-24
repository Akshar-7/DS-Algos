// Locally

vector<int> d = a;
sort(d.begin(), d.end());
d.resize(unique(d.begin(), d.end()) - d.begin());
for (int i = 0; i < n; ++i) {
  a[i] = lower_bound(d.begin(), d.end(), a[i]) - d.begin();
}


// Function

map<int, int> cocom(vector<int> &b){
    sort(b.begin(), b.end());
    map<int, int> m;
    for (int i = 0; i < n; i++)  m[b[i]] = i;
    for (int i = 0; i < n; i++)  a[i] = m[a[i]];
    return m;
}
