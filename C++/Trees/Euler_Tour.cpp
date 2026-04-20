int timer = 0;
vi st(n), end(n);
auto euler = [&](auto&& self, int x, int p) -> void{
  st[x] = timer++;
  for(auto v : g[x]){
    if (v==p) continue;
    self(self, v, x);
  }
  end[x] = timer;
};
euler(euler,0,0);
