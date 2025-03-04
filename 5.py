def f(N):
    bN = bin(N)[2:]
    bN = bN + bN[-2]
    bN = bN + bN[1]
    return int(bN, 2)

for N in range(2, 100):
    R = f(N)
    if R > 150:
        print(N)

