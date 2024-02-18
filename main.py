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

    exit(0)

def debut() -> tuple:
    if len(sys.argv) == 1:
        show_help()

    texte = ""
    fichier_sortie = None
    chiffrement = False
    dechiffrement = False
    decryptage = False

    i = 1
    try:
        while i < len(sys.argv):

            print(sys.argv[i])
                    
            if sys.argv[i] == "-h":
                show_help()
                    
            elif sys.argv[i] == "-v":
                print(version)
                exit(0)

            elif sys.argv[i] == "-f":
                i+=1
                fichier = open(sys.argv[i],"r")
                texte = fichier.read()

            elif sys.argv[i] == "-t":
                i+=1
                texte = sys.argv[i]

            elif sys.argv[i] == "-c":
                chiffrement = True

            elif sys.argv[i] == "-d":
                dechiffrement = True

            elif sys.argv[i] == "-D":
                decryptage = True

            elif sys.argv[i] == "-o":
                i+=1
                fichier_sortie = open(sys.argv[i],"r")

            else:
                raise optionError("Vous avez donné une option invalide: ",sys.argv[i])
                
            i+=1


        if (chiffrement and dechiffrement):
            raise optionError("Vous avez donné deux options incompatibles: -c et -d.")

        elif (chiffrement and decryptage):
            raise optionError("Vous avez donné deux options incompatibles: -c et -D.")
            
        elif (dechiffrement and decryptage):
            raise optionError("Vous avez donné deux options incompatibles: -d et -D.")
        
        elif not chiffrement and not dechiffrement and not decryptage:
            raise optionError("Vous n'avez pas donné d'option. Veuillez en donner une (-c, -d ou -D)")

    except Exception as e:
        if type(e) == optionError:
            print(e)
            exit(1)

    return (texte, fichier_sortie, chiffrement, dechiffrement, decryptage)
        
texte, fichier_sortie, chiffrement, dechiffrement, decryptage = debut()

if chiffrement:
    chiffrement_cesar.chiffrement(texte)

else:
    print("wtf")