from collections import deque
import numpy as np
import math
import matplotlib.pyplot as plt

r = 100
d = 0.05
m = 6
dmax = 0.25
treshold = 99.34

busted = False

mGraphe = []
pourcentageGraphe = []

timeSimulated = 1000
timeStep = 0.001

while not busted:
    #on initialise les infos pour l'itération
    currentTime = 0
    nextRequete = 99999
    serveurActif = []
    timeTraitementRequetes = []
    timeEnteredServeur = []
    createNewRequete = True
    nbRequetesTraite = 0
    nbRequetesLong = 0

    for i in range(0, m):
        serveurActif.append(0)
        timeTraitementRequetes.append(0)
        timeEnteredServeur.append(0)
    attente = deque([])
    tempsEntreeAttente = deque([])

    #simulation temporelle
    while currentTime <= timeSimulated:

        if createNewRequete:
            #on détermine quand la prochaine requete doit arriver
            nextRequete = currentTime + (np.random.exponential(1/r, 1))[0]
            createNewRequete = False
    
        if currentTime >= nextRequete:
            #on crée une nouvelle requete pour le traitement
            timeTraitement = (np.random.exponential(d, 1))[0]
            createNewRequete = True
            foundEmpty = False
            index = 0
            while index < m and not foundEmpty:
                if(serveurActif[index] == 0):
                    foundEmpty = True
                else:
                    index += 1
            
            if foundEmpty:
                #un serveur est vide alors on l'occupe
                serveurActif[index] = 1
                timeTraitementRequetes[index] = currentTime + timeTraitement
                timeEnteredServeur[index] = currentTime
            else:
                #aucun serveur est vide alors en va en file d'attente
                attente.appendleft(timeTraitement)
                tempsEntreeAttente.appendleft(currentTime)

        for i in range(0, m):
            #si le serveur est occupé, on vérifie si sa requete est fini de traiter
            if serveurActif[i] == 1:
                if currentTime >= timeTraitementRequetes[i]:
                    serveurActif[i] = 0
                    nbRequetesTraite += 1
                    if (currentTime - timeEnteredServeur[i]) >= dmax:
                        nbRequetesLong += 1

            #les serveurs innocupés vérifient s'il y a des requetes en attente   
            if serveurActif[i] == 0:
                if len(attente) > 0:
                    newTime = attente.pop()
                    timeEntree = tempsEntreeAttente.pop()
                    serveurActif[i] = 1
                    timeTraitementRequetes[i] = currentTime + newTime
                    timeEnteredServeur[i] = timeEntree
 
        currentTime += timeStep

    pourcentageGood = 100 - (nbRequetesLong/nbRequetesTraite) * 100
    print("essai avec m = " + str(m) + "\n" + str(nbRequetesTraite) + 
    " requetes traitees et " + str(nbRequetesLong) + " requetes ont pris plus de 0.25 secondes\n" +
    str(pourcentageGood) + "%\n\n========================================\n")
    mGraphe.append(m)
    pourcentageGraphe.append(pourcentageGood)

    if pourcentageGood >= treshold:
        busted = True

    m += 1

plt.plot(mGraphe, pourcentageGraphe)
plt.xlabel("nombre de serveurs m")
plt.ylabel("pourcentage de réussite")
plt.axhline(y=99.3, color='r', linestyle='-')
plt.grid()
plt.show()

print("simulation done")