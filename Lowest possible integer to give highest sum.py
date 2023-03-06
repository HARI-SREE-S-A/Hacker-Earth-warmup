length = int(input())
nums = sorted([int(x) for x in input().split()])
n_sum = sum(nums)

for n in nums:
    numm = n * length
    

    if numm> n_sum:
        print(n)
        break
