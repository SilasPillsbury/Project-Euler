def run():
  a = 1
  c = 3
  while a < 1000:
    b = a+1
    while b < c:
      c = 1000-a-b
      if a**2 + b**2 == c**2:
        return a,b,c
      print(a,b,c)
      b += 1
    a += 1
        
