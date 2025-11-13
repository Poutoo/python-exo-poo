class Compte:
    def __init__(self, titulaire: str, solde: int = 0.0, transaction = []):
        self.titulaire = titulaire
        self._solde = solde
        self.__transaction = []

    def deposer(self, montant: float):
        if montant > 0:
            self._solde += montant
            self.__enrengistrer_transaction(f"Dépôt de {montant}€")
        else:
            raise ValueError("Le montant du dépôt doit être positif.")
        
    def _afficher_solde(self) -> float:
        return self._solde
    
    def afficher_solde(self) -> str:
        return f"Solde actuel: {self._solde}€"
    
    def __enrengistrer_transaction(self, detail: str):
        self.__transaction.append(detail)
    
    