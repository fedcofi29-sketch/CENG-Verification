class Player:
    def __init__(self, hp, strength, weapon, armor, money):
        self.health = hp
        self.strength = strength
        self.weapon = weapon
        self.armor = armor
        self.money = money

    def purchase(self, item):
        if self.money < item.cost:
            # Idk if this might be p5 instead so maybe print isn't best
            print('That is too expensive')