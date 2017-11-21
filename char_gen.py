'''
TODO:
    [ ] Casting/turning ability
    [ ] Thief talents
    [ ] Spells
    [ ] Secondary skills
    [ ] More equipment options
    [ ] More classes
'''


from dice_things import AbiRoller, d


saving_throws = [0, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 11]

fighter = {
    'HD': 10,
    'saves': 'Death +2, Transformation +2',
    'FA': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'XP': [0, 0, 2e3, 4e3, 8e3, 16e3, 32e3, 64e3,
           128e3, 256e3, 384e3, 512e3, 640e3],
    'features': {
        'Attack Rate': '1/1 from 1st to 6th level, 3/2 from 7th to 12th\n',
        'Heroic Fighting':
            'From 1st to 6th, double attacks per round against\n' +
            'enemies with less than 2 HD. After 7th, applies\n' +
            'for enemies with less than 3 HD.\n',
        'Weapon Mastery':
            'Choose two weapons. You have +1 to hit and damage \n' +
            'and increased attack rate. Additional weapons may\n' +
            'be mastered at 4th, 8th and 12th levels\n',
        'Grand Mastery':
            'At 4th level, gain an additional +1 attack/damage\n' +
            'with an already mastered weapon.\n',
    }
}
mage = {
    'HD': 4,
    'saves': 'Device +2, Sorcery +2',
    'FA': [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'XP': [0, 0, 2.5e3, 5e3, 10e3, 20e3, 40e3, 80e3,
           160e3, 320e3, 480e3, 640e3, 800e3],
    'features': {
        'Magician\'s Familiar':
            'Summon a small animal (1d3+1 hp). The mage\n' +
            'can see through its eyes as long as it is\n' +
            'within 120 ft. If it dies, mage loses 1 hp\n' +
            'per level.\n',
        'Read Magic':
            'Ability to decipher otherwise unintelligible magical\n' +
            'inscriptions or symbols.\n',
        'Scribe Scrolls':
            'Ability to inscribe spells upon magical scrolls.\n' +
            'Rquires 500 gp + 100 gp/spell level.\n',
        'Sorcery': 'Ability to cast spells memorized from an arcane tome.\n',
        'Alchemy': 'Ability to brew magical potions.\n'
    }
}
cleric = {
    'HD': 8,
    'saves': 'Death +2, Sorcery +2',
    'FA': [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8],
    'XP': [0, 2e3, 4e3, 8e3, 16e3, 32e3, 64e3,
           128e3, 256e3, 384e3, 512e3, 640e3],
    'features': ['Read Scrolls', 'Scribe Scrolls',
                 'Clerical Sorcery', 'Turn Undead'],
}
thief = {
    'HD': 6,
    'saves': 'Device +2, Avoidance +2',
    'FA': [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8],
    'XP': [0, 0, 1.5e3, 3e3, 6e3, 12e3, 24e3, 48e3,
           96e3, 192e3, 288e3, 384e3, 480e3],
    'features': ['Agile', 'Backstab', 'Thieves\' Cant', 'Thief Skills']
}

classes = {'fighter': fighter, 'mage': mage, 'cleric': cleric, 'thief': thief}


def Equipage(abilities, cla):
    dex = abilities[1]
    if dex < 4:
        adj = -2
    elif dex < 7:
        adj = -1
    elif dex < 15:
        adj = 0
    elif dex < 18:
        adj = 1
    else:
        dex = 2
    if cla == 'fighter':
        gear = ['Scale armour', 'battle axe', 'shortbow', 'arrow quiver',
                'arrows x12', 'backpack', 'bandages', 'soft leather pouch',
                'hemp rope', 'large sack', 'tinderbox', 'torches x2',
                'wineskin (full)', 'iron rations']
        ac = 6 - adj
        dr = 1
    elif cla == 'mage':
        gear = ['Silver dagger', 'quarterstaff', 'sling', 'bullets x20',
                'backpack', 'bandages', 'blanket', 'chalk', 'ink and quill',
                'incendiary oil', 'parchment x2', 'soft leather', 'pouch',
                'silk rope', 'small sack', 'tinderbox', 'torches x3',
                'wineskin (full)', 'writing stick', 'standard rations',
                'spellbook']
        ac = 9 - adj
        dr = 0
    elif cla == 'cleric':
        gear = ['Studded armour', 'dagger', 'warhammer', 'backpack',
                'bandages', 'soft leather pouch', 'small sack', 'tinderbox',
                'torches x3', 'wineskin (full)', 'writing stick',
                'iron rations', 'holy oil / water', 'silver holy symbol']
        ac = 6 - adj
        dr = 0
    elif cla == 'thief':
        gear = ['Leather armour', 'short sword', 'darts x2', 'backpack',
                'bandages', 'chalk', 'dice', 'fishing hooks x12',
                'fishing string', 'grappling hook', 'soft leather pouch',
                'silk rope', 'large sack', 'thieves\' tools', 'tinderbox',
                'torches x2', 'wineskin (full)', 'spool of wire',
                'writing stick', 'iron rations.']
        ac = 7 - adj
        dr = 0
    else:
        print 'Sorry, that class in not valid.'

    return gear, ac, dr


def GainHP(abilities, level, hd):
    hp = 0
    con = abilities[2]
    if con < 7:
        adj = -1
    elif con < 13:
        adj = 0
    elif con < 17:
        adj = 1
    elif con < 18:
        adj = 2
    else:
        adj = 3
    for i in xrange(level):
        hp += d(hd) + adj

    return hp


def AvailableClasses(abilities):
    '''Print the available classes given the indicated ability scores'''
    available = ['Fighter', 'Mage', 'Cleric', 'Thief']
    if abilities[0] < 9:
        available.remove('Fighter')
    if abilities[3] < 9:
        available.remove('Mage')
    if abilities[4] < 9:
        available.remove('Cleric')
    if abilities[1] < 9:
        available.remove('Thief')

    print '\nYou are capable of becoming:'
    print available
    return [k.lower() for k in available]


def AbiPrinter(abilities):
    labels = [
        'Strength:     ',
        'Dexterity:    ',
        'Constitution: ',
        'Intelligence: ',
        'Wisdom:       ',
        'Charisma:     ',
    ]
    output = ''
    output += ('\n')
    for i in range(6):
        output += labels[i] + ' ' + str(abilities[i]) + '\n'
    return output


def AbiDialog():
    print 'Select your ability score generation method:'
    print '(3) 3d6--as Crom intended'
    print '(4) 4d6--drop lowest'
    print '(5) 5d6--drop lowest two'

    abilities = AbiRoller(int(raw_input('>')))

    print AbiPrinter(abilities)

    return abilities


if __name__ == '__main__':
    print '\nWelcome to ASSHtonishing PC Generation! \n'

    ability_generation = True
    while ability_generation:
        abilities = AbiDialog()
        cool = raw_input('Are these to your liking? (y/n) \n>')
        if cool.lower() == 'y':
            ability_generation = False

    available = AvailableClasses(abilities)
    choosing_class = True
    while choosing_class:
        cla = raw_input('\nWhich do you choose?\n>').lower()
        if cla not in available:
            print 'I am sorry, try again.'
        else:
            print 'Excellent choice, '+cla+'!'
            choosing_class = False

    level = int(raw_input('\nAt what level will you start?\n>'))
    hp = GainHP(abilities, level, classes[cla]['HD'])
    save = saving_throws[level]
    gear, ac, dr = Equipage(abilities, cla)
    gear_str = ', '.join(gear)

    with open('unnamed_hero.txt', 'w') as f:
        print >> f, ''
        print >> f, 'Level', level, cla.upper()
        print >> f, '===================='
        print >> f, ''
        print >> f, 'Abilities and Attributes'
        print >> f, '------------------------'
        print >> f, 'Hit Points:      ', hp
        print >> f, 'Armor Class:     ', ac
        print >> f, 'Damage Reduction:', dr
        print >> f, 'Fighting Ability:', classes[cla]['FA'][level]
        print >> f, AbiPrinter(abilities)
        print >> f, 'Saving Throw:', str(save)+',', classes[cla]['saves']
        print >> f, ''
        print >> f, 'Gear'
        print >> f, '----'
        for i in range(len(gear_str)/80):
            print >> f, gear_str[i*80:(i+1)*80]
        print >> f, gear_str[(i+1)*80:]
        print >> f, ''
        print >> f, 'Class Features:'
        print >> f, '---------------'
        if type(classes[cla]['features']) is dict:
            for power in classes[cla]['features'].keys():
                print >> f, '*'+power+'*'
                print >> f, classes[cla]['features'][power]
        else:
            for power in classes[cla]['features']:
                print >> f, power
