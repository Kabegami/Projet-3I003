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

def cout(v1,v2,cout_dif):
    if v1 != v2:
        return cout_dif
    return 0
    
def cout1(c1,c2,t1,t2,cout_gap,cout_dif,dico):
    if t1 == t2 and t1 == 0:
        return cout(c1[t1],c2[t2],cout_dif)
    if t1 == 0:
        return t2*cout_gap
    if t2 == 0:
        return t1*cout_gap
    #y a t-il une réutilisation de variable
    dico[(t1,t2)] = min(cout1(c1,c2,t1-1,t2-1,1,1,dico) + cout(c1[t1],c2[t2],cout_dif),
               cout1(c1,c2,t1,t2-1,1,1,dico) + cout_gap,
               cout1(c1,c2,t1-1,t2,1,1,dico) + cout_gap)
    return dico[(t1,t2)]

if __name__ == "__main__":
    L = lire_sequence("Inst_0000010_44.adn")
    dico = dict()
    c = cout1(L[2],L[3],L[0],L[1],1,1,dico)
    print(c)
