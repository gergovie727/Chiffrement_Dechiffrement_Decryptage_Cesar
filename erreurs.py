class optionError(Exception):

    def __init__(self, message):
        self.message = "Erreur dans la saisie des options. Veuillez vous référer à l'aide.\n"
        self.message += "Précision: "
        self.message += message

    def __str__(self) -> str:
        return super().__str__()