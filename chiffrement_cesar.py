from erreurs import *

def chiffrement_texte(texte: str, clef: int, ponct: bool) -> str:
    texte_chiffre = ""

    for lettre in texte:

        nlettre = chiffrement_lettre(lettre, ponct, clef)

        if nlettre != None:
            texte_chiffre = texte_chiffre + nlettre

    return texte_chiffre

def chiffrement_lettre(lettre: str, ponct: bool, clef: int):

    if lettre in ('à', 'â', 'ä'):
        lettre = 'a'
    elif lettre in ('é', 'è', 'ê', 'ë'):
        lettre = 'e'
    elif lettre in ('ï', 'î'):
        lettre == 'i'
    elif lettre in ('ù', 'ü', 'û'):
        lettre == 'u'
    elif lettre in ('o', 'ô', 'ö'):
        lettre == 'o'

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
        nlettre = None

    return nlettre