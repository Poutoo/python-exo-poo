class Personne:
    def __init__(self, nom: str, age: int, numero_secu: str = 123-45-6789):
        self.nom = nom
        self.__age = age
        self.__numero_secu = numero_secu
        
    
    def afficher_info():
        pass