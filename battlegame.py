class Player:
    def __init__(self, hp, strength, money):
        self.health = hp
        self.strength = strength
        self.equipment = []
        self.money = money

    def purchase(self, item):
        if self.money < item.cost:
            # Idk if this might be p5 instead so maybe print isn't best
            print('That is too expensive')
        else:
            self.money -= item.cost
            self.equipment.append(item)
    

class Item:
    def __init__(self, name, type, cost, stats):
        self.name = name
        self.type = type
        self.cost = cost
        self.stats = stats

# Idk if some of these are copyright but they're interchangeable w/ other names
fantasy_names = [
    "Aragorn", "Frodo", "Bilbo", "Thranduill"
    "Shrek", "Donkey", "Swamp",
    "Eragon", "Varden", "Uragals", "Ra'zac", "Murtagh"
    "Diago", "Caten", "Res", "Luceum", "Obiteum"
    "Eldrazi", "Kor", "Fae"]

# Add more options to vary the game slightly
weapon_types = [
    "Sword", "Bow", "Spear", "Mace"
]

# Add more options to vary the game slightly
armor_types = [
    "Helmet", "Boots", "Chestplate", "Leggings", "Shield"
]