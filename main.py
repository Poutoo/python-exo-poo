from app.classes.personne import Personne
from app.classes.compte import Compte
from app.classes.rectangle import Rectangle

if __name__ == "__main__":
    p = Personne("Dupont", 30, "987-65-4321")
    print(p.afficher_info())
    
    p.set_nom("Durand")
    p.set_age(35)
    p.set_numero_secu("123-45-6789")
    print("\nAprès modification:")
    print(p.afficher_info())
    
    mon_compte = Compte(titulaire=p.nom)
    mon_compte.deposer(100.0)
    print(mon_compte.afficher_solde())
    mon_compte.deposer(500.0)
    print(mon_compte.afficher_solde())
    # afficher transactions
    print("\nTransactions enregistrées:")
    for transaction in mon_compte._Compte__transaction:
        print(transaction)
        
    mon_rectangle = Rectangle(5.0, 3.0)
    print(f"\nRectangle \nLongueur: {mon_rectangle.get_longeur()}\nLargeur: {mon_rectangle.get_largeur()}")
    print(f"Aire du rectangle: {mon_rectangle.aire()}")
        
    