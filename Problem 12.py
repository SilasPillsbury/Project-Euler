def divCount(n):
  #accepts and outputs integers
  i = 2
  #count starts at two because two factors are assumed: 1 and n
  count = 3
  div = []
  while i < n:
    if n%i == 0:
      count += 1
      div.append(i)
      n = n/i
      i = 2
    else:
      i += 1
  return count
  

def run():
  tri = 1
  i = 2
  while divCount(tri) <= 500:
    tri += i
    print(tri)
    i += 1
  return i
