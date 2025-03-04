for n in range(101, 1000):
    s = '1' * n
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(f'Длина = {n}, кол-во единиц: {s.count('1')}')
