z = ord('a')
mod = [10**9 +7, 10**9 +9]
k = [29, 31]

def insert(s):
  w = [1]*2; hsh = [0]*2
  for x in s:
    y = ord(x) -z +1
    for i in range(2):
      hsh[i] = (hsh[i] + y*w[i]) %mod[i]
      w[i] = w[i] * k[i] %mod[i]
      tup = (hsh[0], hsh[1])
      f[tup] = f.get(tup, 0) +1

def count(s):
  w = [1]*2; hsh = [0]*2; res = 0
  for x in s:
    y = ord(x) -z +1
    for i in range(2):
      hsh[i] = (hsh[i] + y*w[i]) %mod[i]
      w[i] = w[i] * k[i] %mod[i]
      tup = (hsh[0], hsh[1])
      res += f.get(tup, 0)
  return res

f = {}
