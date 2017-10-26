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
        cool = raw_input('Are these to your liking? (y/n) >')
        if cool.lower() == 'y':
            ability_generation = False
