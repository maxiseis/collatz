n = int(input("Which Number("x" if forever):"))
steps = 0

while n != 1:
  if n % 2 == 0:
    n // 2
  else:
    n * 3 + 1
  steps += 1
print(1, steps)
