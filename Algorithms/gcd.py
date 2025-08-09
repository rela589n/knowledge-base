def gcd(a, b):
  print("%d %d" % (a, b))
  while a > 0 and b > 0:
    if a > b:
      a = a % b
      print("%d %d" % (a, b))
    else:
      b = b % a
      print("%d %d" % (a, b))
  return a + b

print(gcd(int(input()), int(input())))
