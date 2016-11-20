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

#--------------------------------------------
#           TEST
#--------------------------------------------

def cout2(c1,c2,t1,t2,cout_gap,cout_dif,dico,fils):
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

    #print("test")
    F1 = cout2(c1,c2,t1-1,t2-1,cout_gap,cout_dif,dico,fils) + cout(c1[t1],c2[t2],cout_dif)
    F2 = cout2(c1,c2,t1,t2-1,cout_gap,cout_dif,dico,fils) + cout_gap
    F3 = cout2(c1,c2,t1-1,t2,cout_gap,cout_dif,dico,fils) + cout_gap
    #print("test")
    if F1 <= F2 and F1 <= F3:
        dico[(t1,t2)] = F1
        fils[(t1,t2)] = (t1-1,t2-1)
    elif F2 <= F1 and F2 <= F3:
        dico[(t1,t2)] = F2
        fils[(t1,t2)] = (t1,t2-1)
    elif F3 <= F1 and F3 <= F2:
        dico[(t1,t2)] = F3
        fils[(t1,t2)] = (t1-1,t2)
    #print("fils :",fils)
    return dico[(t1,t2)]

def descente(t1,t2,fils,dico,cout_diff,cout_gap):
    i = t1
    j = t2
    L = []
    L2 = []
    while (i,j) in fils:
        if fils[(i,j)] == (i-1,j-1):
            L.append((i,j))
        L2.append((i,j))
        c1 = fils[(i,j)][0]
        c2 = fils[(i,j)][1]
        i = c1
        j = c2
    L.append((i,j))
    L2.append((i,j))
    L.reverse()
    L2.reverse()
    return (L,L2)
    

def sol1(t1,t2,cout_gap,cout_dif,dico):
    L = []
    i = t1
    j = t2
    
    while (i,j) != (0,0):
        print(dico[(i,j)],dico[(i-1,j-1)])
        if dico[(i-1, j-1)] + cout(i,j,cout_dif) == dico[(i,j)]:
            L.append((i,j))
            (i,j) = (i-1,j-1)
        else:
            if dico[(i,j)] == dico[(i-1,j)] + cout_gap:
                (i,j) = (i-1,j)
            else:
                (i,j) = (i,j-1)
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
    L = lire_sequence("Inst_0000010_44.adn")
    #L = lire_sequence("Inst_0000100_3.adn")
    dico = dict()
    fils = dict()
    #fils = dict()
    COUT_GAP = 1
    COUT_DIFF = 1
    #c = cout1(L[2],L[3],L[0],L[1],COUT_GAP,COUT_DIFF,dico)
    #print(c)
    c2 = cout2(L[2],L[3],L[0],L[1],COUT_GAP,COUT_DIFF,dico,fils)
    (des, inv) = descente(L[0],L[1],fils,dico,COUT_DIFF,COUT_GAP)
    #align = sol1(L[0],L[1],COUT_GAP,COUT_DIFF,dico)
    print ("------- Alignement M : -------")
    #print ("sol 1 ",align)
    print("descente : ",des)
    print("inverse : ",inv)
    print ("------------------------------")
    res = afficheAlignement(L[2], L[3], L[0], L[1], des)
    #print(coutAlign(res[0], res[1], COUT_GAP, COUT_DIFF))
    
