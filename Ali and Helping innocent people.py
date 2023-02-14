n = input()
vow = ["A","E","I","O","U","Y"]

if n[2] not in vow:
    if n[0].isnumeric() and n[1].isnumeric() and n[3].isnumeric() and n[4].isnumeric() and n[5].isnumeric() and n[7].isnumeric() and n[8].isnumeric():
        if (int(n[0]) + int(n[1]))%2 == 0  and (int(n[3]) + int(n[4]))%2 == 0 and (int(n[4]) + int(n[5]))%2 == 0 and (int(n[7]) + int(n[8]))%2 == 0 :
            print(True)
        else:
            print("valid")
    else:
        print("False2")
else:
    print("False3")

