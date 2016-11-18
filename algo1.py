#!/usr/bin/python
# -*- coding: utf-8 -*-
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
    
def cout1Naif(c1,c2,t1,t2,cout_gap,cout_dif,dico):
    if t1 == t2 and t1 == 0:
        return cout(c1[t1],c2[t2],cout_dif)
    if t1 == 0:
        return t2*cout_gap
    if t2 == 0:
        return t1*cout_gap #y a t-il une réutilisation de variable
    return min(cout1Naif(c1,c2,t1-1,t2-1,cout_gap,cout_dif,dico) + cout(c1[t1],c2[t2],cout_dif),
               cout1Naif(c1,c2,t1,t2-1,cout_gap,cout_dif,dico) + cout_gap,
               cout1Naif(c1,c2,t1-1,t2,cout_gap,cout_dif,dico) + cout_gap)

def cout1(c1,c2,t1,t2,cout_gap,cout_dif,dico):
    if (t1, t2) in dico:
        #print (t1,t2), "in dico"
        return dico[(t1, t2)]
    if t1 == t2 and t1 == 0:
        dico[(t1, t2)] = cout(c1[t1],c2[t2],cout_dif)
        return dico[(t1, t2)]
    if t1 == 0:
        dico[(t1, t2)] = t2*cout_gap
        return dico[(t1, t2)]
    if t2 == 0:
        dico[(t1, t2)] = t1*cout_gap
        return dico[(t1, t2)]
    
    dico[(t1,t2)] = min(cout1(c1,c2,t1-1,t2-1,cout_gap,cout_dif,dico) + cout(c1[t1],c2[t2],cout_dif),
               cout1(c1,c2,t1,t2-1,cout_gap,cout_dif,dico) + cout_gap,
               cout1(c1,c2,t1-1,t2,cout_gap,cout_dif,dico) + cout_gap)
    #print (t1,t2), dico[(t1, t2)]
    return dico[(t1,t2)]
        
def sol1(t1,t2,cout_gap,cout_dif,dico):
    L = []
    i = t1
    j = t2
    cout = dico[(t1, t2)]
    #print ("cout : ", cout)

    # 1ere iteration pour initialiser la liste
    if dico[i-1, j-1] <= dico[i, j-1] and dico[i-1, j-1] <= dico[i-1, j]:
        #if dico[(i-1, j-1)] <= cout:
        L.append((i-1, j-1))
            #print ("J'ajoute", i-1, j-1, "vaut", dico[(i-1, j-1)])
        i = i-1
        j = j-1
    elif dico[i, j-1] <= dico[i-1, j-1] and dico[i, j-1] <= dico[i-1, j]:
        #if dico[(i, j-1)] <= cout:
            #print ("J'ajoute", i, j-1, "vaut", dico[(i, j-1)])
        L.append((i, j-1))
        j = j-1
    elif dico[i-1, j] <= dico[i-1, j-1] and dico[i-1, j] <= dico[i, j-1]:
        #if dico[(i-1, j)] <= cout:
            #print ("J'ajoute", i-1, j, "vaut", dico[(i-1, j)])
        L.append((i-1, j))
        i = i-1
    

    # on parcourt le dictionnaire et on prend le min
    # prend (66,60) dans l'alignement alors qu'il ne devrait pas
    # [..., (65, 59), (67, 61), ...]
    # gerer le cas ou ils sont tous egaux...
    
    while i > 0 and j > 0:
        print ("(i, j) = ", i , j)
        if dico[i-1, j-1] == dico[i, j-1] and dico[i, j-1] == dico[i-1, j]:
            print ("i, j egaux", i, j)
            i = i-1
            j = j-1
        elif dico[i-1, j-1] <= dico[i, j-1] and dico[i-1, j-1] <= dico[i-1, j]:
            #if dico[(i-1, j-1)] <= cout:
            L.append((i-1, j-1))
            print ("J'ajoute", i-1, j-1, "vaut", dico[(i-1, j-1)])
            i = i-1
            j = j-1
        elif dico[i, j-1] <= dico[i-1, j-1] and dico[i, j-1] <= dico[i-1, j]:
            #if dico[(i, j-1)] <= cout:
            if (j == L[-1][1]):
                print ("J'enleve", L[-1] , "vaut", dico[L[-1]])
                L.pop()
                print ("J'ajoute", i, j-1, "vaut", dico[(i, j-1)])
            L.append((i, j-1))
            j = j-1
        elif dico[i-1, j] <= dico[i-1, j-1] and dico[i-1, j] <= dico[i, j-1]:
            #if dico[(i-1, j)] <= cout:
            if (i == L[-1][0]):
                print ("J'enleve", L[-1] , "vaut", dico[L[-1]])
                L.pop()
                print ("J'ajoute", i-1, j, "vaut", dico[(i-1, j)])
            L.append((i-1, j))
            i = i-1
            
        
    L.reverse()
    return L


