# final boss, we will include unit tests
import string as st
import random as rd


def password(length : int, use_digits : bool, use_letters : bool, use_punctuations : bool):
    """
    We will now allow the user to choose, once again,
    but this time we will include unit tests
    :param length:
    :param use_digits:
    :param use_letters:
    :param use_punctuations:
    :return:
    """
    # lists to be used for the generating the password for the user
    digits = list(st.digits)
    letters = list(st.ascii_letters)
    characters = list(st.punctuation)
    pw = [] # the list to be filled with the user's choices
    if not (use_digits or use_letters or use_punctuations):
        raise ValueError("Nothing to generate")
    while len(pw) < length :
        if use_digits and len(pw) < length :
            pw.append(rd.choice(digits))
        if use_letters and len(pw) < length :
            pw.append(rd.choice(letters))
        if use_punctuations and len(pw) < length :
            pw.append(rd.choice(characters))
    rd.shuffle(pw) #we do not want the password to have the same structure everytime
    return ''.join(pw) # We then return the wanted password

if __name__ == "__main__":
    # Test longueur
    pw = password(10, True, True, True)
    assert len(pw) == 10, f"Longueur attendue 10, obtenu {len(pw)}"

    # Test présence chiffres
    assert any(c.isdigit() for c in pw), "Le mot de passe doit contenir au moins un chiffre"

    # Test présence lettres
    assert any(c.isalpha() for c in pw), "Le mot de passe doit contenir au moins une lettre"

    # Test présence ponctuations
    assert any(c in st.punctuation for c in pw), "Le mot de passe doit contenir au moins un caractère spécial"

    # Test erreur si rien choisi
    try:
        password(10, False, False, False)
        assert False, "La fonction doit lever une erreur si aucune catégorie choisie"
    except ValueError:
        pass  # OK, erreur attendue
    print(" Success for all tests !!")