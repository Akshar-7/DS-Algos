def get_lps(s):
  lps = [0]*len(s)
  i = 1; j = 0
  while i < len(s):
    if s[i] == s[j]:
      j += 1
      lps[i] = j
      i +=1
    elif j>0:
      j = lps[j-1]
    else:
      lps[i] = 0
      i += 1
  return lps

def kmp(s1, s2):
  n, m = len(s1), len(s2)
  if m > n:
    return -1
  if m == n:
    return 0 if s2 == s1 else -1
  if s2 == "":
    return 0
  lps = get_lps(s2)
  i, j = 0, 0
  while i<n and j<m:
    if s1[i] == s2[j]:
      i += 1;  j += 1
    elif j > 0:
      j = lps[j-1]
    else:
      i += 1
  return -1 if j < m else i-m
