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
    
class Mage:
    def __init__(self,nom,mana,pv,):
        self.mana = mana
        self.Hp = pv
        self.main = [carte("dragon",10,"un puissant dragon qui crache du feu","boule de feu\n"),carte("soldat",5,"un soldat lambda","coup d'épée\n")]
        self.defausse = 0
        self.name = nom

    def manaJ(self):
        self.mana = 100
        return self.mana

    def defausseCarte(self):
        self.defausse = self.defausse + 1
        return self.defausse
        
    def carteMain(self):
        return self.main

    def pvJ(self):
        return self.Hp
    
    def mainJ(self):
        self.main = 7
        return self.main
    
    def jouerCarte(self):
        print("vois ci vos carte en main", self.main)
        propositionJ = int(input("quel carte voulez vous jouer ?\n"))
        if(propositionJ == "dragon"):
            print ("vous avez poser la carte dragon sur le jeu")
            self.mana = self.mana - 10
        else :
            print("vous avez poser la carte ",propositionJ, "sur le jeu")
            self.mana = self.mana - propositionJ
        

    def play(self):
        self.carteMain()
        self.jouerCarte()
        print("bien joué vous avez poser une carte")

myGame = Mage("John",100,20)
myGame.play()
