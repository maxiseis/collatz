cache = {1: 0}  # known sequence lengths

n = 1
max_steps = 0

while True:
    x = n
    path = []

    while x not in cache:
        path.append(x)
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1

    steps = cache[x]

    for i, v in enumerate(reversed(path)):
        steps += 1
        cache[v] = steps

    if cache[n] > max_steps:
        max_steps = cache[n]
        print(f"New record: n={n} steps={max_steps}")

    n += 1