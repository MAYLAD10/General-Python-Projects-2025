# A new dictionary challenge, playing with functions and a mix of everything

notes = {
    "Alice": [14, 16, 15],
    "Bob": [10, 12, 11],
    "Charlie": [18, 17, 19],
    "Diana": [9, 8, 10],
    "Eve": [15, 13, 14]
}

#1. Calcule la moyenne de chaque élève
def averaging(dictio : dict) :
    new = {}
    for name, notes in dictio.items() :
        new[name] = round(sum(notes) / len(notes), 2)
    return new
aver = averaging(notes)
print(aver)
print()
#2. Trie les élèves du meilleur au moins bon (par moyenne)
def tri(dictio : dict) :
    count = 0
    sorted_new = dict(sorted(dictio.items(), key = lambda item: item[1], reverse = True))
    for name, average1 in sorted_new.items() :
        count += 1
        print(f" {count}-{name} -> {average1}")
    print()
    return sorted_new
trie = tri(aver)
print(trie)
print()
#3. Le premier du classement (nom et moyenne)
def first(dictio : dict) :
    first = next(iter(dictio.items()))
    print(f" The Best is : {first[0]} with an average of {first[1]}")
    return "Program is done"
print(first(trie))
print()
#4. Le dernier du classement (nom et moyenne)
def last(dictio : dict) :
    rev = dict(list(dictio.items())[::-1])
    last = next(iter(rev.items()))
    print(f" The last is : {last[0]} with an average of {last[1]}")
    return "Program is done"
print(last(trie))
print()
#5. La moyenne générale de la classe
def general_average(dictio : dict) :
    general = 0
    for average4 in dictio.values() :
        general += average4
    return round(general / len(dictio.values()), 2)
print(f"The general average is : {general_average(trie)}")
print()
#6. Le nombre d’élèves ayant une moyenne supérieure à celle de la classe
def very_good(dictio : dict) :
    average5 = general_average(dictio)
    la_liste = []
    for name, moyenne in dictio.items() :
        if moyenne > average5 :
            la_liste.append(name)
        else :
            continue
    return len(la_liste)
print(f" Those above the average are : {very_good(trie)} people")