def afficheAlignement(chaine1, chaine2, t1, t2, align):
    nbGaps = 0
    c1 = chaine1
    c2 = chaine2
    for k in range(len(align)):
        i = align[k][0]
        j = align[k][1]
    
        if (i - j >= nbGaps):
            # il faut decaler les indices de "decoupage" avec le nombre de gaps ajoutes
            j += nbGaps
            
            # cas ou x_j est dans l'alignement ou pas
            if (j == align[k-1][0]):
                nbGaps += i-j-1
                c2 = c2[:j] + (i-j-1) * '-'  + c2[j:]
            else:
                nbGaps += i-j
                c2 = c2[:j] + (i - j) * '-'  + c2[j:]

        if (j > i):
            i += nbGaps

            # cas ou y_i est dans l'alignement ou pas
            if (i == align[k-1][1]):
                nbGaps += j-i-1
                c1 = c1[:i] + (j-i-1) * '-'  + c1[i:]
            else:
                nbGaps += j-i
                c1 = c1[:i] + (j-i) * '-'  + c1[i:]
    
            
    # rajoute des gaps a la sequence la plus courte des deux apres les insertions
    taille1 = len(c1)
    taille2 = len(c2)
    if len(c1) < len(c2):
        c1 = c1 + (len(c2) - len(c1))*'-'
    elif len(c2) < len(c1):
        c2 = c2 + (len(c1) - len(c2))*'-'

    print(c1)
    print(c2)
    return (c1, c2)

def coutAlign(c1, c2, cout_gap, cout_dif):
    cout = 0
    for i in range(min(len(c1), len(c2))):
        if c1[i] == '-' or c2[i] == '-':
            cout += cout_gap
        elif c1[i] != c2[i]:
            cout += cout_dif
    if (len(c1) < len(c2)):
        cout += (len(c2) - len(c1)) * cout_gap
    elif (len(c2) < len(c1)):
        cout += (len(c1) - len(c2)) * cout_gap
    return cout
        

if __name__ == "__main__":
    #L = lire_sequence("Inst_0000010_44.adn")
    L = lire_sequence("Inst_0000100_3.adn")
    dico = dict()
    COUT_GAP = 1
    COUT_DIFF = 1
    c = cout1(L[2],L[3],L[0],L[1],COUT_GAP,COUT_DIFF,dico)
    print(c)
    #print L[0], L[1]
    """
    for i in dico:
        if dico[i] <= 20:
            print (i, dico[i])
    """
    print("\n")
    
    print (dico[67, 61])
    print (dico[67, 60])
    print (dico[66, 61])
    print (dico[66, 60])
    
    align = sol1(L[0],L[1],COUT_GAP,COUT_DIFF,dico)
    print ("------- Alignement M : -------")
    print (align)
    print ("------------------------------")
    res = afficheAlignement(L[2], L[3], L[0], L[1], align)
    print(coutAlign(res[0], res[1], COUT_GAP, COUT_DIFF))
    
