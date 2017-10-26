from random import randint


def d(sides):
    '''a simple n-sided dice roller'''
    return randint(1, sides)


def AbiRoller(n):
    '''generates an ability score from the top 3d6 of nd6 rolled'''
    scores = []
    for i in range(6):
        rolls = []
        for j in range(n):
            rolls.append(d(6))
        for j in range(n-3):
            rolls.remove(min(rolls))
        scores.append(sum(rolls))

    return scores


if __name__ == '__main__':
    print AbiRoller(3)
