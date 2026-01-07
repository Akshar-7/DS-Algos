f = {}
z = ord('a')
mod = [10**9 +7, 10**9 +9]
w = [29, 31]
k = [1]*2
hsh = [0]*2
for x in s:
  y = ord(x) -z
  for i in range(2):
    hsh[i] = (hsh[i] + k[i]*y %mod[i])
    k[i] = k[i] *w[i] %mod[i]
    tup = (hsh[0], hsh[1])
    f[tup] = f.get(tup, 0) +1
