sub = mask
while True:
  # Do something
  sub = (sub-1)&mask
  if sub==0: break

sup = mask
while sup < (1<<n):
  # Do something
  sup = (sup+1)|mask
