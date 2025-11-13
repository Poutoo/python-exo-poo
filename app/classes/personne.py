class Personne:
    def __init__(self, nom: str, age: int, numero_secu: str = 123-45-6789):
        self.nom = nom
        self.__age = age
        self.__numero_secu = numero_secu
        
    # accéder au infos direct et par name mangling
    def afficher_info(self) -> str:
        return f"Nom: {self.nom} \nAge: {self.__age} \nNuméro de sécu: {self.__numero_secu}"    
    
    #modifier les infos direct
    def set_nom(self, nouveau_nom: str):
        if nouveau_nom:
            self.nom = nouveau_nom
        else:
            raise ValueError("Le nom ne peut pas être vide")
    
    def set_numero_secu(self, nouveau_numero: str):
        if len(nouveau_numero) == 11 and nouveau_numero.count('-') == 2:
            self.__numero_secu = nouveau_numero
        else:
            raise ValueError("Le numéro de sécurité sociale doit être au format XXX-XX-XXXX.")
    
    def set_age(self, nouvel_age: int):
        if nouvel_age >= 0:
            self.__age = nouvel_age
        else:
            raise ValueError("L'âge ne peut pas être négatif.")
        
    