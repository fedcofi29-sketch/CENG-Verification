from p5 import *
import random

# Idk if some of these are copyright but they're interchangeable w/ other names
fantasy_names = [
    "Aragorn", "Frodo", "Bilbo", "Thranduill"
    "Shrek", "Donkey", "Swamp",
    "Eragon", "Varden", "Uragals", "Ra'zac", "Murtagh"
    "Diago", "Caten", "Res", "Luceum", "Obiteum"
    "Eldrazi", "Kor", "Fae"
]

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
        # Circle draws w/ diameter but its easier for other references to store w/ radius
        self.r = 20
        # Only ever one player so this is just hardcoded
        # Can either use WASD or arrow keys
        self.up_key = ["W", 'UP']
        self.down_key = ["S", 'DOWN']
        self.left_key = ["A", 'LEFT']
        self.right_key = ["D", 'RIGHT']

        self.moving = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        


    def render(self):
        fill('red')
        circle(self.pos, self.r * 2)

    # Key presseed / released allows click hold
    def handlekeypressed(self, k):
        if k.upper() in self.up_key:
            self.moving['up'] = True
        elif k.upper() in self.down_key:
            self.moving['down'] = True
        elif k.upper() in self.left_key:
            self.moving['left'] = True
        elif k.upper() in self.right_key:
            self.moving['right'] = True

    def handlekeyreleased(self, k): 
        if k.upper() in self.up_key:
            self.moving['up'] = False
        elif k.upper() in self.down_key:
            self.moving['down'] = False
        elif k.upper() in self.left_key:
            self.moving['left'] = False
        elif k.upper() in self.right_key:
            self.moving['right'] = False

    def move(self):
        # The +/- of up/down are inversed since 0 is the top of p5 coordinates
        if self.moving['up']:
            self.position.y -= 5
            if self.position.y - self.r <= 0:
                self.position.y = 0 + self.r
        if self.moving['down']:
            self.position.y += 5
            if self.position.y + self.r >= screen_height:
                self.position.y = screen_height - self.r
        if self.moving['left']:
            self.position.x -= 5
            if self.position.x - self.r <= 0:
                self.position.x = 0 + self.r
        if self.moving['right']:
            self.position.x += 5
            if self.position.x + self.r >= screen_width:
                self.position.x = screen_width - self.r

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

class Location:
    def __init__(self, position, width, height, name):
        self.position = position
        self.width = width
        self.height = height
        self.name = name

    def render(self):
        # colors are arbitrary. just wanted to confirm text was there
        fill('white')
        rect((self.position), self.width, self.height)
        fill('black')
        text(self.name, self.position.x + 10, self.position.y)



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
pos = Vector(100, 200)
shop = Location(pos, 80, 40, 'Shop')


def setup():
    size(screen_width, screen_height)
    arial = create_font("arial.ttf")
    text_font(arial)

def draw():
    jimmy.render()
    jimmy.move()
    shop.render()
    
run()
