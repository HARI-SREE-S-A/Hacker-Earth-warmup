L = int(input())
N = int(input())
dictn = {}

for _ in range(N):
    dictn[_]  = [int(x) for x in input().split()]

for k in range(N):
    b = dictn[k]
   
    if b[0] or b[1] < L:
        print(b[0],b[1])
        print("UPLOAD ANOTHER")
    elif b[0] and b[1] >= L:
        if b[0] == b[1]:
            print("ACCEPTED")
        else:
            print("CROP IT")
       
