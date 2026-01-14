# Only works for odd values of 'n'

def magic_square(n):
  magic = [[0]*n for i in range(n)]
  x = 1
  i, j = 0, n//2
  while x <= n*n:
    magic[i][j] = x
    x += 1
    ni, nj = (i-1) %n, (j+1) %n
    if magic_matrix[ni][nj]:
        i = (i+1) %n
    else:
        i, j = ni, nj
  return magic
