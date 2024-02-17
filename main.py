import chiffrement_cesar
import sys
from erreurs import *

version = "0.0.1"

def show_help():
    print("Usage: cesarpy [OPTIONS]\n")

    print("Description:\n\tScript pour chiffrer un message en clair et déchiffrer ou décrypter un message chiffré par le code de César.\n")

    print("Options:")
    print("\t-h, --help\t\t Affiche l'aide.")
    print("\t-v, --version\t\t Affiche la version du script.")
    print("\t-f, --file\t\t Permet de spécifier le chemin du fichier dans lequel est contenu le texte.")
    print("\t-t, --texte\t\t Permet de spécifier le texte directement en ligne de commande.")
    print("\t-c, --chiffrement\t\t Permet de chiffrer le texte.")
    print("\t-d, --dechiffrement\t\t Permet de déchiffrer le texte.")
    print("\t-D, --decryptage\t\t Permet de décrypter le texte.")
    print("\t-o, --output\t\t Permet de spécifier le fichier où le texte chiffré sera stocké.")

def debut() -> tuple:

    if len(sys.argv) == 1:
        show_help()

    texte = ""
    fichier_sortie = None
    chiffrement = False
    dechiffrement = False
    decryptage = False

    i = 1
    while i < len(sys.argv):
            
        match sys.argv[i]:
                
            case "-h":
                show_help()
                break
                
            case "-v":
                print(version)
                break

            case "-f":
                i+=1
                fichier = open(sys.argv[i],"r")
                texte = fichier.read()
                break

            case "-t":
                i+=1
                texte = sys.argv[i]
                break

            case "-c":
                chiffrement = True
                break

            case "-d":
                dechiffrement = True
                break

            case "-D":
                decryptage = True
                break

            case "-o":
                i+=1
                fichier_sortie = open(sys.argv[i],"r")
                break

            case _:
                raise optionError("Vous avez donné une option invalide: ",sys.argv[i])


    if (chiffrement and dechiffrement):
        raise optionError("Vous avez donné deux options incompatibles: -c et -d.")

    elif (chiffrement and decryptage):
        raise optionError("Vous avez donné deux options incompatibles: -c et -D.")
        
    elif (dechiffrement and decryptage):
        raise optionError("Vous avez donné deux options incompatibles: -d et -D.")
        
