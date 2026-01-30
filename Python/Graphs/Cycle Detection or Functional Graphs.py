a = succ(x)
b = succ(succ(x))
while (a != b): # tortoise hare algorithm
  a = succ(a)
  b = succ(succ(b))
a = x
while (a != b):
  a = succ(a)
  b = succ(b)
first = a  # first element of the cycle
# length of the cycle
b = succ(a)
length = 1
while (a != b):
  b = succ(b)
  length++
