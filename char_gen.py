'''
TODO:
[X] Flesh out abilitiy descriptions
[X] Thief talents
[X] More equipment options
[X] Mage spells!!!
[X] Cleric spells
[X] Improve class feature printing
[ ] Races
[X] XP bonus
[ ] Attribute score modifiers
[ ] Add more classes!
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
    'features': '''
*Attack Rate*
1/1 from 1st to 6th level, 3/2 from 7th to 12th.

*Heroic Fighting*
From 1st to 6th, double attacks per round against enemies with less than
2 HD. After 7th, applies for enemies with less than 3 HD.

*Weapon Mastery*
Choose two weapons. You have +1 to hit and damage and increased attack
rate. Additional weapons may be mastered at 4th, 8th and 12th levels.
Alternatively, a you may choose one particular previously-mastered weapon and
achieve grand mastery for an additional +1 to hit and damage.'''
}
mage = {
    'HD': 4,
    'saves': 'Device +2, Sorcery +2',
    'FA': [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'XP': [0, 0, 2.5e3, 5e3, 10e3, 20e3, 40e3, 80e3,
           160e3, 320e3, 480e3, 640e3, 800e3],
    'features': '''
*Magician\'s Familiar*
Summon a small animal (1d3+1 hp). You can see through its eyes as long as
it is within 120 ft. If it dies, you lose 1 hp per level.

*Sorcery*
Ability to cast spells memorized from an arcane tome. You can also decipher
otherwise unintelligible magical inscriptions or symbols, inscribe spells
upon magical scrolls (requires 500 gp + 100 gp/spell level), and brew magical
potions.'''
}
cleric = {
    'HD': 8,
    'saves': 'Death +2, Sorcery +2',
    'FA': [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8],
    'XP': [0, 2e3, 4e3, 8e3, 16e3, 32e3, 64e3,
           128e3, 256e3, 384e3, 512e3, 640e3],
    'features': '''
*Clerical Sorcery*
Through prayer, you can invoke the power of your deity to perform miracles,
inscribe spells upon holy scrolls (cost of 500 gp + 100 gp/spell level),

*Turn Undead*
Exert control over undead or demonic beings.'''
}
thief = {
    'HD': 6,
    'saves': 'Device +2, Avoidance +2',
    'FA': [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8],
    'XP': [0, 0, 1.5e3, 3e3, 6e3, 12e3, 24e3, 48e3,
           96e3, 192e3, 288e3, 384e3, 480e3],
    'features': '''
*Agile*
-1 AC when unarmoured and unencumbered.

*Backstab*
Sneaky attacks have a bonus to hit probability and damage.

*Thieves\' Cant*
You speak the secret language of criminals.

