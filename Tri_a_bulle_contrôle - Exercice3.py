#création d'un tableau (liste en python) myTable
myTable = [3,5,6,1,8,2]

#3)  Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement un tableau grâce à l’algorithme du tri à bulles.

#crée la liste myTable_triee, qui va contenir les valeurs dans l'ordre inversé
myTable_triee = []
#
for j in range(len(myTable)):
    #code de l'exercice 2
    maximum = myTable[0]
    #comme la liste va se retrouver à une valeur, on doit créer indice_max dès le début
    indice_max = 0
    for i in range(len(myTable)):
        if myTable[i] > maximum :
            maximum = myTable[i]
            indice_max = i
    indice1 = -1
    indice2 = indice_max
    valeur_temporaire = myTable[indice1]
    myTable[indice1] = myTable[indice2]
    myTable[indice2] = valeur_temporaire
    #ajoute à myTable_triee la derniere valeur de myTable, qui est donc la plus haute
    myTable_triee.append(myTable.pop())
#myTable_triee est à l'envers, on doit maintenant créer la liste finale
for i in range(len(myTable_triee)):
    myTable.append(myTable_triee.pop())
#vérifie que le code fonctionne
assert(myTable) == [1,2,3,5,6,8]
