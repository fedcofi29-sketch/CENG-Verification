from p5 import *
import random
import math

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
locations = []
background_colors = [
    {"location": "Outdoors",
     "r": 0, "g": 50, "b": 10
    }
]

screen_width = 600
screen_height = 400

class Player:
    def __init__(self, hp, strength, money):
        self.health = hp
        self.strength = strength
        self.equipment = []
        self.money = money
        # I'm just doing a circle for the player for now
        self.position = Vector(20, 20)
        # Circle draws w/ diameter but its easier for other references to store w/ radius
        self.r = 10
        # Only ever one player so this is just hardcoded
        # Can either use WASD or arrow keys
        self.up_key = ["W", 'UP', "w", "up"]
        self.down_key = ["S", 'DOWN', "s", "down"]
        self.left_key = ["A", 'LEFT', 'a', 'left']
        self.right_key = ["D", 'RIGHT', 'd', 'right']
        self.moving = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        self.map = "Outdoors"
        


    def render(self):
        fill('gray')
        circle(self.position, self.r * 2)

    # Key presseed / released allows click hold
    def handlekeypressed(self, k):
        if k in self.up_key:
            self.moving['up'] = True
        elif k in self.down_key:
            self.moving['down'] = True
        elif k in self.left_key:
            self.moving['left'] = True
        elif k in self.right_key:
            self.moving['right'] = True

    def handlekeyreleased(self, k): 
        if k in self.up_key:
            self.moving['up'] = False
        elif k in self.down_key:
            self.moving['down'] = False
        elif k in self.left_key:
            self.moving['left'] = False
        elif k in self.right_key:
            self.moving['right'] = False

    def move(self):
        # The +/- of up/down are inversed since 0 is the top of p5 coordinates
        if self.moving['up']:
            self.position.y -= 1.5
            if self.position.y - self.r <= 0:
                self.position.y = 0 + self.r
        if self.moving['down']:
            self.position.y += 1.5
            if self.position.y + self.r >= screen_height:
                self.position.y = screen_height - self.r
        if self.moving['left']:
            self.position.x -= 1.5
            if self.position.x - self.r <= 0:
                self.position.x = 0 + self.r
        if self.moving['right']:
            self.position.x += 1.5
            if self.position.x + self.r >= screen_width:
                self.position.x = screen_width - self.r

    # This is repurposed from a pong variant I made
    # It checks whether a circle overlaps w/ a rectangle
    def enter_location(self, location):   
        bottom = round(self.position.y - self.r)
        top = round(self.position.y + self.r)
        for i in range(bottom, top): # This passes through each y value in the player
            # This function returns where the edges of the circle are at that y value
            # The moment an edge touches the location, the player counts as entered
            high_x, low_x = self.each_point_on_circle(i)
            if high_x != 0 and low_x != 0: # The function returns 0 as a spillway for errors
                high_x_hit = location.position.x + location.w > high_x >= location.position.x
                low_x_hit = location.position.x < low_x <= location.position.x + location.w
                vertical_hit = location.position.y <= i <= location.position.y + location.h
                if high_x_hit or low_x_hit:
                    horizontal_hit = True
                else:
                    horizontal_hit = False
                # Means at least one point of the circle edge is within the shop frame
                if vertical_hit and horizontal_hit:
                    self.map = location.name

# Also from my pong game
    def each_point_on_circle(self, i):
        # circ_equation: r^2 = (x - h)^2 + (y - k)^2
        xminush_squared = self.r**2 - (i - self.position.y)**2
        if xminush_squared > 0: # Not sure how negatives appear, but the code crashes without this line
            position_xminush = math.sqrt(xminush_squared)
            neg_xminush = math.sqrt(xminush_squared)*-1 # I realized .sqrt only returns positive root not both
            pos_x = position_xminush + self.position.x
            neg_x = neg_xminush + self.position.x
            return pos_x, neg_x
        else:
            return 0, 0 # fallback if negatives somehow come up

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
    def __init__(self, position, width, height, name, r, g, b):
        self.position = position
        self.w = width
        self.h = height
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def render(self):
        # colors are arbitrary. just wanted to confirm text was there
        fill('white')
        rect((self.position), self.w, self.h)
        fill('black')
        text(self.name, self.position.x + 10, self.position.y)


def key_pressed(evt):
    jimmy.handlekeypressed(evt.key)

def key_released(evt):
    jimmy.handlekeyreleased(evt.key.name)

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
# Probably will have this generate randomly in future
pos = Vector(100, 200)
shop = Location(pos, 80, 40, 'Shop', 255, 255, 255)
locations.append(shop)
background_colors.append({
    'location': shop.name,
    'r': shop.r,
    'g': shop.g,
    'b': shop.b
})

def render_backdrop():
    for place in background_colors:
        if place['location'] == jimmy.map:
            background(place['r'], place['g'], place['b'])
    

def setup():
    size(screen_width, screen_height)
    arial = create_font("arial.ttf")
    text_font(arial)

def draw():
    render_backdrop()
    jimmy.render()
    jimmy.move()
    if jimmy.map == "Outdoors":
        for place in locations:
            place.render()
            jimmy.enter_location(place)
    if jimmy.map == "Shop":
        for item in shop_items:
            x_cord = screen_width*((shop_items.index(item)+1)/4)
            text(item.name, x_cord, 40)
    
run()
