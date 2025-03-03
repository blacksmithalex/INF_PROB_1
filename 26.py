file = open('26-143.txt')
N = file.readline()
data = sorted([[int(x) for x in line.split()] for line in file])
file.close()

count1, out = 0, 0 #заправились на 1 / уехали
q1, q2 = [], [] #время окончания обслуживания в 1 / 2 колонке
for start, time, type in data:
    q1 = [x for x in q1 if x > start]
    q2 = [x for x in q2 if x > start]
    if type == 1 or (type == 0 and len(q1) <= len(q2)):
        if len(q1) >= 5:
            out += 1
            continue
        if len(q1) == 0:
            q1.append(start + time)
        else:
            q1.append(max(q1) + time)
        count1 += 1
    else:
        if len(q2) >= 5:
            out += 1
            continue
        if len(q2) == 0:
            q2.append(start + time)
        else:
            q2.append(max(q2) + time)
print(count1, out)
