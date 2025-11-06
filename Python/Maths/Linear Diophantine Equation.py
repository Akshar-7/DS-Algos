def find_any_solution(a, b, c):
  g, x0, y0 = gcd(abs(a), abs(b))
  if c % g != 0:
    return False, 0, 0, 0  # No solution
  x0 = x0 * (c // g)
  y0 = y0 * (c // g)
  if a < 0: x0 = -x0
  if b < 0: y0 = -y0
  return True, x0, y0, g

def shift_solution(x, y, a, b, cnt):
  x += cnt * b
  y -= cnt * a
  return x, y

def find_all_solutions(a, b, c, minx, maxx, miny, maxy):
  has_solution, x, y, g = find_any_solution(a, b, c)
  if not has_solution:
    return 0
  a //= g
  b //= g
  sign_a = 1 if a > 0 else -1
  sign_b = 1 if b > 0 else -1
  x, y = shift_solution(x, y, a, b, (minx - x) // b)
  if x < minx:
    x, y = shift_solution(x, y, a, b, sign_b)
  if x > maxx:
    return 0
  lx1 = x
  x, y = shift_solution(x, y, a, b, (maxx - x) // b)
  if x > maxx:
    x, y = shift_solution(x, y, a, b, -sign_b)
  rx1 = x

  x, y = shift_solution(x, y, a, b, -(miny - y) // a)
  if y < miny:
    x, y = shift_solution(x, y, a, b, -sign_a)
  if y > maxy:
    return 0
  lx2 = x
  x, y = shift_solution(x, y, a, b, -(maxy - y) // a)
  if y > maxy:
    x, y = shift_solution(x, y, a, b, sign_a)
  rx2 = x
  if lx2 > rx2:
    lx2, rx2 = rx2, lx2
  lx = max(lx1, lx2)
  rx = min(rx1, rx2)
  if lx > rx:
    return 0
  return (rx-lx) //abs(b) +1
