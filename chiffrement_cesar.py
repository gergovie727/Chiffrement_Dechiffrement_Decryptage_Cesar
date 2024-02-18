from erreurs import *

def chiffrement(texte) -> str:
    texte_chiffre = ""

    for lettre in texte:
        
        if ord(lettre) >= 65 and ord(lettre) <= 90:
            print("Majuscule: ",lettre)

        elif ord(lettre) >= 97 and ord(lettre) <=122:
            print("Minuscule: ",lettre)