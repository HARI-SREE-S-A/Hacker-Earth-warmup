### cirular list concept tram ride
station = int(input())
start = int(input())
finish = int(input())
charges =[int(x) for x in input().split()]
circle = list(range(1,station+1))

count = []
countt = []
index_strt = circle.index(start)
f = index_strt
r = f

for i in range(0,len(circle)+1):
    
    if circle[r] != finish:
        count.append(charges[r])
        r += 1
        if r > (len(circle)-1):
            r = 0
    else:
        break

for j in range(0,len(circle)+1):
    if circle[f] != finish:
        
        countt.append(charges[f-1])
        f -= 1
a,b = sum(count),sum(countt)

#print(countt)
print(min(a,b))