*Thief Skills*
You are proficient in all manner of skullduggery, specifically: climbing,
decipherment, careful listening, hiding, trap manipulation, moving silently,
lock picking, pick pocketing, and reading magical scrolls.'''
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
    return choice(skills)


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

    if 'none' in gear:
        gear.remove('none')
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


def FinalAbiPrinter(abilities, cla, level):
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
    classes = ['fighter', 'mage', 'cleric', 'thief']
    primes = [0, 3, 4, 1]
    prime = primes[classes.index(cla)]
    for i in range(6):
        supp = ''
        if i == prime:
            if abilities[i] > 15:
                supp = r' +10% XP bonus'
        output += labels[i] + ' ' + str(abilities[i]) + supp + '\n'
    return output


def AbiDialog():
    print 'Select your ability score generation method:'
    print '(3) 3d6--as Crom intended'
    print '(4) 4d6--drop lowest'
    print '(5) 5d6--drop lowest two'

    abilities = AbiRoller(int(raw_input('>')))

    print AbiPrinter(abilities)

    return abilities


def MageSpells(level):
    level1 = ['Alarm', 'Burning Hands', 'Charm Person', 'Dancing Lights',
              'Dash', 'Decipher Language', 'Detect Magic', 'Enlargement',
              'Feather Fall', 'Floating Disc', 'Friends', 'Grease',
              'Hold Portal', 'Identify', 'Influence Normal Fire', 'Jump',
              'Light', 'Magic Missile', 'Melt Ice', 'Mending', 'Message',
              'Mount', 'Protection from Evil/Good', 'Shield',
              'Shocking Grasp', 'Shove', 'Sleep', 'Sorcerer Mask',
              'Sorcerous Armor', 'Spider Climb', 'Unseen Servant',
              'Ventriloquism', 'Write Spell']
    level2 = ['Acid Arrow', 'Auditory Glamour', 'Continuous Light',
              'Cool Metal', 'Darkness', 'Detect Evil',
              'Detect Illusion', 'Detect Invisibility', 'Detect Silence',
              'Extra-dimensional Pocket', 'Extrasensory Perception',
              'Flaming Sphere', 'Fool\'s Gold', 'Glitterdust',
              'Gust of Wind', 'Invisibility', 'Knock', 'Levitate',
              'Locate Object', 'Magic Mouth', 'Mind Blank', 'Mirror Image',
              'Pyrotechnics', 'Ray of Enfeeblement', 'Scare', 'Shatter',
              'Sorcerer Lock', 'Stinking Cloud', 'Strengthen',
              'Summon Daemon I', 'Ungovernable Hideous Laughter',
              'Wall of Shadow', 'Web']
    level3 = ['Black Cloud', 'Blink', 'Cataleptic State', 'Clairaudience',
              'Clairvoyance', 'Dispel Magic', 'Explosive Runes', 'Fireball',
              'Flame Arrow', 'Fly', 'Haste', 'Hold Person', 'Infrared Vision',
              'Invisibility Hemisphere', 'Lightning Bolt', 'Phantasm',
              'Protection from Evil/Good 15 ft. r',
              'Protection from Ordinary Missiles', 'Rope Trick', 'Secret Page',
              'Sepia Snake Sigil', 'Shadow Sending', 'Slow', 'Suggestion',
              'Summon Monster I', 'Tiny Hut', 'Tongues', 'Twofold Missile',
              'Water Breathing', 'Wind Wall']
    level4 = ['Black Tentacles', 'Charm Monster', 'Confusion', 'Dig Hole',
              'Dimension Door', 'Dweomered Weapon', 'Extend Spell I', 'Fear',
              'Fire Shield', 'Fire Trap', 'Globe of Lesser Invulnerability',
              'Hallucinatory Terrain', 'Ice Javelin', 'Ice Storm',
              'Mass Treemorph', 'Mirror, Mirron', 'Mneumonic Enhancer',
              'Plant Growth', 'Polymorph Other', 'Polymorph Self',
              'Remove Curse', 'Resilient Sphere', 'Secure Shelter', 'Shout',
              'Sorcerer Eye', 'Stoneskin', 'Summon Daemon II',
              'Summon Monster II', 'Wall of Fire', 'Wall of Ice']
    level5 = ['Air-like Water', 'Animate Dead', 'Cloudkill', 'Cone of Cold',
              'Contact Otherworldly Being', 'Dismissal', 'Extend Spell II',
              'Fabricate', 'Faithful Hound', 'Feeblemind', 'Hold Monster',
              'Interposing Hand', 'Magic Jar', 'Passwall', 'Secret Chest',
              'Sending', 'Stone Shape', 'Summon Elemental',
              'Summon Monster III', 'Telekinesis', 'Teleport',
              'Transmute Rock to Mud', 'Wall of Force', 'Wall of Iron',
              'Wall of Stone']
    level6 = ['Anti-Magic Field', 'Chain Lightning', 'Control Water',
              'Control Weather', 'Controlled Blast Fireball', 'Death',
              'Disintegrate', 'Extend Spell III', 'Forceful Hand',
              'Freezing Sphere', 'Geas', 'Globe of Greater Invulnerability',
              'Guards and Wards', 'Legend Lore', 'Move Earth', 'Project Image',
              'Reincarnation', 'Repulsion', 'Stone to Flesh',
              'Summon Daemon III', 'Summon Invisible Stalker',
              'Summon Monster IV', 'Transformation']
    spell_catalog = [level1, level2, level3, level4, level5, level6]
    max_spell_progression = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    max_spell_level = max_spell_progression[level - 1]
    spells = []
    for i in range(3):
        new_spell = choice(level1)
        spells.append(new_spell)
        level1.remove(new_spell)
    for j in range(max_spell_level):
        new_spell = choice(spell_catalog[j])
        spells.append(new_spell)
        spell_catalog[j].remove(new_spell)
    return ', '.join(spells)


def ClericSpells(level):
    level1 = ['Bless', 'Bless Oil or Water', 'Ceremony of Consecration',
              'Cold Resistance', 'Command', 'Create Water', 'Cure Light Wounds',
              'Detect Evil', 'Detect Magic', 'Detect Malady', 'Light',
              'Magic Stone', 'Omen', 'Perceive Disguise', 'Precipitate',
              'Protection from Evil', 'Purify Food and Drink', 'Remove Fear',
              'Sanctuary']
    level2 = ['Aid', 'Augury', 'Cure Moderate Wounds', 'Darkness',
              'Delay Poison', 'Detect Silence', 'Distinguish Alignment',
              'Enthral', 'Find Traps', 'Fire Resistance', 'Hold Person',
              'Incantation', 'Invisibility to Undead', 'Serpent Charm',
              'Silence', 'Speak with Animals', 'Weird War Hammer',
              'Wyvern Warden']
    level3 = ['Animate Dead', 'Continuous Light', 'Create Food and Water',
              'Cure Blindness', 'Cure Deafness', 'Cure Disease', 'Dispel Magic',
              'Glyph of Warding', 'Locate Object', 'Magic Vestment',
              'Meld into Stone', 'Prayer', 'Remove Curse', 'Remove Paralysis',
              'Speak with Dead', 'Water Walk']
    level4 = ['Brink of Death', 'Control Water', 'Cure Serious Wounds',
              'Discern Lie', 'Divination', 'Imbue with Spell Ability',
              'Neutralize Poison', 'Perform Exorcism',
              'Protection from Evil 15 ft. radius', 'Scrying Font',
              'Shroud of Fear', 'Speak with Plants', 'Spike Growth', 'Them',
              'Tongues', 'Turn Sticks to Serpents']
    level5 = ['Air Walk', 'Atonement', 'Commune', 'Cure Critical Wounds',
              'Cure Madness', 'Dispel Evil', 'Finger of Death', 'Flame Strike',
              'Inoculate', 'Insect Plague', 'Plane Shift', 'Quest',
              'Raise Dead', 'True Seeing']
    level6 = ['Animate Objects', 'Blade Barrier', 'Communicate with Monsters',
              'Control Weather', 'Find the Path', 'Forbiddance', 'Heal',
              'Heroes\' Feast', 'Restoration', 'Stone Tell',
              'Summon Aerial Minion', 'Summon Animal I', 'Word of Recall']
    spell_catalog = [level1, level2, level3, level4, level5, level6]
    max_spell_progression = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    spells = []
    for j in range(level):
        for i in range(3):
            new_spell = choice(spell_catalog[max_spell_progression[j]])
            spells.append(new_spell)
            spell_catalog[max_spell_progression[j]].remove(new_spell)
    return ', '.join(spells)


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
        print >> f, 'Attributes and Statistics'
        print >> f, '-------------------------'
        print >> f, 'Hit Points:      ', hp
        print >> f, 'Armor Class:     ', ac
        print >> f, 'Damage Reduction:', dr
        print >> f, 'Fighting Ability:', classes[cla]['FA'][level]
        print >> f, 'Experience      :', int(classes[cla]['XP'][level])
        print >> f, FinalAbiPrinter(abilities, cla, level)
        print >> f, 'Saving Throw:', str(save)+',', classes[cla]['saves']
        print >> f, 'Background skill:', SecondarySkills()
        print >> f, ''
        print >> f, 'Gear'
        print >> f, '----'
        print >> f, textwrap.fill(gear)
        print >> f, ''
        print >> f, 'Class Features:'
        print >> f, '---------------'
        print >> f, classes[cla]['features']
        if cla == 'mage':
            print >> f, ''
            print >> f, 'Spells:'
            print >> f, '-------'
            spells = MageSpells(level)
            print >> f, textwrap.fill(spells)
        elif cla == 'cleric':
            print >> f, ''
            print >> f, 'Spells:'
            print >> f, '-------'
            spells = ClericSpells(level)
            print >> f, textwrap.fill(spells)
    print open('unnamed_hero.txt', 'r').read()
    print open('unnamed_hero.txt', 'r').read()
