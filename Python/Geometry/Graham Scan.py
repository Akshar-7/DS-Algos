import math
def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def polar_angle(p1, p2):
    if p1[1] == p2[1]:
        return -math.pi
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    return math.atan2(dy, dx)

def graham(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))
    hull = []
    for i in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    return hull
