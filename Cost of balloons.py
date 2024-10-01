

test = int(input())
for _ in range(test):
    dictn = {}
    a = []
    l = []
    prices = []
    test = int(input())


       
    prices = [int(y) for y in input().split()] ## getting the prices of each balloon
    
    n_ts = int(input())
    for k in range(n_ts):
        dictn[k] = [int(x) for x in input().split()]

    for p in range(1):
        for b in range(n_ts):
            a.append(dictn[b][p]) ### splitting the elements a column or "a" question scores 
    r = 1
    for c in range(n_ts):
        l.append(dictn[c][r]) ### splitting the elements b column or "b" question scores
    
    
    a_c = a.count(1) # counting the scores of  "a" question 
    
    b_c = l.count(1) # counting scores of "b" question
    
    
    C_ab = min(a_c,b_c) * max(prices[0],prices[1]) # finding optimal cost of "a" balloon
    
    C_bb = max(a_c,b_c) * min(prices[0],prices[1]) # finding optimal cost of "b" balloon
   
    print(C_ab + C_bb )

