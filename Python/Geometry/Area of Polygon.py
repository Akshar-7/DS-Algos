def polygon_area(pt):
  n = len(pt) 
  area = 0
  for i in range(n):
    j = (i+1) %n
    x1,y1 = pt[i]
    x2,y2 = pt[j]
    area += (x1 * y2 - y1 * x2)
  return abs(area)/2
