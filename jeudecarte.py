from operator import truediv
from unicodedata import name


class carte:
    def __init__(self,nom,mana,description,attribut):
        self.mana = mana
        self.name = nom
        self.desc = description
        self.attr = attribut
    
    def getName(self):
        return self.name
    
    def getMana(self):
        return self.mana

    def getDescription(self):
        return self.desc

    def getAttribut(self):
        return self.attr

class cristal(carte):
    def __init__(self,nom,mana,description,attribut):
        self.mana = mana
        super().__init__(nom)
        self.desc = description
        self.attr = attribut
        self.valeur = 5

class dragon(carte):
    def __init__(self, nom, mana, description, attribut):
        super().__init__(nom, mana, description, attribut)   

class soldat(carte):
    def __init__(self, nom, mana, description, attribut):
        super().__init__(nom, mana, description, attribut)

class Mage:
    def __init__(self,nom,mana,pv):
        self.mana = mana
        self.Hp = pv
        self.carte = [dragon("dragon",10,"un puissant dragon qui crache du feu","boule de feu"),soldat("soldat",5,"un soldat lambda","coup d'épée")]
        self.defausse = 0
        self.name = nom
        self.tour = 0
        self.hpE = 20

    def partieGagne(self):
        win = False
        if(self.Hp <= 0):
            win = True
            print("Défaite !")
        if(self.hpE <= 0):
            win = True
            print("Victoire !")
        return win

    def defausseCarte(self):
        self.defausse = self.defausse + 1
        return self.defausse

    def tourPartie(self):
        self.tour == self.tour + 1
        if (self.tour == self.tour + 1):
            self.mana == self.mana + 1

    def jouerCarte(self):
        print("vous avez", self.mana, "point de mana")
        choixJ = input("que voulez vous faire attaquer ou piocher\n")
        if (choixJ == "attaquer"):
            print("vois ci vos carte en main", self.carte)
            propositionJ = input("quel carte voulez vous jouer ?\n")
            if(propositionJ == "dragon" ):
                if (self.mana != 10):
                    print ("vous ne pouvez pas poser cette carte")
                else :
                    print ("vous avez poser la carte dragon sur le jeu")
            if(propositionJ == "soldat"):
                if (self.mana != 5):
                    print ("vous ne pouvez pas poser cette carte")
                else :
                    print("vous avez poser la carte ",propositionJ, "sur le jeu")
        if (choixJ == "piocher"):
            print ("vous avez piocher une carte")
        if (self.mana == 10):
            print("votre mana est au maximum")
        self.hpE -= 5
        print("l'ennemi a pris des dégat, il lui reste :", self.hpE, "point de vie !")

    def play(self):
        while(self.tour < 3 and not self.partieGagne()):
            self.jouerCarte()

myGame = Mage("John",2,20)
myGame.play()
