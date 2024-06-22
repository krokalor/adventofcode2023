"""
@author Karol K
"""

from string import whitespace

games = 'Day2/games_record.txt'
cubes = {'red': 12, 'green': 13, 'blue': 14}
cubes_in_game = {'red': 0, 'green': 0, 'blue': 0}

def part1():
    with open(games, 'r') as file:
        lines = file.readlines()
    id_sum = 0
    for l in lines:
        l = ''.join(c for c in l if c not in whitespace)
        game_id = int(l.split(':')[0].split('Game')[1])
        subsets = ','.join(l.split(':')[1].split(';'))
        valid = True
        for i in cubes.keys():
            nums = ([int(k) for k in
                    [j.replace(i, '') for j in subsets.split(',')]
                    if k.isnumeric()])
            if max(nums) > cubes[i]:
                valid = False
                break
            if not valid:
                break
        if valid:
            id_sum += game_id
        print(l)
        print(subsets)
        print(f'Game({game_id}):', cubes_in_game)
        print()
    print('Sum of ids of valid games:', id_sum)
    return id_sum

def part2():
    """Part 2"""
    with open(games, 'r') as file:
        lines = file.readlines()
    id_sum = 0
    powers_sum = 0
    for l in lines:
        l = ''.join(c for c in l if c not in whitespace)
        game_id = int(l.split(':')[0].split('Game')[1])
        subsets = ','.join(l.split(':')[1].split(';'))
        valid = True
        power = 1
        for i in cubes.keys():
            nums = ([int(k) for k in
                    [j.replace(i, '') for j in subsets.split(',')]
                    if k.isnumeric()])
            power *= max(nums)  # key=lambda x: x if x < cubes[i] else -1
            print(f'Power ({i}):', power)
        powers_sum += power
        if valid:
            id_sum += game_id
        print(l)
        print(subsets)
        print(f'Game({game_id}):', power)
        print()
    print('Sum of powers:', powers_sum)
    return id_sum


if __name__ == '__main__':
    part2()
