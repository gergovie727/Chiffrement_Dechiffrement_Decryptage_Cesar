from erreurs import *

def chiffrement(texte, clef, ponct) -> str:
    texte_chiffre = ""

    for lettre in texte:

        numlettre = ord(lettre)
        
        if numlettre >= 65 and numlettre <= 90:
            
            nlettre = numlettre + clef
            
            if nlettre > 90:
                nlettre = 65 + (nlettre - 91)
            
            nlettre = chr(nlettre)

        elif numlettre >= 97 and numlettre <=122:
            
            nlettre = numlettre + clef
            
            if nlettre > 122:
                nlettre = 97 + (nlettre - 123)
            
            nlettre = chr(nlettre)

        elif ponct:
            nlettre = lettre
        else:
            continue

        texte_chiffre = texte_chiffre + nlettre

    print(texte_chiffre)