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

def cout1(c1,c2,n,m,dif,gap,dico):
    for i in range(-1,n+1):
        dico[(i,-1)] = i*gap
    for j in range(0,m+1):
        dico[(-1,j)] = j*gap
    for i in range(0,n+1):
        for j in range(0,m+1):
            dico[(i,j)] = min(dico[(i-1,j-1)]+cout(c1[i-1],c2[j-1],dif),
                            dico[(i-1,j)] + gap,
                            dico[(i,j-1)] + gap)
    return dico[(n,m)]

def sol1(c1,c2,n,m,cout_gap,cout_dif,dico):
    L = []
    X = ""
    Y = ""
    i = n
    j = m
    
    while i!= -1 and j != -1:
        if dico[(i,j)] == dico[(i-1, j-1)] + cout(c1[i],c2[j],cout_dif):
            L.append((i,j))
            X += c1[i]
            Y += c2[j]
            (i,j) = (i-1,j-1)
        else:
            if dico[(i,j)] == dico[(i-1,j)] + cout_gap:
                X += '-'
                Y += c2[j]
                (i,j) = (i-1,j)
            else:
                X += c1[i]
                Y += '-'
                (i,j) = (i,j-1)
    print((i,j))
    L.reverse()
    print(X)
    print(Y)
    return (L)

def Alignement(chaine1,chaine2,t1,t2,align):
    print("entrer fonction alignement")
    i = 1
    j = 1
    c1 = ""
    c2 = ""
    for paire in align:
        while i != paire[0]:
            c1 += "-"
            i += 1
        c1 += chaine1[paire[0]]
        while j != paire[1]:
            c2 += "-"
            j += 1
        c2 += chaine2[paire[1]]
    print(c1)
    print(c2)
    return (c1,c2)
            
            

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
    COUT_GAP = 1
    COUT_DIFF = 1
    c = cout1(L[2],L[3],L[0],L[1],COUT_DIFF,COUT_GAP,dico)
    print(c)
    align = sol1(L[2],L[3],L[0],L[1],COUT_GAP,COUT_DIFF,dico)
    print("-------- Alignement--------")
    print(align)
    print("---------------------------")
    res = afficheAlignement(L[2], L[3], L[0], L[1], align)
    print(coutAlign(res[0], res[1], COUT_GAP, COUT_DIFF))
