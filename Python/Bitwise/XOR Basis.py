lg = 32
def insert(x):
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    if bs[i]==0:
      bs[i] = x
      break
    x ^= bs[i]

def query(x):
  for i in range(lg-1, -1, -1):
    if x&1<<i==0: continue
    x ^= bs[i]
  return x==0

