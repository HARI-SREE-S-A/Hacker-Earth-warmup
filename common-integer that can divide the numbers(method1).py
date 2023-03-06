nums = [int(x) for x in input().split()]
m = max(nums)
n = min(nums)
result = []
for i in range(1,m):
    print(n,m,i)
    if nums[0] % i == nums[1] % i == 0:
        print(i)
        result.append(i)
print(len(result))


