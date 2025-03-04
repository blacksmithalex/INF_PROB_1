file = open('9.txt')
count = 0
for line in file:
    line = sorted([int(x) for x in line.split()])
    if len(set(line)) == 5:
        s_minmax = line[0] + line[4]
        s_other = line[1] + line[2] + line[3]
        if s_minmax < s_other:
            count += 1
print(count)

