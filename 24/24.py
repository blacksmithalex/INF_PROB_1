file = open('24.txt')
a = file.readline()
file.close()

for k in range(1, 50):
    if 'CA' * k in a:
        print(k)
res = 'CA' * 27 + 'C'
print(res in a)
print(54)