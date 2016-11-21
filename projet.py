import numpy as np
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

def delta(a, b,dif=1):
    if a == b:
        return 0
    else:
        return dif


def cout1(x, y, gap=1,dif=1):
    m, n = len(x), len(y)
    F = np.zeros((m+1, n+1), dtype=int)
    for i in range(1, m+1):
        F[i, 0] = i * gap
    for j in range(1, n+1):
        F[0, j] = j * gap
    for i in range(1, m+1):
        for j in range(1, n+1):
            F[i, j] = min(F[i-1, j-1] + delta(x[i-1], y[j-1],dif),
                          F[i-1, j] + gap,
                          F[i, j-1] + gap)
    return F


def sol1(x, y, F, gap=1,dif=1):
    i, j = len(x), len(y)
    M = []
    while (i, j) != (0, 0):
        if i > 0 and j > 0 and F[i, j] == F[i-1, j-1] + delta(x[i-1], y[j-1],dif):
            M.append((i, j))
            i, j = i-1, j-1
        elif i > 0 and F[i, j] == F[i-1, j] + gap:
            i -= 1
        else:
            j -= 1
    M.reverse()
    return M


def affiche(x, y, M,F,gap,dif):
    #Quand on rajoute la paire (xn,ym) a notre allignement cela pose des problemes."
    #if F[len(x),len(y)] + delta(x[len(x)-1],y[len(y)-1],dif) <= F[len(x)-1,len(y)-1] + gap:
    M.append((len(x)+1, len(y)+1))
    i, j = 1, 1
    sx, sy = '', ''
    print("M : ", M)
    for (u, v) in M:
        while i < u and j < v:
            sx = sx + x[i-1]
            sy = sy + y[j-1]
            i, j = i+1, j+1
        while i < u:
            sx = sx + x[i-1]
            sy = sy + '-'
            i += 1
        while j < v:
            sx = sx + '-'
            sy = sy + y[j-1]
            j += 1
    print(sx)
    print(sy)
    return (sx,sy)

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

def coutAlign2(c1,c2,gap,dif):
    cout = 0
    for i in range(len(c1)):
        if c1[i] == '-' or c2[i] == '-':
            cout += gap
        else:
            if c1[i] != c2[i]:
                cout += dif

    return cout


# test
if __name__ == "__main__":
    L = lire_sequence("Inst_0000010_44.adn")
     #L = lire_sequence("Inst_0000100_3.adn")
    x = L[2]
    y = L[3]
    #x = "ATG"
    #y = "C"
    #l'algorithme marche quand COUT_GAP >= COUT_DIF mais pas l'inverse 
    COUT_GAP = 2
    COUT_DIF = 30
    F = cout1(x,y,COUT_GAP,COUT_DIF)
    print('cout total :', F[len(x), len(y)])
    
    M = sol1(x, y, F,COUT_GAP,COUT_DIF)
    print('alignements :', M)
    (c1,c2) = affiche(x, y, M,F,COUT_GAP,COUT_DIF)
    print("cout align : ", coutAlign2(c1,c2,COUT_GAP,COUT_DIF))
