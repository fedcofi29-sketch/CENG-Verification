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
            pass
    

class Item:
    def __init__(self, type, cost, stats):
        self.type = type
        self.cost = cost
        self.stats = stats