
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

cancelled = []
cancelled = erastothenes(cancelled, 2, 0)
cancelled = erastothenes(cancelled, 5, 0)

cases = {}
for i in range(3):
    cases[i] = {}
    for j in range(7):
        cases[i][j] = erastothenes(erastothenes(cancelled, 3, i), 7, j)

import pprint

pprint.pprint(cases)
