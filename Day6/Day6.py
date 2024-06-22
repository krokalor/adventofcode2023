"""
@author Karol K
"""

# from string import whitespace
# import numpy as np
# from termcolor import colored


input_file = 'Day6/input.txt'


def part1():
    """Part 1"""
    print('Running script for part 1 of day 6 of AoC23')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    races = {}
    t = lines[0].split(':')[1].split()
    d = lines[1].split(':')[1].split()
    races = {int(t[i]): int(d[i]) for i in range(len(t))}
    print(races)
    result = 1
    for i in races:
        print('\nRace time:', i, 'ms')
        print('Hold time [ms] distance [mm]')
        hold = 1  # speed equals hold time
        x = 0
        margin_of_error = 0
        while hold < i:
            if x > races[i]:
                margin_of_error += 1
                print(hold, x)
            hold += 1
            y = i - hold
            x = y*hold
        print('Margin of error:', margin_of_error)
        result *= margin_of_error
    return result


def part2():
    """Part 1"""
    print('Running script for part 2 of day 6 of AoC23')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    t = int(lines[0].split(':')[1].replace(' ', '').strip())
    d = int(lines[1].split(':')[1].replace(' ', '').strip())
    result = 1
    hold = 1  # speed equals hold time
    x = 0
    margin_of_error = 0
    while hold < t:
        if x > d:
            margin_of_error += 1
            # print(hold, x)
        hold += 1
        y = t - hold
        x = y*hold
    print('Margin of error:', margin_of_error)
    result *= margin_of_error
    return result


if __name__ == '__main__':
    print('\nResult:', part2())
