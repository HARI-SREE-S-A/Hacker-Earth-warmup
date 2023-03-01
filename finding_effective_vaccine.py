vi = list("AAGCCU")


va = list("BBGCUU")
vb = "CCGGUU"
vil =[1]*2
val = [1]*2
vbl = [1]*2

virus_list = (vi.count("C"))* "C" + (vi.count("G") * ("G" ))
virus_list = list(virus_list)
print(virus_list)

for n in va:
    if n == "C":
        virus_list.remove("C")
    elif n == "G":
        virus_list.remove("G")

val[0] = va.count("C")
val[1]= va.count("G")

vbl[0] = vb.count("C")
vbl[1]= vb.count("G")

virus_list
