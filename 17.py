file = open('17.txt')
a = [int(x) for x in file]
file.close()

m2 = -float('inf')
for x in a:
    if len(str(abs(x))) == 2 and x > m2:
        m2 = x

count, sm = 0, -float('inf')
for i in range(len(a) - 1):
    rule1 = a[i] >= 0 and len(str(a[i])) == 3
    rule2 = a[i + 1] >= 0 and len(str(a[i + 1])) == 3
    rule3 = (a[i] + a[i + 1]) % m2 == 0
    if (rule1 or rule2) and rule3:
        count += 1
        sm = max(sm, a[i] + a[i + 1])
print(count, sm)