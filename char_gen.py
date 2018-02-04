'''
TODO:
[X] Flesh out abilitiy descriptions
[X] Thief talents
[X] More equipment options
[ ] Improve special ability printing
[ ] Spells!!!
[ ] Races
[ ] XP bonus
[ ] Attribute score modifiers
'''


from dice_things import AbiRoller, d
from random import choice
import textwrap


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
    'features': {
        'Read Scrolls': 'You can invoke cleric spells from scrolls.\n',
        'Scribe Scrolls':
            'You can write magical scrolls at a cost of 500 gp\n' +
            '100 gp per spell level\n',
        'Clerical Sorcery': 'Ability to cast clerical spells.\n',
        'Turn Undead': 'Exert control over undead or demonic beings.\n',
    }
}
thief = {
    'HD': 6,
    'saves': 'Device +2, Avoidance +2',
    'FA': [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8],
    'XP': [0, 0, 1.5e3, 3e3, 6e3, 12e3, 24e3, 48e3,
           96e3, 192e3, 288e3, 384e3, 480e3],
    'features': {
        'Agile':
            '-1 AC when unarmoured and unencumbered.\n',
        'Backstab':
            'An attack from behind with small melee weapon has a\n' +
            'bonus to hit chance and damage.\n',
        'Thieves\' Cant':
            'You speak the secret language of criminals.\n',
        'Thief Skills':
            'Check out the table. There\'s some straight up ninja shit.\n',
    }
}

classes = {'fighter': fighter, 'mage': mage, 'cleric': cleric, 'thief': thief}


def SecondarySkills():
    skills = ['Animal Trainer', 'Armorer', 'Cook', 'Barber', 'Inkeeper',
              'Blacksmith', 'Shipwright', 'Bookbinder', 'Bowyer',
              'Brewer', 'Vintner', 'Butcher', 'Carpenter', 'Cartwright',
              'Chandler', 'Peatman', 'Clothier', 'Cobbler', 'Cooper',
              'Engineer', 'Farmer', 'Fisherman', 'Furrier', 'Glazier',
              'Jailer', 'Gardener', 'Jeweller', 'Grocer', 'Guard',
              'Herdsman', 'Hunter', 'Tanner', 'Painter', 'Sculptor',
              'Messenger', 'Locksmith', 'Logger', 'Mason', 'Merchant',
              'Miller', 'Miner', 'Minstrel', 'Mortician', 'Navigator',
              'Potter', 'Riverman', 'Thatcher', 'Roper', 'Sailor',
              'Scribe', 'Soldier', 'Stabler', 'Weaponsmith', 'Tailor',
              'Teamster', 'Tinker']
    number_of_skills = len(skills)
    index = d(number_of_skills)
    return skills[index]


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

    armors = ['none', 'padded', 'leather', 'studded leather', 'scale',
              'chain mail', 'laminated', 'banded mail', 'splint', 'plate mail',
              'field mail', 'full plate']
    ac_array = [9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 2, 1]
    dr_array = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]

    light = ['torches (x3)', 'lamp (w/full flask of oil)']
    randos = ['chalk', 'ink and quill', 'hemp rope', 'incendiary oil', 'dice',
              'fishing net', 'glue', 'grappling hook', 'horn', 'marbles',
              'mirror', 'hammer and nails', 'needle and thread', 'crowbar',
              'collapsable 10-ft pole', 'soap', 'wooden stakes (x4)',
              'spool of wire', 'block of beeswax', 'mask']
    standard = ['backpack', 'wineskin', 'bandages', 'tinderbox',
                'trail rations (1 week)', str(d(10)+d(10))+' gp']

    if cla == 'fighter':
        armor = choice(armors[2:])
        weapon = choice(['warhammer', 'footman\'s mace', 'morning star',
                         'war pick', 'longsword', 'flail', 'bastard sword',
                         'great axe', 'halberd', 'great hammer', 'spear',
                         'scimitar', 'two-handed sword', 'pike'])
        missile = choice(['bola', 'sling', 'longbow (w/20 arrows)',
                          'composite bow (w/20 arrows)',
                          'shortbow (w/20 arrows)',
                          'light crossbow (w/20 bolts)',
                          'heavy crossbow (w/20 bolts)'])
    elif cla == 'mage':
        armor = 'none'
        weapon = choice(['dagger', 'quarterstaff'])
        missile = choice(['sling', 'darts'])
    elif cla == 'cleric':
        armor = choice(armors[2:])
        weapon = choice(['warhammer', 'footman\'s mace', 'morning star',
                         'war pick', 'longsword', 'flail', 'bastard sword',
                         'great axe', 'halberd', 'great hammer', 'spear',
                         'scimitar', 'pike'])
        missile = choice(['bola', 'sling',
                          'light crossbow (w/20 bolts)',
                          'heavy crossbow (w/20 bolts)'])
    elif cla == 'thief':
        armor = choice(armors[:4])
        weapon = choice(['dagger', 'longsword', 'short sword', 'falcata',
                         'war pick', 'flail', 'light mace', 'light hammer',
                         'scimitar'])
        missile = choice(['sling', 'darts',
                          'composite bow (w/20 arrows)',
                          'shortbow (w/20 arrows)',
                          'light crossbow (w/20 bolts)'])
    else:
        print 'Sorry, that class in not valid.'

    gear = [armor, weapon, missile, choice(light)] + standard

    for i in range(3):
        doohickey = choice(randos)
        gear.append(doohickey)
        randos.remove(doohickey)

    gear = ', '.join(gear)
    ac = ac_array[armors.index(armor)] - adj
    dr = dr_array[armors.index(armor)]

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
        print >> f, 'Background skill:', SecondarySkills()
        print >> f, ''
        print >> f, 'Gear'
        print >> f, '----'
        print >> f, textwrap.fill(gear)
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
    print open('unnamed_hero.txt', 'r').read()
