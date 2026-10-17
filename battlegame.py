from p5 import *
import random

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

shop_items = []

screen_width = 600
screen_height = 400

class Player:
    def __init__(self, hp, strength, money):
        self.health = hp
        self.strength = strength
        self.equipment = []
        self.money = money
        # I'm just doing a circle for the player for now
        self.pos = (20, 20)
        self.r = 20


    def render(self):
        circle(self.pos, self.r)

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



def create_shop_items():
    for i in range(0, 3):
        name = random.choice(fantasy_names)
        type = random.randint(1, 2)
        if type == 1:
            type = 'weapon'
            subName = random.choice(weapon_types)            
        elif type == 2:
            type = 'armor'
            subName = random.choice(armor_types)
        name = f"{subName} of {name}"

        odds = random.randint(0, 100)
        # 40% chance of 1, 30% of 2, 20% of 3, 10% of 4
        if odds >= 40:
            stats = 1
        elif odds >= 70:
            stats = 2
        elif odds >= 90:
            stats = 3
        else:
            stats = 4

        cost = stats + random.randint(-1, 3)

        newItem = Item(name, type, cost, stats)
        shop_items.append(newItem)


create_shop_items()
for item in shop_items:
    print(item.name, item.type, item.cost, item.stats)

jimmy = Player(1, 1, 1)

def setup():
    size(screen_width, screen_height)

def draw():
    jimmy.render()
    
run()
