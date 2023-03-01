dictn = {}
vi = list("AAGCCU")


va = list("BBGCUU")
vb = "CCGGUU"
vil =[1]*2
val = [1]*2
vbl = [1]*2

virus_list = (vi.count("C"))* "C" + (vi.count("G") * ("G" ))
virus_list = list(virus_list)

for b in range(2):
    virus_listss = (vi.count("C"))* "C" + (vi.count("G") * ("G" ))
    virus_lists  = list(virus_listss)
    
    
    va = [str(x) for x in input()]
    for n in va:
       
        if n == "C" and "C" in virus_lists:
            #print(virus_lists)
            virus_lists.remove("C")
        elif n == "G" and "G" in virus_lists:
            #print(virus_lists)
            virus_lists.remove("G")
        dictn[b] = len(virus_lists)
        
    


   
print(dictn)
nl = [1]*2
for k in range(2):
    nl[k] = dictn[k]
print( ( nl.index(max(nl)) )+1 )
