dictn = {}
a = []
l = []
for k in range(3):
    dictn[k] = [int(x) for x in input().split()]
for p in range(1):
    for b in range(3):
        a.append(dictn[b][p])
r = 1
for c in range(3):
    l.append(dictn[c][r])
a_c = a.count(1)
b_c = l.count(1)
print(a_c,b_c)


