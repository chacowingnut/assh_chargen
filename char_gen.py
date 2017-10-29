'''
TODO:
    [x] Abiltity scores
    [ ] Class
    [ ] Alignment
    [ ] Background
    [ ] Gear
    [ ] Secondary stats
    [ ] Spells
'''


from dice_things import AbiRoller

fighter = {
    'HD': 'd10',
    'saves': 'Death +2, Transformation +2',
    'FA': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'XP': [0, 2e3, 4e3, 8e3, 16e3, 32e3, 64e3,
           128e3, 256e3, 384e3, 512e3, 640e3],
    'features': {
        'Attack Rate': '1/1 from 1st to 6th level, 3/2 from 7th to 12th',
        'Heroic Fighting': 'From 1st to 6th, double attacks per round against' +
                           'enemies with less than 2 HD. After 7th, applies' +
                           'for enemies with less than 3 HD.',
        'Weapon Mastery': '',
        'Gand Mastery': '',
    }
}

mage = {}
cleric = {}
thief = {}

classes = {'fighter': fighter, 'Mage': mage, 'cleric': cleric, 'thief': thief}


def AvailableClasses(abilities):
    '''Print the available classes given the indicated ability scores'''
    available = ['Fighter', 'Mage', 'Cleric', 'Thief']
    if abilities[0] < 10:
        available.remove('Fighter')
    if abilities[3] < 10:
        available.remove('Mage')
    if abilities[4] < 10:
        available.remove('Cleric')
    if abilities[1] < 10:
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
    print ''
    for i in range(6):
        print labels[i], abilities[i]
    print ''


def AbiDialog():
    print 'Select your ability score generation method:'
    print '(3) 3d6--as Crom intended'
    print '(4) 4d6--drop lowest'
    print '(5) 5d6--drop lowest two'

    abilities = AbiRoller(int(raw_input('>')))

    AbiPrinter(abilities)

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
        cla = raw_input('\nWhich do you choose?\n>')
        if cla.lower() not in available:
            print 'I am sorry, try again.'
        else:
            print 'Excellent choice, '+cla+'!'
            choosing_class = False
    print classes[cla]
