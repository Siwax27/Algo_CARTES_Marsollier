class Carte:
    def __init__(self,mana,nom,description,attribut):
        self.mana = mana
        self.name = nom
        self.desc = description
        self.attr = attribut
    
    def nameCarte(self):
        return self.name
    
    def manaCarte(self):
        return self.mana

    def descriptionCarte(self):
        return self.desc

    def attributCarte(self):
        return self.attr