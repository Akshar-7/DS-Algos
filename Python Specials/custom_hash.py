from time import time
htime = int(time())
def hash(x):
  m = 1<<64
  x += htime
  x = (x+0x9e3779b97f4a7c15)%m
  x = (x^(x>>30))* 0xbf58476d1ce4e5b9%m
  x = (x^(x>>27))* 0x94d049bb133111eb%m
  return x^(x>>31)
