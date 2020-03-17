#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:14:12 2018

@author: Paddy Jo
@title BwInf 2018 A3
"""
import math
# Der folgende Abschnitt dient zum Einlesen der Beispiele
readLuckyList = []

with open("A3beispiel3.txt") as file:
    readLuckyList = file.readlines()
 
luckyList = [] # Die luckyList ist die Liste mit den Zahlen, auf die die Besucher gesetzt haben.
luckyNumbers = [] # Die luckyNumbers sind die Zahlen, auf die Al setzen sollte.
for i in readLuckyList:
    i=i[:-1]
    luckyList.append(int(i))
luckyList.sort()

#Wenn die Liste weniger als 10 Eintraege hat,
# werden die Glueckszahlen direkt auf die gesetzten Stellen gesetzt:
if len(luckyList) <= 10:
    for i in luckyList:
        luckyNumbers.append(i)
    for y in range(10-len(luckyNumbers)):
        luckyNumbers.append(y+1)
else:
    """
    Der folgende Abschnitt dient dazu, eine bestimmte Anzahl 
    von gesetzten Stellen zu einer Liste zusammenzufassen
    (Im folgenden werden diese Listen als "Sublist" bezeichnet).
    Danach werden die 10 Sublisten in die intervallList eingefuegt, 
    sodass man ueber die intervallList am Ende alle
    Sublists abrufen kann.
    """
    
    minVal = math.floor(len(luckyList)/10)  # minVal ist die Menge der Zahlen, 
                                            # die mindestens in eine Sublist muss, 
                                            # sodass man am Ende alle Stellen in 10 
                                            # Sublisten aufgeteilt hat.
    
    intervallList = []
    tempIntervallList = []
    for i in luckyList:
        tempIntervallList.append(i)
        if len(tempIntervallList) == minVal:
            intervallList.append(tempIntervallList)
            tempIntervallList = []
    intervallList.append(tempIntervallList)
    
    if len(intervallList) == 10:
        while intervallList[10] is not None:    # Wenn Elemente uebrig waren, 
                                                # welche nun in einer 11. Sublist sind: 
            """
            Im folgenden Abschnitt werden die "uebrigen" Elemente aus der 11. Sublist
            moeglichst effizient auf die ersten 10 Sublisten verteilt.
            Als erstes wird berechnet, wie die Abstaende der Randelemente der 
            ersten 10 Sublisten sind.
            """
            v2List = []
            for i in range(1, len(intervallList)-1):
                v2List.append(intervallList[i][0] - intervallList[i-1][len(intervallList[i-1])-1])
            """
            Nun wird geschaut, bei welchen Sublisten diese Abstaende am kleinsten sind. 
            Der erste Wert in der v2List ist dabei der Abstand zwischen
            dem letzten Element in der ersten Sublist und dem ersten Element in der zweiten Sublist.
            Nach jeder Zuteilung eines weiteren Elements zu einer der Sublisten  wird der ganze 
            Vorgang wiederholt, damit sich durch die generelle
            Verschiebung aller Sublisten keine Fehler ergeben.
            """
            for repeat in range(len(intervallList[10])):
                tempMinVal = v2List[0]
                tempPosition = 0
                for y in range(len(v2List)-1):
                    if v2List[y] > tempMinVal and v2List[y] != -1:
                        tempMinVal = v2List[y]
                        tempPosition = y
            # Hier werden jetzt die Sublisten neu errechnet, wobei die Subliste an der Stelle 
            # tempPosition ein Element mehr zugeteilt bekommt:
            intervallList = []
            tempIntervallList = []
            i = 0
            while i < len(luckyList):
                tempIntervallList.append(luckyList[i])
                if len(tempIntervallList) == minVal:
                    if len(intervallList) == tempPosition:
                        tempIntervallList.append(luckyList[i+1])
                        i += 1
                    intervallList.append(tempIntervallList)
                    tempIntervallList = []
                i+=1
            intervallList.append(tempIntervallList)
            
    
    
    """
    Im folgenden Abschnitt werden die nun errechneten Sublists noch weiter optimiert, 
    indem zuerst die mittlere Abweichung der Elemente in 
    jeder Sublist berechnet wird. Danach wird die Abweichung zwischen dem letzten Element 
    einer Liste und dem ersten Element der naechsten Liste 
    errechnet. Ist diese Abweichung kleiner als die mittlere Abweichung beider Listen 
    und die mittlere Abweichung der ersten Liste kleiner als
    die der zweiten, so wird das Element aus der zweiten Liste in die erste geschoben.
    """
    vList = []
    for sublist in range(10):
        tempVList = []
        for position in range(1, len(intervallList[sublist])-1):
            tempVList.append(intervallList[sublist][position] - intervallList[sublist][position-1])
        sum = 0
        for i in tempVList:
            sum += i
        mVal = sum/len(tempVList)
        vList.append(mVal)
        
    v2List = []
    for i in range(1, len(intervallList)-1):
        v2List.append(intervallList[i][0] - intervallList[i-1][len(intervallList[i-1])-1])
    
    for index in range(1, len(intervallList)-1):
        if vList[index] > vList[index-1]:
            if v2List[index-1] < vList[index] and v2List[index-1] < vList[index-1]:
                toBeMoved = intervallList[index][0]
                intervallList[index-1].append(toBeMoved)
                intervallList[index].remove(toBeMoved)
            

    
    # Jetzt wird immer der Wert in der Mitte jeder Sublist zur luckyNumbers Liste hinzugefuegt.
    for i in intervallList:
        middle = len(i)/2
        middle = math.floor(middle)
        if middle != 0:
            luckyNumbers.append(i[int(middle)-1])

# Diese Funktion dient dazu, den Betrag einer Zahl zurueckzugeben.
def pos(val):
    if val<0:
        val*=-1
    return val
    
# Mit dieser Funktion wird der Gewinn von Al berechnet. Dazu werden zuerst seine Einnahmen 
# und dann seine Ausgaben berechnet. Die Differenz ist der Gewinn.
def calcWin():
    income = len(luckyList)*25
    loss= 0
    for i in luckyList:
        for y in luckyNumbers:
            if y>=i:
                diff1=pos(y-i)
                diff2=pos(luckyNumbers[luckyNumbers.index(y)-1]-i)
                loss+=min(diff1,diff2)
                break
    win=income-loss
    return win
                    
        
    
    
print("Auf diese Nummern sollte Al setzen:",luckyNumbers)
print("damit sein Gewinn dieser ist:",calcWin(),"$")