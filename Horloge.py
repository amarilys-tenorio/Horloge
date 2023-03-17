import time
from datetime import datetime

infinite = 1

def heure_actuelle():
    while infinite == 1:
        print(time.ctime()) 
        time.sleep(1)

def regler_heure(heure):
    global heures, minutes, secondes
    heures, minutes, secondes = heure

def afficher_heure():
    global heures, minutes, secondes
    while infinite == 1:
        secondes = secondes + 1
        if secondes == 60:
            secondes = 0 
            minutes = minutes + 1
        if minutes == 60:
            minutes = 0
            heures = heures + 1
        if heures == 24:
            heures = 0
        heures = str(heures)
        minutes = str(minutes)
        secondes = str(secondes)
        if len(secondes) < 2:
            secondes = list(secondes)
            secondes.insert(0,"0")
            secondes = "".join(secondes)
        if len(minutes) < 2:
            minutes = list(minutes)
            minutes.insert(0,"0")
            minutes = "".join(minutes)
        if len(heures) < 2:
            heures = list(heures)
            heures.insert(0,"0")
            heures = "".join(heures)
        print(heures, ":", minutes, ":", secondes)
        heures = int(heures)
        minutes = int(minutes)
        secondes = int(secondes)
        time.sleep(1)


def alarme():
    heures_alarme = input("Entrez l'heure de l'alarme sous la forme HH:MM:SS")
    
    while True : 
        heure_actuelle = datetime.now().time()
        heure_actuelle = str(heure_actuelle)
        heure_actuelle = heure_actuelle[:-7]
        if heure_actuelle == heures_alarme : 
            print ("Wake up")
            menu()
            break
        else : 
            time.sleep(1)
            continue
        

def menu():
    while True:
        choix = input('Fais ton choix entre : \n 1. Afficher heure actuelle \n 2. Modifier heure\n 3. Mettre une alarme \n')
        if choix == '1' :
            heure_actuelle()
            break
        elif  choix == '2' : 
            regler_heure((00, 00, 00))
            afficher_heure()
            break
        elif choix == '3':
            alarme()
        else : 
            continue


menu()