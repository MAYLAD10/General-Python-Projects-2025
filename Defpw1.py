# We are now going to write a program for password generation.

import string as st
import random as rd
def generate_password(length : int) :
    chars = st.ascii_letters + st.digits
    password = ""
    while length:
        password += rd.choice(chars)
        length -= 1
    return password


def generate_password2(length : int):
    chars = st.ascii_letters + st.digits
    return "".join(chars for _ in range(length)) #list comprehension


print(generate_password(10)) # pour avoir le resultat avec 10 caratères


