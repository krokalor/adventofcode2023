"""
@author Karol K
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


input_file = 'Day7/input.txt'
cards = '23456789TJQKA'
types = (['high card', 'one pair', 'two pairs', 'three of a kind',
            'full house', 'four of a kind', 'five of a kind'])


def part1():
    """Part 1"""
    print('Running script for part 1 of day 7 of AoC23')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    bets = {}
    for c in [i.split() for i in lines]:
        bets[c[0]] = int(c[1])
    #
    ##
    points = {}
    for i in types:
        points[i] = []
    for h in bets:
        c = set(h)
        if len(c) == 5:
            points['high card'].append(h)
        elif len(c) == 4:
            points['one pair'].append(h)
        elif len(c) == 3:
            # print(h, 'Two pairs or three of a kind!')
            if h.count(max(c, key=lambda x: h.count(x))) > 2:
                points['three of a kind'].append(h)
            else:
                points['two pairs'].append(h)
        elif len(c) == 2:
            # print(h, 'Four of a kind or full house!')
            if h.count(max(c, key=lambda x: h.count(x))) > 3:
                points['four of a kind'].append(h)
            else:
                points['full house'].append(h)
        else:
            points['five of a kind'].append(h)
    #
    ##
    values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for i in range(2, 10):
        values[str(i)] = i
    strength = {j: [values[k] for k in j] for j in bets}
    #
    ##
    rank_map = {}
    m = 1
    total_winnings = 0
    for i in points:
        hands = points[i]
        if len(hands) > 0:
            print(i)
            hands.sort(key=lambda x: strength[x])
            for j in hands:
                print(j, strength[j], m)
                total_winnings += bets[j]*m
                rank_map[j] = f'{bets[j]}*{m}={bets[j]*m}'
                m += 1
    print('Total winnings:', total_winnings)
    return total_winnings


if __name__ == '__main__':
    part1()
