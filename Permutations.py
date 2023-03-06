c = [int(y) for y in input().split()]
j = c[1]
per = [int(z) for z in input().split()]


for _ in range(j):
    
    p = per
    
    k = [int(x) for x in input().split()]
    
    for i in range(k[0],k[1]):
        try:
            p.remove(per[i])
        except IndexError:
            None
    print(max(p))
        
    
