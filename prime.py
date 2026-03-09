n = 3

def check_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True  
while True:
  print(check_prime(n))
  n += 1
