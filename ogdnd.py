import random


class Character(object):
    name = 'John Doe'
    hp = 0
    xp = 0
    cla = ''
    attr = []
    inv = []

    def AC(self):
        return 10

    def Add(self):
        self.inv = self.inv

    def Remove(self):
        self.inv = self.inv

    def Weight(self):
        return 0


class Thief(Character):
    level = Character.xp + 1
    hd = 'd6'
    with open('specials/thief.txt', 'r') as f:
        specials = f.read()

    def GainHP(self):
        Character.hp = Character.hp + random.randint(1, int(self.hd[1:]))

    def Saves(self):
        return [0, 1, 2, 3][self.level]

    def Thac0(self):
        return 20


def GetBonus(score):
    bonuses = [-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
    mod = bonuses[score - 3]
    if mod > 0:
        mod = '+' + str(mod)
    elif mod == 0:
        mod = ''
    else:
        mod = str(mod)
    return mod


def d6():
    return random.randint(1, 6)


def GenAttributes(num_dice):
    attr = []
    for i in range(6):
        rolls = []
        for j in range(num_dice):
            rolls.append(d6())
        for k in range(num_dice - 3):
            rolls.remove(min(rolls))
        attr.append(sum(rolls))
    return attr


def PrintAttributes(attr):
    attr_names = ['STR:', 'DEX:', 'CON:', 'INT:', 'WIS:', 'CHA:']
    for i, score in enumerate(attr):
        mod = GetBonus(score)
        if score < 10:
            score = ' ' + str(score)
        print attr_names[i], score, mod


if __name__ == '__main__':
    fondag = Thief()
    fondag.name = 'Fondag the Great'
    fondag.attr = GenAttributes(3)
    print fondag.name
    PrintAttributes(fondag.attr)
