#création d'un tableau (liste en python) myTable
myTable = [3,5,6,1,8,2]

#2) Écrire un programme permettant le parcours du tableau au cours d’une itération du tri à bulles.

#maximum va stocker la plus grande valeur de la liste parcourue
maximum = myTable[0]
#le programme va parcourir la liste en comparant la valeur actuelle de maximum avec la valeur de la liste d'indice i
for i in range(len(myTable)):
    if myTable[i] > maximum :
        maximum = myTable[i]
        #indice_max va stocker l'indice de la plus grande valeur, pour pouvoir le réutiliser dans le code suivant
        indice_max = i
#code de l'exercice 1
indice1 = -1
indice2 = indice_max
valeur_temporaire = myTable[indice1]
myTable[indice1] = myTable[indice2]
myTable[indice2] = valeur_temporaire
#vérifie que le code fonctionne
assert(myTable) == [3,5,6,1,2,8]