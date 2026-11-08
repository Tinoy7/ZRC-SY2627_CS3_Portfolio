class HealthPotion:
    def use(self):
        print("You regain 50 hp.")

class ManaPotion:
    def use(self):
        print("You restore 30 mp.")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds.")

def apply_item(item):
    item.use()

basic_hp = HealthPotion()
basic_mana = ManaPotion()
basic_speed = SpeedBoost()

potions = [basic_hp, basic_mana, basic_speed]

for potion in potions:
    apply_item(potion)