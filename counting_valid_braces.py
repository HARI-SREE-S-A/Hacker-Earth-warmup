name = str(input())
a = name.count("(")
b = name.count(")")

if b - a == 0:
    print((len(name)//2))
else:
    l = min(a,b)
    print(l)
    
