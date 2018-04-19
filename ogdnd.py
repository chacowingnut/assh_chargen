import random


class Character(object):
    name = 'John Doe'
    hp = 0
    xp = 0
    level = 0
    thac0 = 20
    save = 20
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
    cla = 'Thief'
    hd = '1d6'
    specials = 'Backstab, Thieves\' Cant, Special Derring-Do Skills'

    def ExpTable(self):
        xp_table = [1500, 3000, 6000, 12000, 23000, 48000,
                    96000, 192000, 288000, 384000, 480000]
        level = 1
        for i, entry in enumerate(xp_table):
            if entry < self.xp:
                level = i+2
        return level

    def GainLevel(self, message=False):
        new_level = self.ExpTable()

        if new_level == self.level:
            print 'You\'ve not enough XP to gain a level'
        else:
            self.thac0 = [20, 20, 19, 19, 18, 18,
                          17, 16, 16, 15, 14, 14][self.level]

            self.save = [0, 1, 2, 3, 4, 5, 6][self.level]

            d_index = self.hd.find('d')
            hp_gain = d(int(self.hd[d_index+1:])) + GetBonus(self.attr[2])
            if hp_gain < 0:
                hp_gain = 0
            self.hp += hp_gain
            if message:
                print (self.name, 'gained', hp_gain,
                       'hit points for a new total of', self.hp)
                self.hd = str(int(self.hd[:d_index])) + self.hd[d_index:]

            self.level += 1


def GetBonus(score):
    bonuses = [-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
    mod = bonuses[score - 3]
    return mod


def d(n):
    return random.randint(1, n)


def GenAttributes(num_dice):
    attr = []
    for i in range(6):
        rolls = []
        for j in range(num_dice):
            rolls.append(d(6))
        for k in range(num_dice - 3):
            rolls.remove(min(rolls))
        attr.append(sum(rolls))
    return attr


def PrintAttributes(attr):
    attr_names = ['STR:', 'DEX:', 'CON:', 'INT:', 'WIS:', 'CHA:']
    for i, score in enumerate(attr):
        mod = GetBonus(score)
        if mod > 0:
            mod = '+' + str(mod)
        elif mod == 0:
            mod = ''
        else:
            mod = str(mod)
        if score < 10:
            score = ' ' + str(score)
        print attr_names[i], score, mod


def PrintChar(char):
    print '\n', char.name
    print 'Level', char.level, char.cla, '\n'
    PrintAttributes(char.attr)
    print ''
    print 'HP:', char.hp, '     XP:', char.xp
    print 'AC:', char.AC(), ' THAC0:', char.thac0


if __name__ == '__main__':
    fondag = Thief()
    fondag.name = 'Fondag the Great'
    fondag.attr = GenAttributes(3)
    fondag.GainLevel()
    PrintChar(fondag)
