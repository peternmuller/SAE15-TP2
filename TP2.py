import csv
import matplotlib.pyplot as plt

def ouverture_fichier():
    """
    Cette fonction ouvre le fichier CSV 'RTE_2020.csv' et attribue chaque ligne non vide,
    à l'exception de la première, à une variable nommée rte.
    """
    rte = []
    i = 0
    with open('RTE_2020.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            i += 1
            if i % 2 == 0:
                rte.append(row)
    return rte

fic = ouverture_fichier()

def production_nucleaire():
    """
    Cette fonction récupère les valeurs de la production nucléaire stockée dans fic,
    dans la colonne d'indice 10, et les additionne dans la variable prod.
    """
    prod = 0
    for ligne in fic:
        elem = ligne[10]
        if elem.strip():
            prod += int(elem)
    return prod

def production_totale():
    """
    Cette fonction stocke la somme des valeurs des productions,
    en parcourant les lignes de fic et les colonnes de 7 à 13.
    """
    prod_totale = 0
    for ligne in fic:
        for i in range(len(ligne)):
            if 6 < i < 14:
                element = ligne[i]
                if element.strip():
                    prod_totale += int(element)
    return prod_totale

# Calcul des pourcentages de la production nucléaire et des autres productions
pourcentage_nucleaire = production_nucleaire() / production_totale() * 100 
pourcentage_autres = 100 - pourcentage_nucleaire

# Création du diagramme en camembert
labels = ['Productions autres', 'Production nucléaire']
sizes = [pourcentage_autres, pourcentage_nucleaire]
colors = ['lightcoral', 'lightskyblue']
explode = (0, 0.1)  # Fait sortir la part nucléaire du camembert

# Affichage des résultats
print("Production nucléaire :", sizes[1])
print("Production totale :", sizes[0])

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Part de nucléaire dans la production totale')
plt.show()