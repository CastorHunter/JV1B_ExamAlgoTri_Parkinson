#création d'un tableau (liste en python) myTable
myTable = [3,5,6,1,8,2]

#1) Écrire un programme permettant de permuter deux valeurs du tableau myTable.

#création de deux variables indice1 et indice2 qui sont les indices des deux valeurs à permutter
indice1 = 2
indice2 = 4
#la variable valeur_temporaire va contenir la valeur de myTable de l'indice indice1
valeur_temporaire = myTable[indice1]

myTable[indice1] = myTable[indice2]
myTable[indice2] = valeur_temporaire
#vérifie que le code fonctionne
assert(myTable) == [3,5,8,1,6,2]
