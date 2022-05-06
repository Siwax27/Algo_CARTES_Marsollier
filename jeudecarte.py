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

class créature(carte):
    def __init__(self, nom, mana, description, attribut):
        super().__init__(nom, mana, description, attribut)   


class Mage:
    def __init__(self,nom,mana,pv):
        self.mana = mana
        self.Hp = pv
        self.carte = [carte("dragon",10,"un puissant dragon qui crache du feu","boule de feu"),carte("soldat",5,"un soldat lambda","coup d'épée")]
        self.defausse = 0
        self.name = nom
        self.tour = 0
        self.hpE = 20

    def partieGagne(self):
        win = True
        if(self.Hp <= 0):
            win = win
            print("Défaite !")
        if(self.hpE <= 0):
            win = win
            print("Victoire !")
        


    def manaJ(self):
        return self.mana

    def defausseCarte(self):
        self.defausse = self.defausse + 1
        return self.defausse

    def pvJ(self):
        return self.Hp

    def jouerCarte(self):
        self.tour == self.tour + 1
        print("vous avez", self.mana, "point de mana")
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
        if (self.tour == self.tour + 1):
            self.mana += 1 
        if (self.mana == 10):
            print("votre mana est au maximum")
        if (self.tour == self.tour + 1):
            self.hpE -= 5
            print("l'ennemi a pris des dégat, il lui reste :", self.hpE, "point de vie !")

    def play(self):
        while(self.tour<3 and not self.partieGagne()):
            print("vois ci vos carte en main", self.carte)
            self.jouerCarte()

myGame = Mage("John",2,20)
myGame.play()
