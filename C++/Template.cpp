#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update> oset;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define all(x) (x).begin(), (x).end()
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

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);
  int t; cin>>t;
  while(t--) solve();
  return 0;
}
