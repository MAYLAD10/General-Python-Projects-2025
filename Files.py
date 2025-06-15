# We will be working with files through a project
import operator

#Lire le fichier notes.txt
with open("notes.txt", "r", encoding = "utf-8" ) as file:
    lignes = file.readlines() #.redlines() et non 'readline()
    # lignes est une liste python
print(lignes)
for ligne in lignes :
    print(ligne)
print()
# autre methode ?
with open("notes.txt", "r", encoding = "utf-8") as fichier:
    for ligne in fichier :
        print(ligne)
print()
print("Un autre methode")
#Extraire les noms et les notes
# ce travail sera fait avec une fonction (personal note)
# Il faudrait que j'apprenne un peu plus à me familiariser avec
# les fonctions dans ce genre de cas. l'écriture est plus fluide et compréhensible
print()
def extraction(fich) :
    eleves  = {} # le resultat est mis dans un dictionnaire
    with open(fich, 'r') as f :
        for ligne in f : #nous voulons faire l'extraction de chacune des lignes
            nom, notes_str = ligne.strip().split(':')
            note = [int(dgt.strip()) for dgt in notes_str.strip().split(',') if dgt.strip().isdigit() == True ]
            eleves[nom.strip()] = note # on remplit le dictionnaire
    return eleves
print()
extracted = extraction("notes.txt")

#Computing the average for each student
def moyenne(eleves : dict) :
    moyenne = {key : round(sum(value)/len(value), 2) for key, value in eleves.items()}
    return moyenne
average = moyenne(extracted)

#Sorted in decreasing order average-wise
def trier(moyenne : dict) :
    new_moyenne = dict(sorted(moyenne.items(), key = operator.itemgetter(1), reverse = True)) # we specify the targeted object every time. Here we want a dictionnary
    return new_moyenne
tri  = trier(average)

#Displaying the " best
def best_3_new(moyenne : dict) :
    count = 0
    # (Bonus) writing the results in 'classement'.txt
    with open("classement.txt", 'w', encoding="utf-8") as classement:
        for key, value in moyenne.items() :
            if count == 3 :
                break
            count += 1
            classement.write(f"{count}- {key} avg : {round(value, 2)}\n") #writing tentative
            print(f"{count}- {key} avg : {round(value, 2)}")
    return "Done"

best = best_3_new(tri)
print(best)


