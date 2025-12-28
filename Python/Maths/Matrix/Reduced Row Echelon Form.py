mod = 10**9 +7
e = 0 #1e-10
def invmod(x):
  res = 1
  y = mod-2
  while y>0:
    if y&1:
      res = res*x %mod
    x = x*x %mod
    y >>=1
  return res

def rref(a):
  """
  Computes the Reduced Row Echelon Form (RREF) of a matrix 
  using Gauss-Jordan elimination with partial pivoting.
  Args:
      a: A list of lists (matrix) of floats. Modified in-place.
  Returns:
      int: The rank of the matrix.
  """
  n = len(a)
  m = len(a[0])
  r = 0
  c = 0
  while c < m and r < n:
    # 1. Pivot Selection: Find the row with the largest absolute value in column c
    j = r
    for i in range(r + 1, n):
      if abs(a[i][c]) > abs(a[j][c]):
        j = i
    # 2. Zero Check: If the pivot is essentially zero, skip this column
    if abs(a[j][c]) == e:
      c += 1
      continue
    # 3. Swap Rows: Move the pivot row to the current row index r
    a[j], a[r] = a[r], a[j]
    # 4. Normalize the Pivot Row: Scale row r so the pivot becomes 1
    s = 1 * invmod(a[r][c])
    for k in range(m):
      a[r][k] = a[r][k] * s %mod
    # 5. Eliminate Other Entries: Make column c zero for all other rows
    for i in range(n):
      if i != r:
        t = a[i][c]
        for k in range(m):
          a[i][k] = (a[i][k] - t * a[r][k]) %mod
    r += 1
    c += 1
  return r
