import chiffrement_cesar
import sys
from erreurs import *

version = "0.2"

def show_help() -> None:
    print("Usage: cesarpy [OPTIONS]\n")

    print("Description:\n\tScript pour chiffrer un message en clair et déchiffrer ou décrypter un message chiffré par le code de César.\n")

    print("Options:")
    print("\t-h, --help\t\t Affiche l'aide.")
    print("\t-v, --version\t\t Affiche la version du script.")
    print("\t-f, --file\t\t Permet de spécifier le chemin du fichier dans lequel est contenu le texte.")
    print("\t-t, --text\t\t Permet de spécifier le texte directement en ligne de commande.")
    print("\t-c, --chiffrement\t\t Permet de chiffrer le texte.")
    print("\t-d, --dechiffrement\t\t Permet de déchiffrer le texte.")
    print("\t-D, --decryptage\t\t Permet de décrypter le texte.")
    print("\t-o, --output\t\t Permet de spécifier le fichier où le texte chiffré sera stocké.")
    print("\t-p, --ponctuation\t\t Permet de déterminer si la ponctuation doit être gardé (Vaut True par défaut).")

    exit(0)

def debut() -> tuple:
    if len(sys.argv) == 1:
        show_help()

    texte = ""
    fichier_sortie = None
    chiffrement = False
    dechiffrement = False
    decryptage = False
    clef = -1
    ponct = True

    i = 1
    try:
        while i < len(sys.argv):
                    
            if sys.argv[i] in ("-h", "--help"):
                show_help()
                    
            elif sys.argv[i] in ("-v", "--version"):
                print(version)
                exit(0)

            elif sys.argv[i] in ("-f", "--file"):
                i+=1
                try:
                    fichier = open(sys.argv[i],"r")
                    texte = fichier.read()
                    fichier.close()

                except FileNotFoundError as e:
                    print(f"Erreur, le fichier d'entrée {sys.argv[i]} n'existe pas.")

                except IndexError as e:
                    print("Erreur, vous n'avez pas fourni de fichier.")
                

            elif sys.argv[i] in ("-t", "--text"):
                i+=1
                texte = sys.argv[i]

            elif sys.argv[i] in ("-c", "--chiffrement"):
                chiffrement = True
                i+=1
                try:
                    clef = sys.argv[i]
                    clef = int(clef)
                    if clef<0 or clef>25:
                        raise optionError("La clef donnée n'est pas bonne. Celle-ci doit être comprise entre 0 et 25.")
                    
                except ValueError as e:
                    print("Erreur, la clef donnée doit être un nombre compris entre 0 et 25, et non", sys.argv[i])
                    exit(2)

                except IndexError as e:
                    print("Erreur, vous n'avez pas donné de clef de chiffrement.")
                    exit(3)

            elif sys.argv[i] in ("-d", "--dechiffrement"):
                dechiffrement = True
                i+=1
                try:
                    clef = sys.argv[i]
                    clef = int(clef)
                    if clef<0 or clef>25:
                        raise optionError("La clef donnée n'est pas bonne. Celle-ci doit être comprise entre 0 et 25.")
                    
                except ValueError as e:
                    print("Erreur, la clef donnée doit être un nombre compris entre 0 et 25, et non", sys.argv[i])
                    exit(2)

                except IndexError as e:
                    print("Erreur, vous n'avez pas donné de clef de déchiffrement.")
                    exit(3)

            elif sys.argv[i] in ("-D", "--decryptage"):
                decryptage = True

            elif sys.argv[i] in ("-o", "--output"):
                i+=1
                try:
                    if sys.argv[i][0] == '-':
                        raise IndexError("erreur")
                    
                    fichier_sortie = open(sys.argv[i],"w")

                except IndexError as e:
                    print(f"Erreur, vous n'avez pas donné de fichier de sortie après l'option {sys.argv[i-1]}.")
                    exit(6)

            elif sys.argv[i] in ("-p", "--ponctuation"):
                i+=1
                try:
                    if sys.argv[i].lower() not in ("true","false"):
                        raise ValueError("Error")
                    if sys.argv[i].lower() == "true":
                        ponct = True
                    else:
                        ponct = False
                except ValueError as e:
                    print("Erreur, la valeur de l'option -p doit être true ou false, et non", sys.argv[i])
                    exit(4)

                except IndexError as e:
                    print("Erreur, vous n'avez pas donné de valeur pour l'option -p.")
                    exit(5)

            else:
                raise optionError("Vous avez donné une option invalide: ",sys.argv[i])
                
            i+=1


        if (chiffrement and dechiffrement):
            raise optionError("Vous avez donné deux options incompatibles: -c/--chiffrement et -d/--dechiffrement.")

        elif (chiffrement and decryptage):
            raise optionError("Vous avez donné deux options incompatibles: -c/chiffrement et -D/--decryptage.")
            
        elif (dechiffrement and decryptage):
            raise optionError("Vous avez donné deux options incompatibles: -d/--dechiffrement et -D/--decryptage.")
        
        elif not chiffrement and not dechiffrement and not decryptage:
            raise optionError("Vous n'avez pas donné d'option. Veuillez en donner une (-c/--chiffrement, -d/--dechiffrement ou -D/--decryptage)")

    except Exception as e:
        if type(e) == optionError:
            print(e)
            exit(1)
    return (texte, fichier_sortie, chiffrement, dechiffrement, decryptage, clef, ponct)
        
texte, fichier_sortie, chiffrement, dechiffrement, decryptage, clef, ponct = debut()

if chiffrement:
    texte = chiffrement_cesar.chiffrement_texte(texte, clef, ponct)
    if fichier_sortie != None:
        fichier_sortie.write(texte)
        fichier_sortie.close()
    else:
        print(texte)

else:
    print("wtf")