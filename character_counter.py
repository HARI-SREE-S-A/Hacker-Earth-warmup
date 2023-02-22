def solve (S, k):
    b = S.count(k)
    return b
    pass

T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print (out_)
