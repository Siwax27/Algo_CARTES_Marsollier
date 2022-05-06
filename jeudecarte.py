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

    def manaJ(self):
        self.mana = 100
        return self.mana

    def defausseCarte(self):
        self.defausse = self.defausse + 1
        return self.defausse

    def pvJ(self):
        return self.Hp
    

    def jouerCarte(self):
        propositionJ = input("quel carte voulez vous jouer ?\n")
        if(propositionJ == "dragon"):
            print ("vous avez poser la carte dragon sur le jeu")
            self.mana = self.mana - 10
            print("il vous reste ",self.mana," de mana")
        if(propositionJ == "soldat"):
            print("vous avez poser la carte ",propositionJ, "sur le jeu")
            self.mana = self.mana - 5
            print("il vous reste ",self.mana," point de mana")

    def play(self):
        print("vois ci vos carte en main", self.carte)
        self.jouerCarte()
        print("bien joué vous avez poser une carte")

myGame = Mage("John",100,20)
myGame.play()
