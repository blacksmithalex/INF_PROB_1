file = open('24.txt')
a = file.readline()
file.close()

count, countm = 0, 0
for x in a:
    if (x == 'C' and count % 2 == 0) or (x == 'A' and count % 2 == 1):
        count += 1
        countm = max(count, countm)
    elif x == 'C':
        count = 1
    else:
        count = 0
print(countm)