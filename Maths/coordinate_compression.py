n = int(input())
a = [int(i) for i in input().split()]
b = sorted(a)
f = {}
for i in range(n):
  f[b[i]] = i
for i in range(n):
  a[i] = f[a[i]]
