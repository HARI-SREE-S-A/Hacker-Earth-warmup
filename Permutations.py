c = [int(y) for y in input().split()]
j = c[1]
per = [int(z) for z in input().split()]

l = []
b  = per
for _ in range(j):
    
    p = per
    
    k = [int(x) for x in input().split()]
    
    for i in range(k[0],k[1]+1):
        try:
            l.append(per[i])
        except IndexError:
            None
    print(l)
    for n in l:
        print(n)
        if n in per:
            b.remove(n)
        else:
            pass
    print((b))
