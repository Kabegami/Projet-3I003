import os

def lire_sequence(fichier):
    os.chdir('test')
    f = open(fichier,'r')
    sequence = f.read()
    L = sequence.splitlines()
    L2 = []
    L2.append(int(L[0])-1)
    L2.append(int(L[1])-1)
    L2.append(L[2].replace(" ",""))
    L2.append(L[3].replace(" ",""))
    if (L2[0]) < 100 and L2[1] < 100:
        print(L2[2])
        print(L2[3])
    return L2
    f.close()

def cout1bis(c1, c2, t1, t2, cout_gap, cout_dif, dico):
    if t1 > t2:
        for i in range(t2, t1):
            c2 += '-'
    else:
        for i in range(t1, t2):
            c1 += '-'

    if c2[t2] == '-':
        return cout1bis(c1, c2, t1-1, t2, cout_gap, cout_dif, dico) + cout_gap
    if c1[t1] == '-':
        return cout1bis(c1, c2, t1, t2-1, cout_gap, cout_dif, dico) + cout_gap
    if c1[t1] != c2[t2]:
        return cout1bis(c1, c2, t1-1, t2-1, cout_gap, cout_dif, dico) + cout_diff
    else:
        return cout1bis(c1, c2, t1-1, t2-1, cout_gap, cout_dif, dico)

    
def cout1(c1,c2,t1,t2,cout_gap,cout_dif,dico):
    if (t1,t2) in dico:
        return dico[(t1,t2)]
    if t1 < t2:
        V = cout1(c1,c2,t1,t2-1,cout_gap,cout_dif,dico) + cout_gap
        dico[(t1,t2)] = V
        return V
    
    if t1 > t2:
        V = cout1(c1,c2,t1-1,t2,cout_gap,cout_dif,dico) + cout_gap
        dico[(t1,t2)] = V
        return V
    if t1 == 0 and t2 == 0:
        if c1[t1] == c2[t2]:
            ct = 0
        else:
            ct = cout_dif
        return ct
            
    if t1 == 0:                 
        return t2*cout_gap
    if t2 == 0:
        return t1*cout_gap
    if t1 == t2:
        if c1[t1] == c2[t2]:
            ct = 0
        else:
            ct = cout_dif
        V = cout1(c1,c2,t1-1,t2-1,cout_gap,cout_dif,dico) + ct
        dico[(t1,t2)] = V    
        return V

    

if __name__ == "__main__":
    L = lire_sequence("Inst_0000010_44.adn")
    dico = dict()
    c = cout1bis(L[2],L[3],L[0],L[1],1,1,dico)
    print(c)
