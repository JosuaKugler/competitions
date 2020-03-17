import pprint

def erastothenes(cancelled, cancelnumber, modul):
    """
    Wir betrachten Zahlen von 1 bis 100, aus denen die Nicht-Primzahlen gestrichen werden sollen.
    cancelled ist eine Liste der bereits gestrichenen Zahlen
    cancelnumber ist die Primzahl, bezüglich der gekürzt werden soll
    modul ist der Rest, den 0 (eins unseres Intervalls -1) modulo dieser Zahl lässt
    gibt eine Liste der neugekürzten sowie eine Liste aller gekürzten Zahlen zurück
    """

    newcancelled = []

    for i in range(1,101):
        if (i+modul)%cancelnumber == 0:
            if i not in cancelled:
                newcancelled.append(i)
    cancelled = cancelled + newcancelled

    return cancelled

cases = {}
cancelled = []
cancelled = erastothenes(cancelled, 2, 0)
cancelled = erastothenes(cancelled, 5, 0)

cancelled.sort()


for i in range(3):
    cases[i] = erastothenes(cancelled, 3, i)
    if 100 - len(cases[i]) > 23:
        temp1 = cases[i]
        cases[i] = {}
        for j in range(7):
            cases[i][j] = erastothenes(temp1, 7, j)
            if 100 - len(cases[i][j]) > 23:
                temp2 = cases[i][j]
                cases[i][j] = {}
                for k in range(11):
                    cases[i][j][k] =  erastothenes(temp2, 11, k)
                    if 100 - len(cases[i][j][k]) > 23:
                        temp3 = cases[i][j][k]
                        cases[i][j][k] = {}
                        for l in range(13):
                            cases[i][j][k][l] = True
                            temp4 = erastothenes(temp3, 13, k)
                            if 100 - len(temp4) > 23:
                                cases[i][j][k][l] = False
                    else:
                        cases[i][j][k] = True
            else:
                cases[i][j] = True
    else:
        cases[i] = True
                            
pprint.pprint(cases)


#%%
cancelled = []
cancelled = erastothenes(cancelled, 2, 0)
cancelled = erastothenes(cancelled, 5, 0)

for i in range(3):
    for j in range(7):
        for k in range(11):
            for l in range(13):
                temp = erastothenes(erastothenes(erastothenes(erastothenes(cancelled, 13, l), 11, k), 7, j), 3, i)
                if 100- len(temp) > 23:
                    print(i, j, k, l)