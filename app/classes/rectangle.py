class Rectangle:
    def __init__ (self, longeur: float, largeur: float):
        self.longeur = longeur
        self.largeur = largeur
        
    def set_longueur(self, nouvelle_longeur: float):
        if nouvelle_longeur > 0:
            self.longeur = nouvelle_longeur
        else:
            raise ValueError("La longeur doit être positive")
        
    def set_largeur(self, nouvelle_largeur: float):
        if nouvelle_largeur > 0:
            self.largeur = nouvelle_largeur
        else:
            raise ValueError("La largeur doit être positive")
        
    def get_longeur(self) -> float:
        return self.longeur
    
    def get_largeur(self) -> float:
        return self.largeur
    
    def aire(self) -> float:
        return self.longeur * self.largeur
    
    