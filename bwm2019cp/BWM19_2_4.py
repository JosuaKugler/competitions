def erastothenes(cancelled, cancelnumber, modul):
    """
    Wir betrachten Zahlen von 1 bis 100, aus denen die Nicht-Primzahlen gestrichen werden sollen.
    cancelled ist eine Liste der bereits gestrichenen Zahlen
    cancelnumber ist die Primzahl, bezueglich der gekürzt werden soll
    modul ist der Rest, den 0 (eins unseres Intervalls -1) modulo dieser Zahl laesst
    gibt eine Liste der neugekürzten sowie eine Liste aller gekürzten Zahlen zurück
    """

    newcancelled = []

    for i in range(1,101):
        if (i+modul)%cancelnumber == 0:
            if i not in cancelled:
                newcancelled.append(i)
    cancelled = cancelled + newcancelled

    return cancelled, newcancelled

def case3_7_table():
    table = []
    table.append(r"\begin{tabular}{||c|c|l|c||}")
    table.append(r"i&j&durch 3 oder 7, aber nicht durch 2 oder 5 teilbar&n\\")
    cancelled = []
    cancelled, newcancelled = erastothenes(cancelled, 2, 0)
    cancelled, newcancelled = erastothenes(cancelled, 5, 0)
    for i in range(3):
        for j in range(7):
            cancelledby3, newcancelled1 = erastothenes(cancelled, 3, i)
            temp, newcancelled2 = erastothenes(cancelledby3, 7, j)
            newcancelled = newcancelled1 + newcancelled2
            nprimes = len(newcancelled)+60
            if 100-nprimes > 23:
                nprimes = r"\textcolor{red}{"+str(nprimes)+r"}"
            else:
                nprimes = str(nprimes)
            newcancelled.sort()
            numbers = ""
            for number in newcancelled:
                numbers += r"\textbf{"+str(number)+r"}, "
            table.append(str(i) + r"&"+ str(j) + r"&" + numbers[:-2]+r"&"+nprimes+r"\\")
    table.append(r"\end{tabular}")
    return table

def case11_table():
    table1 = []
    table2 = []
    table1.append(r"\begin{tabular}{||c|c|l|c||}")
    table1.append(r"j&l&durch 11 teilbar$^{\mathrm{a}}$&n\\")
    table2.append(r"\begin{tabular}{||c|c|l|c||}")
    table2.append(r"j&l&durch 11 teilbar\footnote{aber nicht durch 2,3,5, oder 7 teilbar}&n\\")
    cancelled = []
    cancelled, newcancelled = erastothenes(cancelled, 2, 0)
    cancelled, newcancelled = erastothenes(cancelled, 5, 0)
    linecounter = 0
    for i in range(3):
        for j in range(7):
            cancelledby3and7 = erastothenes(erastothenes(cancelled, 3, i)[0], 7, j)[0]
            if 100 - len(cancelledby3and7) > 23:
                for k in range(11):
                    totalcancelled, newcancelledby11 = erastothenes(cancelledby3and7, 11, k)
                    if len(totalcancelled) < 77:
                        nprimes = r"\textcolor{red}{"+str(len(totalcancelled))+r"}"
                    else:
                        nprimes = str(len(totalcancelled))
                    newcancelledby11.sort()
                    numbers = ""
                    for number in newcancelledby11:
                        numbers += r"\textbf{"+str(number)+r"}, "
                    if linecounter < 28:
                        table1.append(str(j) + r"&"+ str(k) + r"&" + str(numbers)[:-2]+r"&"+nprimes+r"\\")
                        linecounter += 1
                    else:
                        table2.append(str(j) + r"&"+ str(k) + r"&" + str(numbers)[:-2]+r"&"+nprimes+r"\\")

    table1.append(r"\end{tabular}")
    table2.append(r"\end{tabular}")
    return table1, table2

def case13_table():
    table1 = []
    table2 = []
    table1.append(r"\begin{tabular}{||c|c|c|l|c||}")
    table1.append(r"j&l&m&durch 13 teilbar$^{\mathrm{a}}$&n\\")
    table2.append(r"\begin{tabular}{||c|c|c|l|c||}")
    table2.append(r"j&m&m&durch 13 teilbar\footnote{aber nicht durch 2,3,5,7, oder 11 teilbar}&n\\")
    cancelled = []
    cancelled, newcancelled = erastothenes(cancelled, 2, 0)
    cancelled, newcancelled = erastothenes(cancelled, 5, 0)
    linecounter = 0
    for i in range(3):
        for j in range(7):
            cancelledby3and7 = erastothenes(erastothenes(cancelled, 3, i)[0], 7, j)[0]
            if 100 - len(cancelledby3and7) > 23:
                for k in range(11):
                    cancelledby37and11 = erastothenes(cancelledby3and7, 11, k)[0]
                    if len(cancelledby37and11) < 77:
                        for l in range(13):
                            totalcancelled, newcancelledby13 = erastothenes(cancelledby37and11, 13, l)
                            if len(totalcancelled) < 77:
                                nprimes = r"\textcolor{red}{"+str(len(totalcancelled))+r"}"
                            else:
                                nprimes = str(len(totalcancelled))
                            newcancelledby13.sort()
                            numbers = ""
                            for number in newcancelledby13:
                                numbers += r"\textbf{"+str(number)+r"}, "
                            if linecounter < 39:
                                table1.append(str(j) + r"&"+ str(k) + r"&"+ str(l) + r"&" + str(numbers)[:-2]+r"&"+nprimes+r"\\")
                                linecounter += 1
                            else:
                                table2.append(str(j) + r"&"+ str(k) + r"&"+ str(l) + r"&" + str(numbers)[:-2]+r"&"+nprimes+r"\\")
                    
    table1.append(r"\end{tabular}")
    table2.append(r"\end{tabular}")
    return table1,table2

table1, table2 = case13_table()
for line in table1:
    print(line)

for line in table2:
    print(line)
