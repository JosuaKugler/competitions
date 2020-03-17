#you want a darker
#Für die Übergabe von Kommandozeilenargumenten
import sys
if len(sys.argv)!=2:
    print("Benutzung: a1.py <pfad\\zur\\datei.txt>")
    sys.exit(0)

#Einlesen der textdatei
#In der Liste "grouplist" sind alle Mitglieder aufgelistet
#In der Liste "followlist" sind alle Beziehungen aufgelistet, 
#sodass die  Funktion "Anfrage" daraus einfach ermitteln kann,
#ob eine Person einer anderen folgt. 
#Die Funktion "Anfrage" ist die einzige, die auf "followlist" zugreifen darf

with open(sys.argv[1],"r") as f:
    llist=f.readlines()
    followList=[]
    for i,line in enumerate(llist):
        if i==0:

            grouplist=line.split()
        elif i==len(llist)-1:
            pass
        else:
            followList.append(line.split())

#Anfn zählt die Anzahl der Anfragen
Anfn=0
def Anfrage(person1,person2):
    """
    Output: True, wenn person1 person2 folgt,
    ansonsten: False
    """
    global Anfn
    Anfn+=1
    for i in followList:
        if i[1] == person2:
            if i[0] == person1:
                return True
    return False

#In der Anfragenliste werden alle gestellten Anfragen mit Resultat gespeichert.
#Eine Anfrage "Anfrage(a,b)" wird als Liste [a,b] abgespeichert
#Mit False beantwortete Anfragen werden unter Anfragenliste[0] gespeichert,
#mit True beantwortete Anfragen unter Anfragenliste[1].
Anfragenliste=[[],[]]
#In der Liste nsuperstar werden alle Personen gespeichert, die nicht Superstar sein können
nsuperstar=[]


def get_superstar_candidate(person1=None,person2=None):
    """
    - schließt mittels einer Anfrage stets eine Person aus, die nicht Superstar ist 
    - ruft sich selbst mit der person possible_superstar und einer anderen person,
      die nicht aus nsuperstar kommt und daher auch ein Superstar sein könnte.
    - Sobald alle Personen aus grouplist bis auf eine ausgeschlossen sind, 
      wird verifysuperstar mit dieser Person (possible_superstar) aufgerufen.
    - gibt das Ergebnis von verifysuperstar bezüglich possible_superstar zurück
    """
    if person1 == None and person2 == None:
        person1=grouplist[0]
        person2=grouplist[1]
        
    if Anfrage(person1,person2):
        Anfragenliste[1].append([person1,person2])
        nsuperstar.append(person1)
        print("{} folgt {}, also ist {} kein Superstar".format(person1,person2,person1))
        possible_superstar = person2

    else:
        Anfragenliste[0].append([person1,person2])
        nsuperstar.append(person2)
        print("{} folgt {} nicht, also ist {} kein Superstar".format(person1,person2,person2))
        possible_superstar = person1

    if len(nsuperstar)==len(grouplist)-1:
        return verifysuperstar(possible_superstar)
    else:    
        for iterateperson in grouplist:
            if iterateperson not in nsuperstar and iterateperson!=possible_superstar:
                return get_superstar_candidate(possible_superstar, iterateperson)
                break


def verifysuperstar(candidate):
    """
    Output: 
        - "<candidate> ist der Superstar der Gruppe!", 
          wenn alle dem candidate folgen und der candidate niemandem folgt,
        - ansonsten: "Es gibt keinen Superstar!"
    """
    
    #test, ob alle dem candidate folgen:
    candidate_followers = []
    for i in Anfragenliste[1]:
        if i[1] == candidate:
            candidate_followers.append(i[0])
    
    for i in grouplist:
        if i != candidate and i not in candidate_followers:
            if Anfrage(i,candidate):
                print("{} folgt {}".format(i,candidate))
                candidate_followers.append(i)
            else:
                print("{} folgt {} nicht".format(i, candidate))
                return "Es gibt also keinen Superstar!"
    #test, ob der candidate niemandem folgt:
    candidate_not_follows = []
    for i in Anfragenliste[0]:
        if i[0] == candidate:
            candidate_not_follows.append(i[1])
    for i in grouplist:
        if i != candidate and i not in candidate_not_follows:
            if Anfrage(candidate,i):
                print("{} folgt {}".format(candidate,i))
                return "Es gibt also keinen Superstar!"
            else:
                print("{} folgt {} nicht".format(candidate,i))
                
    return "{} ist der Superstar dieser Gruppe!".format(candidate)

print(get_superstar_candidate())
print("Kosten: {} Euro".format(Anfn))