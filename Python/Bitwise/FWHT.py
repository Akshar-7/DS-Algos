def fwht(a, inv=False):
  """
  In-place Fast Walsh-Hadamard Transform.
  a: List of ints (length must be power of 2)
  inv: Boolean, set to True for inverse transform
  """
  n = len(a)
  if n == 1: return a
  b = 1
  while b < n:
    for i in range(0, n, 2*b):
      for j in range(b):
        u = a[i+j]
        v = a[i+b+j]
        # XOR Convolution Logic
        a[i+j] = u+v
        a[i+b+j] = u-v
    b <<= 1
  # Normalization for Inverse Transform
  if inv:
    for i in range(n):
      a[i] //= n
  return a 

def multiply_poly(a, b):
  """
  Returns the XOR convolution of two lists a and b.
  Computes C[k] = sum(A[i] * B[j]) for all i ^ j = k
  """
  n = 1
  sz = max(len(a), len(b))
  while n < sz: n <<= 1
  a.extend([0]*(n-len(a)))
  b.extend([0]*(n-len(b)))
  fwht(a, inv=False)
  fwht(b, inv=False)
  c = [a[i]*b[i] for i in range(n)]
  fwht(c, inv=True)
  return c

# Count ways to get XOR sum K from subset of [1, 2]
# Polynomial for {1}: x^0 + x^1 -> [1, 1, 0, 0] (representing 0 and 1)
# Polynomial for {2}: x^0 + x^2 -> [1, 0, 1, 0] (representing 0 and 2)
A = [1, 1]
B = [1, 0, 1]
C = multiply_poly(A, B)
# Expected: [1, 1, 1, 1] -> 1 way to get 0, 1, 2, 3
print(f"Convolution Result: {result}") 
