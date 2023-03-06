from fractions import gcd
def cf(num1,num2):
    n=[]
    g=gcd(num1, num2)
    for i in range(1, g+1): 
        if g%i==0: 
            n.append(i)
    return n
nums = [int(x) for x in input().split()]
cf(nums[0],nums[1])
result = n
print(len(result)
