# second défi avec :
# les caractères spéciaux (string.punctuation) dans la pool possible.

#libre choix à l'utilisateur :

    #Lettres
    #Chiffres
    #Caractères spéciaux
import string as st
import random as rd

def generate_password_m(length : int):
    choice1 = input("voulez vous inclure des chiffres ? ")
    choice2 = input("voulez vous inclure des lettres ? ")
    choice3 = input("voulez vous inclure des caractères spéciaux ? ")
    if choice1 == "oui" and choice2 == "oui" and choice3 == "oui":
        print("".join(rd.choice(st.ascii_letters + st.digits + st.punctuation) for _ in range(length)))
    elif choice1 == "oui" and choice2 == "non" and choice3 == "oui":
        print("".join(rd.choice(st.digits + st.punctuation) for _ in range(length)))
    elif choice1 == "oui" and choice2 == "non" and choice3 == "non":
        print("".join(rd.choice(st.ascii_letters) for _ in range(length)))
    elif choice1 == "oui" and choice2 == "oui" and choice3 == "non":
        print("".join(rd.choice(st.digits + st.ascii_letters) for _ in range(length)))
    elif choice1 == "non" and choice2 == "oui" and choice3 == "oui":
        print("".join(rd.choice(st.ascii_letters + st.punctuation) for _ in range(length)))
    elif choice1 == "non" and choice2 == "non" and choice3 == "oui":
        print("".join(rd.choice(st.punctuation) for _ in range(length)))
    elif choice1 == "non" and choice2 == "oui" and choice3 == "non":
        print("".join(rd.choice(st.ascii_letters) for _ in range(length)))
    elif choice1 == "non" and choice2 == "non" and choice3 == "non":
        print("There is nothing to return here")
    return "Program Finished"

print(generate_password_m(10))

# Another way of doing it by chatgpt

def generating_password(length : int, use_digits : bool, use_letters : bool, use_punctuations : bool) :
    """
    Ce que la function fait, c'est de prendre les choix de l'utilisateur en paramètres
    avant de former une chaîne complète composée de tous les caractères du module 'string'.
    Enfin il y a une selection qui se fait avec 'random', ce qui permet de générer le mot de passe
    en fonction de la longueur entrée en paramètre.
    """
    password = ""
    if use_digits :
        password += st.digits
    if use_letters :
        password += st.ascii_letters
    if use_punctuations :
        password += st.punctuation
    if not password :
        raise ValueError("You need to put at least one character!")
    return ''.join(rd.choice(password) for _ in range(length))

print(generating_password(10, use_digits = True, use_letters = True, use_punctuations = True))