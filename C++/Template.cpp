#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
template <typename T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

//#define int long long
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef long long ll;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define iter(x) auto it=(x).rbegin(); it!=(x).rend(); it++
#define all(x) (x).begin(), (x).end()
#define mine min_element
#define maxe max_element
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define endl '\n'
#define ff first
#define ss second

void solve() {
  int n; cin>>n;
  vi a(n); for(auto& x:a) cin>>x;
  
}

signed main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);
  int t=1; cin>>t;
  while(t--) solve();
  return 0;
}
