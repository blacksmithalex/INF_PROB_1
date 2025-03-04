def F(x, y, z, w):
    l1 = x or (not y)
    l2 = not(x == z)
    return int(l1 and l2 and w)

print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w) == 1:
                    print(x, y, z, w, '|', F(x, y, z, w))


