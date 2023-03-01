test  = int(input())
ans = 0
for _ in range(0,test):
    N = int(input())
    ans = 0
    for i in range (1,N+1):
        ans += int(N/i)
print(ans)

