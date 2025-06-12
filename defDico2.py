import operator

notes = {
    "Alice": 14,
    "Bob": 9,
    "Charlie": 17,
    "Dina": 12,
    "Eli": 7,
    "Fanny": 18,
    "Gaby": 10,
    "Hugo": 4,
    "Ines": 15,
    "Jonas": 19
}
sorted_notes = dict(sorted(notes.items(), key = operator.itemgetter(1), reverse = True))
#Classer les élèves par note décroissante.
def ranking_etudiants(etudiants : dict):
    count = 0
    for key, value in etudiants.items() :
        count += 1
        print(f" {count}- {key} moyenne : {value}")
    return f" The ranking is from the following dictionary : {etudiants}"
print(ranking_etudiants(sorted_notes))
print()

#Afficher les 3 meilleurs élèves avec leur note.
def ranking_First3(etudiants : dict):
    count = 0
    for key, value in etudiants.items() :
        count += 1
        print(f" {count}- {key} avec une note de  {value}/20")
        if count == 3 :
            break
    return "program finished"
print(ranking_First3(sorted_notes))
print()

#Calculer la moyenne générale de la classe.
def average(etudiants : dict):
    the_sum = 0
    for value in etudiants.values() :
        the_sum += value
    return f" the average is : {round(the_sum/len(etudiants), 2)}"
print(average(notes))
print()

#Afficher le nombre d'élèves ayant obtenu une note >= 10.
def the_best(etudiants : dict):
    une_liste = []
    for key, value in etudiants.items():
        if value >= 10 :
            une_liste.append(key)
        else : continue
    return f"Those above 10 are {len(une_liste)} people"
print(the_best(notes))
print()

#Donner la répartition des élèves par tranche de notes (0–5, 6–9, 10–13, 14–17, 18–20).
def repartition(etudiants : dict):
    tier_1 = []
    tier_2 = []
    tier_3 = []
    tier_4 = []
    tier_5 = []
    for key, value in etudiants.items() :
        if value in range(6) :
            tier_1.append(key)
        elif value in range(6, 10) :
            tier_2.append(key)
        elif value in range(10, 14) :
            tier_3.append(key)
        elif value in range(14, 18) :
            tier_4.append(key)
        elif value in range(18, 21) :
            tier_5.append(key)
    print(f"Those in Tier 1 are : {', '.join(tier_1)}")
    print(f"Those in Tier 2 are : {', '.join(tier_2)}")
    print(f"Those in Tier 3 are : {', '.join(tier_3)}")
    print(f"Those in Tier 4 are : {', '.join(tier_4)}")
    print(f"Those in Tier 5 are : {', '.join(tier_5)}")
    return "program finished"
print(repartition(notes))
