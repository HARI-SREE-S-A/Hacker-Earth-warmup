dictn = {}

test = int(input("number of vaccines"))
lenn_virus = int(input("length"))
vi = list(input("virus"))




virus_list = (vi.count("C"))* "C" + (vi.count("G") * ("G" ))
virus_list = list(virus_list)

for b in range(test):
    virus_listss = (vi.count("C"))* "C" + (vi.count("G") * ("G" ))
    virus_lists  = list(virus_listss)
    
    j = int(input("length"))
    va = [str(x) for x in input("vaccines ")]
    for n in va:
       
        if n == "C" and "C" in virus_lists:
            #print(virus_lists)
            virus_lists.remove("C")
        elif n == "G" and "G" in virus_lists:
            #print(virus_lists)
            virus_lists.remove("G")
        dictn[b] = len(virus_lists)
        
    


   
#print(dictn)
nl = [1]*2
for k in range(test):
    nl[k] = dictn[k]
print( ( nl.index(max(nl)) )+1 )

