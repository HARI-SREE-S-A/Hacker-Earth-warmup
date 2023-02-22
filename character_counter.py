def solve (S, k):
    S.count(k)
    pass

T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print (out_)
