import chiffrement_cesar
import sys

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

if len(sys.argv) == 1:
    show_help()