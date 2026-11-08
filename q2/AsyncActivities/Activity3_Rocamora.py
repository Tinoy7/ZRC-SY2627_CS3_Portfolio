class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage: 
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

wario = Warrior()
magio = Mage()
archio = Archer()

wario.special_move()
magio.special_move()
archio.special_move()
