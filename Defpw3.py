# Forcing that at least one character from every category will be present
import string as st
import random as rd


def generating_random_password(length : int, use_digits : bool, use_letters : bool, use_punctuations : bool) :
    """
    With the arguments in the beginning, we want to generate passwords with the liking of the user. Whether he wants
    to add digits, or letters or punctuations (special characters) to it.
    We also permit the user to choose the length of the password to be generated
    :param length: The length of the password to be generated
    :param use_digits: Whether the password is generated with digits
    :param use_letters: Whether the password is generated with letters
    """
    # we give the condition below, so as to avoid losing time
    if not (use_digits or use_letters or use_punctuations):
        raise ValueError("You chose nothing. Nothing can be generated")
    # we use lists, from which we will select the different characters to be included
    digits = list(st.digits)
    letters = list(st.ascii_letters)
    punctuations = list(st.punctuation)
    password = [] # we use an empty list that we will fill
    while len(password) < length :
        if use_digits and len(password) < length :
            password.append(rd.choice(digits))
        if use_letters and len(password) < length :
            password.append(rd.choice(letters))
        if use_punctuations and len(password) < length :
            password.append(rd.choice(punctuations))
    rd.shuffle(password)
    return ''.join(password)
print(generating_random_password(10, use_digits = True, use_letters = True, use_punctuations = True))



