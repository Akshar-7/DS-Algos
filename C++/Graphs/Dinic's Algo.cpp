struct Dinic {
  struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;};

  int n;
  vector<vector<Edge>> g;
  vector<int> lvl, ptr;
  Dinic(int n) : n(n), g(n), lvl(n), ptr(n) {}
  
  void add(int from, int to, long long cap) {
    g[from].push_back({to, cap, 0, (int)g[to].size()});
    g[to].push_back({from, 0, 0, (int)g[from].size() - 1});
  }

  bool bfs(int s, int t) {
    fill(lvl.begin(), lvl.end(), -1);
    lvl[s] = 0;
    queue<int> q;
    q.push(s);
    while (!q.empty()) {
      int v = q.front();
      q.pop();
      for (auto& edge : g[v]) {
        if (edge.cap - edge.flow > 0 && lvl[edge.to] == -1) {
          lvl[edge.to] = lvl[v] + 1;
          q.push(edge.to);
        }
      }
    }
    return lvl[t] != -1;
  }

  long long dfs(int v, int t, long long pushed) {
    if (pushed == 0 || v == t) return pushed;
    for (int& cid = ptr[v]; cid < g[v].size(); ++cid) {
      auto& edge = g[v][cid];
      int tr = edge.to;
      if (lvl[v] + 1 != lvl[tr] || edge.cap - edge.flow == 0) continue;
      long long push = dfs(tr, t, min(pushed, edge.cap - edge.flow));
      if (push == 0) continue;
      edge.flow += push;
      g[tr][edge.rev].flow -= push;
      return push;
    }
    return 0;
  }

  long long max_flow(int s, int t) {
    long long flow = 0;
    while (bfs(s, t)) {
      fill(ptr.begin(), ptr.end(), 0);
      while (long long pushed = dfs(s,t,1e18)) flow += pushed;
    }
    return flow;
  }
  
  vector<pair<int, int>> min_cut(int s) {
    vector<bool> vis(n, false);
    queue<int> q;
    q.push(s);
    vis[s] = true;
    while (!q.empty()) {
      int v = q.front();
      q.pop();
      for (auto& edge : g[v]) {
        if (edge.cap - edge.flow > 0 && !vis[edge.to]) {
          vis[edge.to] = true;
          q.push(edge.to);
        }
      }
    }
    vector<pair<int, int>> cut_edges;
    for (int u = 0; u < n; ++u) {
      if (vis[u]) {
        for (auto& edge : g[u]) {
          if (!vis[edge.to] && edge.cap > 0) {
            cut_edges.push_back({u, edge.to});
          }
        }
      }
    }
    return cut_edges;
  }
};
