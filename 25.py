def f(N):
    for d in range(17, N, 10):
        if N % d == 0:
            return d
    return -1

N = 700_000 + 1
count = 0
while count != 5:
    res = f(N)
    if res != -1:
        print(N, res)
        count += 1
    N += 1

