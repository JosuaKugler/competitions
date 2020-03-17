#Für die Übergabe von Kommandozeilenargumenten
import sys
#Für Reguläre Ausdrücke
import re
#Zur Durchmischung der Buchstaben beim Twisten
import random
#Für das Handling von Unicode-Zeichen
import codecs

if len(sys.argv)!=2:
    print("Benutzung: a2.py <pfad\\zur\\datei.txt>")
    sys.exit(0)
#Einlesen des Textes
with codecs.open(sys.argv[1],"r",encoding="utf-8") as f:
    twisttext1=u""
    lines=f.readlines()
    for line in lines:
        if "\n" in line:
            line=line[:-1]+" "
        twisttext1+=line
#Einlesen der Wörterliste
with codecs.open("data\\a2\\woerterliste.txt","r",encoding="utf-8") as f:
    woerterliste=[line.rstrip('\n') for line in f]

#Sortieren der Wörterliste
sorteddict={}
for word in woerterliste:
    len1 = len(word)
    if len1 > 3:
        firstchar = word[0]
        lastchar = word[-1]
        try:
            a = sorteddict[len1]
            try:
                a = sorteddict[len1][firstchar]
                try:
                    a = sorteddict[len1][firstchar][lastchar]
                except:
                    sorteddict[len1][firstchar][lastchar] = []
            except:
                sorteddict[len1][firstchar] = {}
                sorteddict[len1][firstchar][lastchar] = []
        except:
            sorteddict[len1] = {}
            sorteddict[len1][firstchar] = {}
            sorteddict[len1][firstchar][lastchar] = []
            
        sorteddict[len1][firstchar][lastchar].append(word)


def middleanagramm(word1,word2):
    """
    Input:  Zwei Wörter
    Output: True  wenn die mittleren Buchstaben der beiden Wörter ein Anagramm bilden
            False ansonsten
    """
    wordlist1=list(word1)[1:-1]
    wordlist2=list(word2)[1:-1]
    for i in wordlist1:
        if i in wordlist2:
            wordlist2.remove(i)
        else:
            return False
    if len(wordlist2)>0:
        return False
    return True


def twistword(word):
    """
    Input:  ein Wort
    Output: ein Wort, bei dem alle mittleren Buchstaben des Eingabewortes 
            zufällig permutiert sind
    """
    tlist=list(word[1:-1])
    random.shuffle(tlist)
    wordend=word[-1]
    word=word[0]
    for i in tlist:
        word+=i
    word+=wordend
    return word


def untwistword(tword):
    """
    Input:  Ein getwistetes Wort (Die mittleren Buchstaben sind zufällig permutiert)
    Output: Das Eingabewort mit einem "#" vorangestellt,
            wenn in der Wörterliste kein Wort zu finden ist, 
            dessen Länge, Anfangs- und Endbuchstabe gleich sind und dessen
            mittlere Buchstaben ein Anagramm zum Eingabewort bilden
            (oder, bei großgeschriebenen Wörtern auch Wörter, bei denen der 
            Anfangsbuchstabe in der Wörterliste kleingeschrieben wird)
            
            Das enttwistete Eingabewort, wenn es genau ein Wort gibt, 
            das die genannten Kriterien erfüllt 
            
            Mehrere Wörter, die mit einem "/" getrennt werden,
            wenn es mehrere Wörter gibt, die die genannten Kriterien erfüllen
            
    """
    possiblewords2 = []
    
    if tword[0].isupper():
        upper = True
        #gibt es wörter mit großem anfangsbuchstaben?
        try:
            possiblewords1 = sorteddict[len(tword)][tword[0]][tword[-1]]
        except:
            #es gibt keine wörter mit großem anfangsbuchstaben
            upper = False
            try:
                #gibt es wörter mit kleinem anfangsbuchstaben?
                possiblewords1 = sorteddict[len(tword)][tword[0].lower()][tword[-1]]
            except:
                #keins von den wörtern passt
                return "#"+tword
        #es gibt wörter mit großem Anfangsbuchstaben
        if upper:
            try:
                possiblewords1 += sorteddict[len(tword)][tword[0].lower()][tword[-1]]
            except:
                pass
    else:

        try:
            possiblewords1 = sorteddict[len(tword)][tword[0]][tword[-1]]
        except:
            return "#"+tword

    for word in possiblewords1:
        if middleanagramm(tword,word):
            possiblewords2.append(tword[0]+word[1:])

    #mehrfach vorkommende wörter aus einer liste entfernen
    for i in possiblewords2:
        n = possiblewords2.count(i)
        for x in range(n-1):
            possiblewords2.remove(i)
                   
    if len(possiblewords2) == 0:
        return "#"+tword
    
    if len(possiblewords2) > 1:
        string = u""
        for n,i in enumerate(possiblewords2):
            if n != 0:
                string += "/"
            string += i
        return string
    
    else:
        return possiblewords2[0]


def twisttext(twtext,twist):
    """
    iteriert über alle Buchstaben des Textes, gruppiert Wörter und 
    twisted/enttwisted (in Abhängigkeit der Variable twist) 
    alle Wörter mit über drei Buchstaben.
    """
    
    retstring = u""
    word = ""
    for i in twtext:
        if re.search("[A-Za-zÄäÖöÜüß]",i):
            word += i
        else:
            if len(word)>3:
                if twist:
                    retstring += twistword(word)
                else:
                    retstring += untwistword(word)
            else:
                retstring += word
            word = u""
            retstring += i
    return retstring

print(twisttext1)
a = twisttext(twisttext1,True)
print(a)
a = twisttext(a,False)
print(a)