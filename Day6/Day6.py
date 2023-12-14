"""
@author Karol K
@date 14/12/2023
"""

# from string import whitespace
# import numpy as np
# from termcolor import colored


class Day6:
    """Day 5 solutions"""
    __input = 'input.txt'

    @staticmethod
    def part1(test=True):
        """Part 1"""
        print('Running script for part 1 of day 6 of AoC23')
        Day6.__input = 'test.txt' if test else Day6.__input
        with open(Day6.__input, 'r') as file:
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


    @staticmethod
    def part2(test=True):
        """Part 1"""
        print('Running script for part 2 of day 6 of AoC23')
        Day6.__input = 'test.txt' if test else Day6.__input
        with open(Day6.__input, 'r') as file:
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
    print('\nResult:', Day6.part2(False))
